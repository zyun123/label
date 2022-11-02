import argparse
import copy
import logging
import pickle
import torch
import numpy as np
from typing import Any, ClassVar, Dict, List

from labelme.src.base.recognize.base.predictorInterface import PredictorInterface
import os
import cv2
from argparse import ArgumentParser

from mmdet.apis import inference_detector, init_detector

from mmpose.apis import (inference_top_down_pose_model, init_pose_model,
                         vis_pose_result)

from labelme.utils.buildKeypointNames import skeletonFromAccunames
from labelme.src.base.recognize.base.models_accuNames import Models_JingluoNames, g_modelAccu


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


class MmposePredictor(PredictorInterface):
    def __init__(self, mmcfg, mmmodel, modelName, device='cuda:0'):
        det_config = "configs/hrnet/hrnet_sy_wei.py"
        det_checkpoint ="/home/sy/models/hrnet_sy_wei_mmdectection.pth"  
        self.kptnames =  g_modelAccu[modelName]
        self.skeleton, self.skelecolor, self.kptcolor, name2index = skeletonFromAccunames(self.kptnames)

        self.det_model = init_detector(
            det_config, det_checkpoint, device)
        # build the pose model from a config file and a checkpoint file
        self.pose_model = init_pose_model(
            mmcfg, mmmodel, device)
        self.modelName = modelName
        

        
    
    def predict(self, image):
        """识别图像

        Args:
            img ([type]): [description]
        """
   # test a single image, the resulting box is (x1, y1, x2, y2)
        mmdet_results = inference_detector(self.det_model, image)

        # keep the person class bounding boxes.
        person_bboxes = process_mmdet_results(mmdet_results)

        # test a single image, with a list of bboxes.

        # optional
        return_heatmap = False

        # e.g. use ('backbone', ) to return backbone feature
        output_layer_names = None

        pose_results, returned_outputs = inference_top_down_pose_model(
            self.pose_model,
            image,
            person_bboxes,
            bbox_thr= 0.1,
            format='xyxy',
            dataset="TopDownCocoWeijingDataset",
            return_heatmap=return_heatmap,
            outputs=output_layer_names)

        return pose_results
    
    def drawResult(self, image, pose_results):
        """显示识别结果

        """
        # Convert image from OpenCV BGR format to Matplotlib RGB format.
        image = image[:, :, ::-1]
        # show the results
        img = vis_pose_result(
            self.pose_model,
            image,
            pose_results,

            self.skeleton,
            self.skelecolor,
            self.kptcolor, 
            self.kptnames,
            dataset="TopDownCocoWeijingDataset",
            kpt_score_thr= 0.1,
            show= None,
            out_file= None)
        smallimg = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2) )
        cv2.imshow("img", smallimg)
        cv2.waitKey(100)
        return img
        
    def getiuv(self, predictions):
        """ 从结果中提取keypoints、box"""
        rbbox = None
        rkeypoints = None
        maxArea = 0
        for result in predictions:
            bbox = result['bbox'][0]
            keypoints = result['keypoints']
            area = bbox[2] * bbox[3]
            if area > maxArea:
                maxArea = area
                rbbox = bbox
                rkeypoints = keypoints

        return rbbox, rkeypoints
def test_MmposePredictor():
    from labelme.src.gui.args import parse_args, load_args
    args = parse_args()
    labelme_directory = "/mnt/data/samples/upward/suit540/v3_1_xinbao/test"
    args.det_config = "/mnt/data/models/configs/hrnet/hrnet_sy_wei.py"
    args.det_checkpoint ="/mnt/data/models/models/hrnet_sy_wei_mmdectection.pth"
    # modelCfg["left_gan"] = ["configs/kp_01_18_gan_left.yaml","models/model_0005999_7_gan_left.pth", "detectron2"]
    namedictgan = {"L-gan":[(1,2),(13,18)],"R-gan":[(3,12)]}
    # namedictxinbao = {"L-xinbao":[(1,9)],"R-xinbao":[(1,9)]}
  
    output = "/mnt/data/samples/upward/suit540/v3_1_xinbao/test1.json"
    img= cv2.imread("/mnt/data/samples/upward/suit540/v3_1_xinbao/test/middle_0026.jpg")
    predictor = MmposePredictor("/home/sy/working/vision/label/configs/hrnet/hrnet_w48_coco_wholebody_384x288_dark_plus_gan.py", \
        "/home/sy/models/mmpose_gan_epoch_800.pth", "left_gan")
    results = predictor.predict(img)
    show = predictor.drawResult(img, results)
    cv2.imshow("ii", show)
    cv2.waitKey(0)    
    boxes, keypoints = predictor.getiuv(results)
    print(boxes)
    print(keypoints)
if __name__ == "__main__":
    test_MmposePredictor()



      