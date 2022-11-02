from abc import ABCMeta, ABC, abstractmethod
import cv2
import logging
class PredictorInterface(ABC):
    @abstractmethod
    def predict(self, img):
        """识别图像

        Args:
            img ([type]): [description]
        """
        pass
    def drawBox(self, image, box):
        if box is None:
            logging.warning(f"box is None")
            return
        x0 = int(box[0])
        y0 = int(box[1])
        x1 = int(box[0] + box[2])
        y1 = int(box[1] + box[3])

        cv2.rectangle(image,(x0, y0), (x1, y1), (255, 255, 0), 1)
        
    @abstractmethod
    def drawResult(self, image, result):
        """显示识别结果

        """
        pass
    @abstractmethod
    def getiuv(self, result):
        """ 从结果中提取i、u、v、box"""
        """ keypoint方法从结果中提取box、keypoints"""
        pass    