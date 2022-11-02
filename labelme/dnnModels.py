from abc import ABCMeta, ABC, abstractmethod
import argparse
import os
import cv2
import numpy as np
from argparse import ArgumentParser
import logging as log

# from mmpose.apis import (inference_top_down_pose_model, init_pose_model,
#                         vis_pose_result)
from labelme.shape import Shape
from qtpy import QtCore
from qtpy import QtGui
from labelme.utils.buildKeypointNames import buildKeypointNames, drawKeypoints
# from labelme.utils.buildKeypointNames import JingluoNames
class IModel(ABC):
    @abstractmethod
    def predict(self, img)->dict:
        """识别图像，得到shapes

        Args:
            img ([type]): [图像]

        Returns:
            dict: [shapes]
        """
    pass

class BoxModel(IModel):
    """识别box

    Args:
        IModel ([type]): [description]
    """
    def __init__(self):
        pass
    def predict(self, img)->dict:
        pass

def process_mmdet_results(mmdet_results, cat_id=0):
    """Process mmdet results, and return a list of bboxes.

    :param mmdet_results:
    :param cat_id: category id (default: 0 for human)
    :return: a list of detected bounding boxes
    """
    if isinstance(mmdet_results, tuple):
        det_results = mmdet_results[0]
    else:
        det_results = mmdet_results
    return det_results[cat_id]

class KeypointModel(IModel):
    """识别Keypoints

    Args:
        IModel ([type]): [description]
    """
    def __init__(self, wholePart, g_modelAccu):
        self.wholePart = wholePart
        self.g_modelAccu = g_modelAccu
        print("init KeypointModel ....")
        # AllJingluoNames, JingluoNames, skeleton, skelecolor, kptcolor, name2index, = buildKeypointNames(namedict)
        # self.keypointNames = AllJingluoNames       
        # self.allLabelNames = AllJingluoNames
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--version", "-V", action="store_true", help="show version"
        )     
        parser.add_argument(
            '--device', default='cuda:0', help='Device used for inference')
        parser.add_argument(
            '--bbox-thr',
            type=float,
            default=0.8,
            help='Bounding bbox score threshold')
        parser.add_argument(
            '--kpt-thr', type=float, default=0, help='Keypoint score threshold')           
        args = parser.parse_args()
        args.det_config = "configs/hrnet/hrnet_sy_wei.py"
        args.det_checkpoint = "models/hrnet_sy_wei_mmdectection.pth"
        # args.pose_config = "configs/hrnet/hrnet_w48_coco_wholebody_384x288_dark_plus_gan.py"
        # args.pose_checkpoint = "models/epoch_800.pth"
        args.device='cpu'
        self.args = args
        self.det_model = None

        # build the pose model from a config file and a checkpoint file
        # self.pose_model = init_pose_model(
        #     args.pose_config, args.pose_checkpoint, device=args.device)
        print("init KeypointModel done!")
        return

    def predict(self, image_name, modelName)->dict:
        # from mmdet.apis import inference_detector, init_detector
        
        # model = self.modelsManager.getModel(modelName)
        # print("dnnModel predicting ...")
        # if model is None:
        #     print(f"warning: model:{modelName} is None")
        #     return None
        # if self.det_model is None:
        #     self.det_model = init_detector(
        #         self.args.det_config, self.args.det_checkpoint, device=self.args.device)
        # # test a single image, the resulting box is (x1, y1, x2, y2)
        
        # mmdet_results = inference_detector(self.det_model, image_name)

        # # keep the person class bounding boxes.
        # person_bboxes = process_mmdet_results(mmdet_results)

        # # test a single image, with a list of bboxes.

        # # optional
        # return_heatmap = False

        # # e.g. use ('backbone', ) to return backbone feature
        # output_layer_names = None
        
        # pose_results, returned_outputs = inference_top_down_pose_model(
        #     pose_model,
        #     image_name,
        #     person_bboxes,
        #     bbox_thr=self.args.bbox_thr,
        #     format='xyxy',
        #     dataset='TopDownCocoWholeBodyDataset',
        #     return_heatmap=return_heatmap,
        #     outputs=output_layer_names)
        # camera = image_name.split(r"/")[-1][:1]
        camera = modelName.split("_")[0][0]
        colorimg1 = cv2.imread(image_name)
        if camera == "r":
            colorimg1 = cv2.flip(colorimg1,0)
            modelName = modelName.replace("right","left")


        boxes, keypoints0 = self.wholePart.predict(colorimg1, 0, modelName,camera)
        if boxes is None:
            return None

        
        showimg = colorimg1.copy()

        if camera == "r":
            # depthimg = cv2.flip(depthimg,0)
            showimgnew = cv2.flip(colorimg1,0)
            keypoints = keypoints0.copy()
            keypoints[:,1] = colorimg1.shape[0] - keypoints[:,1]
            modelName = modelName.replace("left","right")
            print("------------------------------------------------------------------------")
            print(modelName)
            print("------------------------------------------------------------------------")
            

            accuNames = self.wholePart.modelAllCfg[modelName]['accuNames']
            drawKeypoints(showimgnew, keypoints,accuNames, boxes)
            
            drawimg = showimgnew

            
 


        else:
            keypoints = keypoints0.copy()
            accuNames = self.wholePart.modelAllCfg[modelName]['accuNames']
            ##drawKeypoints(图片，预测的点，模型对应的经络穴位，人形框)
            drawKeypoints(showimg, keypoints, accuNames, boxes)
            drawimg = showimg
        
        # cv2.imshow("img", drawimg)
        # cv2.waitKey(30)

        # drawKeypoints(colorimg1, keypoints0,  self.wholePart.modelAllCfg[modelName]['accuNames'], boxes)
        # drawimg = colorimg1
        if False:
            windowName = "whole:" + modelName
            cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
            cv2.imshow(windowName, drawimg)
            cv2.waitKey(50)

        assert len(keypoints) > 0 
        kpnames =  self.g_modelAccu[modelName]
        assert len(kpnames) > 0
        shapes = self.buildShapes(boxes, keypoints, kpnames)
        assert len(shapes) > 0
        print("dnnModel predict finished!")
        return shapes, drawimg
    def buildBoxshape(self, boxes):
        shape = Shape(label='person',shape_type='rectangle', flags = {})
        shape.addPoint(QtCore.QPointF(boxes[0], boxes[1]))
        shape.addPoint(QtCore.QPointF(boxes[2], boxes[3]))
        return shape
    def buildKeypointShape(self, label, x_coord, y_coord):
        shape = Shape(label=label,shape_type='point', flags = {})
        shape.addPoint(QtCore.QPointF(x_coord, y_coord))  
        return shape
    def buildShapes(self, boxes, keypoints0, kpNames):
        shapes = []
        bbox_result = []
        pose_result = []
        # for res in zip():
        bbox_result.append(boxes)
        pose_result.append(keypoints0)
        if len(bbox_result) > 0:
            bboxes = np.vstack(bbox_result)
            
            boxshape = self.buildBoxshape(bbox_result[0])
            shapes.append(boxshape)
            
            for _, kpts in enumerate(pose_result):
                # draw each point on image
                    for kid, kpt in enumerate(kpts):
                        x_coord, y_coord, kpt_score = int(kpt[0]), int(
                            kpt[1]), kpt[2]
                        if kpt_score > self.args.kpt_thr:
                            label = kpNames[kid]
                            shape = self.buildKeypointShape(label, x_coord, y_coord)
                            shapes.append(shape)
                    break
        assert len(shapes) > 0
        return shapes


