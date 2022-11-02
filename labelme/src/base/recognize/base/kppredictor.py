import argparse
import copy
import logging
import pickle
import torch
import cv2
import numpy as np
from typing import Any, ClassVar, Dict, List

from labelme.src.base.recognize.base.predictorInterface import PredictorInterface
from detectron2.config import get_cfg

from detectron2.data import MetadataCatalog
from detectron2.engine.defaults import DefaultPredictor
from detectron2.utils.visualizer import ColorMode, Visualizer
from labelme.utils.buildKeypointNames import buildKeypointNames, drawKeypoints
from labelme.src.base.recognize.base.models_accuNames import g_modelAccu

LOGGER_NAME = "kppredictor"
logger = logging.getLogger(LOGGER_NAME)
#  namedictgan = {"L-gan":[(1,2),(13,18)],"R-gan":[(3,12)]}
def setup_config(config_fpath: str, model_fpath: str
    ):
    cfg = get_cfg()
    # add_densepose_config(cfg)
    cfg.merge_from_file(config_fpath)
    # cfg.merge_from_list(args.opts)
    # if opts:
    #     cfg.merge_from_list(opts)
    cfg.MODEL.WEIGHTS = model_fpath
    cfg.freeze()
    return cfg
class KpPredictor(PredictorInterface):
    def __init__(self,cfg, model, modelName):
        # self.predictor = self._setup_model( cfg, model)
        self.predictor, cfg = self._setup_model(cfg, model)
        self.metadata = MetadataCatalog.get(
            cfg.DATASETS.TEST[0] if len(cfg.DATASETS.TEST) else "__unused"
        )       
        self.instance_mode=ColorMode.IMAGE
        self.modelName = modelName
        self.keypointNames = g_modelAccu[modelName]
        # self.cpu_device = torch.device("cpu")
    def _setup_model(self,  cfg, model): 
         # args.cfg = "configs/densepose_rcnn_R_50_FPN_s1x.yaml"
        opts = []
        cfg = setup_config(cfg, model)
        logger.info(f"Loading model from {model}")
        predictor = DefaultPredictor(cfg)
        return predictor, cfg        
  
    
    def predict(self, image):
        """识别图像

        Args:
            img ([type]): [description]
        """
        from src.gui.args import g_args as args
        if args.detail >= 4:
            cv2.imshow("image kppredictor", image)
            cv2.waitKey(90)
        predictions = self.predictor(image)
        return predictions
    
    def drawResult(self, image1, predictions):
        """显示识别结果

        """
        # Convert image from OpenCV BGR format to Matplotlib RGB format.
        image = image1.copy()
        # visualizer = Visualizer(image, self.metadata, instance_mode=self.instance_mode)

        # if "instances" in predictions:
        #     print('debug: run_on_image: else: instances: ok')
        #     instances = predictions["instances"].to(self.cpu_device)
        #     vis_output = visualizer.draw_instance_predictions(predictions=instances)
        #     print('debug: run_on_image: else: instances: vis_output:', vis_output)
        # else:
        #     assert False
        rbbox, rkeypoints = self.getiuv(predictions)
        if rbbox is None:
            logging.warning("noting to draw")
            return None
        self.drawBox(image,rbbox)
        drawKeypoints(image, rkeypoints,self.keypointNames)
        return image
        
    def getiuv(self, predictions):
        """ 从结果中提取keypoints、box"""
        instances = predictions['instances']
        boxes = instances.pred_boxes if instances.has("pred_boxes") else None
        # scores = predictions.scores if predictions.has("scores") else None
        # classes = predictions.pred_classes if predictions.has("pred_classes") else None
        # labels = _create_text_labels(classes, scores, self.metadata.get("thing_classes", None))
        keypoints = instances.pred_keypoints if instances.has("pred_keypoints") else None
        boxesList = boxes.tensor.tolist()
        keypointsList = keypoints.cpu().numpy()
        rbbox = None
        rkeypoints = None
        maxArea = 0
        for bbox, keypoints1 in zip(boxesList, keypointsList):
            # bbox = result['bbox'][0]
            # keypoints = result['keypoints']
            # w = 
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            assert w > 0 and h > 0 
            area = (w) * (h)
            if area > maxArea:
                maxArea = area
                rbbox = bbox
                rkeypoints = keypoints1
        # assert maxArea > 300 * 300
        return rbbox, rkeypoints        
        # return boxes.tensor.tolist(), keypoints1          
g_modelAccu

if __name__ == "__main__":
    from src.gui.args import parse_args, load_args
    import cv2
    args = parse_args()
    cfg, model, k = ["configs/kp_middle_down_wai_dachang_xiaochang_sanjiao_pangguang.yaml","/mnt/data/new_mergeDataToModel/models_middle_down_wai_dachang_sanjiao_xiaochang_paguang/model_final.pth", "detectron2"]
    predictor = KpPredictor(cfg, model, "left_gan")
    
    img= cv2.imread("/mnt/data/samples/upward/suit540/v3/v3_1_xinbao/test/middle_0026.jpg")

    results = predictor.predict(img)
    show = predictor.drawResult(img, results)
    boxes, keypoints = predictor.getiuv(results)
    cv2.imshow("ii", show)
    cv2.waitKey(0)    