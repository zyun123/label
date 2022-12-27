import time
# import cv2
import copy
import numpy as np
import logging
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
from abc import ABCMeta, ABC, abstractmethod
from labelme.src.base.recognize.composite.modelsManager import ModelsManager
from labelme.utils.buildKeypointNames import buildKeypointNames, drawKeypoints

class KpWholePart():        
    def __init__(self, modelAllCfg, modelsManager:ModelsManager, partRadius):
        """
        partRadius3840
        """
        #whole model {'modelname':modelName,'trainmodel':trainmodel, 'accunames':accunames}
        #parts {'models'}:[ [partname, model1, handfootCenterAccuname, 'accunames':accunames], [model2, ], ...]
        
        self.modelsManager = modelsManager    
        self.modelAllCfg = modelAllCfg
        self.partRadius = partRadius
        self._isUsePartmodels = True
    def setUsePartModels(self, isusePartmodels):
        self._isUsePartmodels = isusePartmodels
    def predict(self, img, cameraIndex, modelName,camera):
        """识别图像

        Args:
            img ([type]): [description]
        """
        # cv2.imshow(f"img{cameraIndex}" , img)
        # cv2.waitKey(50)
        time1 = time.time()
        whole_model  =self.modelsManager.getModel(modelName)
        time2 = time.time()
        whole_results = whole_model.predict(img)
        time3 = time.time()
        rbbox, rkeypoints   = whole_model.getiuv(whole_results)
        if rbbox is None:
            logging.warning("nothing recognized")
            return  None, None

        # keypointnames = self.modelAllCfg[modelName]['accuNames']
        # showimg = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # showimg = img.copy()
        # drawKeypoints(showimg, rkeypoints, keypointnames,rbbox)
        # cv2.waitKey(0)
        # cv2.imshow(f"{modelName}{cameraIndex}" , showimg)
        # cv2.waitKey(50)

        if not self._isUsePartmodels:
            return rbbox, rkeypoints

        parts = self.modelAllCfg[modelName]['submodels']


        # if camera == 'm':
        #     img = cv2.flip(img.copy(),0)
        #     for partName, centerAccname in parts.items():
        #         part_bbox, part_resultbox, part_keypoints = self._recogize_parts(img, rbbox, rkeypoints,modelName, partName, centerAccname, cameraIndex)


        for partName, centerAccname in parts.items():
            
            if camera == 'm' and partName.startswith("right"):
                partName_left = partName.replace("right","left",1)
                centerAccname_left = centerAccname.replace("R","L")
                img1 = cv2.flip(img.copy(),0)
                part_bbox, part_resultbox, part_keypoints = self._recogize_parts(img1, rbbox, rkeypoints,modelName, partName_left, centerAccname_left, cameraIndex)
                if not part_resultbox  is None:

                    self._mergeResults_right(rkeypoints, modelName, partName, centerAccname, part_bbox, part_keypoints, cameraIndex,img1)

            else:
                    
                part_bbox, part_resultbox, part_keypoints = self._recogize_parts(img, rbbox, rkeypoints,modelName, partName, centerAccname, cameraIndex)
                if not part_resultbox  is None:
                    self._mergeResults(rkeypoints, modelName, partName, centerAccname, part_bbox, part_keypoints, cameraIndex)
            time4 = time.time()
            logging.warning(f"{cameraIndex}:all:{time4-time1}, getModel:{time2-time1}, whole_model:{time3-time2}, _recogize_parts:{time4-time3}")
        return rbbox, rkeypoints
    def _calcCenterKeypoint(self, rkeypoints, wholeModelName, partName, centerAccuname):
        wholeAccunames = self.modelAllCfg[wholeModelName]['accuNames']

        index = wholeAccunames.index(centerAccuname)
        centerKeypoint = rkeypoints[index]
        return centerKeypoint

    def _calcRoiRectangle(self, centerKeypoint, imgshape):
        '''获得局部矩形框'''
        roiRectangle = [0,0,0,0]
        radius = self.partRadius * imgshape[0] / 2160 
        roiRectangle[0] = int(max(centerKeypoint[0] - radius, 0))
        roiRectangle[1] = int(max(centerKeypoint[1] - radius, 0))
        roiRectangle[2] = int(min(centerKeypoint[0] + radius, imgshape[1] - 1))
        roiRectangle[3] = int(min(centerKeypoint[1] + radius, imgshape[0] - 1))
        return roiRectangle
    def _recogize_parts(self, img, rbbox, rkeypoints, wholeModelName, partName, centerAccuname, cameraIndex):
        centerKeypoint = self._calcCenterKeypoint(rkeypoints, wholeModelName, partName, centerAccuname)
        roiRectangle = self._calcRoiRectangle(centerKeypoint, img.shape)
        roiImage = img[ roiRectangle[1]:roiRectangle[3], roiRectangle[0]:roiRectangle[2]]
        partModel = self.modelsManager.getModel(partName)
        if not partModel is None:
            predictions  = partModel.predict(roiImage)
            part_resultbox, part_keypoints = partModel.getiuv(predictions)
            drawimg = partModel.drawResult(roiImage, predictions)
            if drawimg is not None:
                # cv2.imshow(f"{partName}{cameraIndex}", drawimg)
                # cv2.waitKey(50)
                pass
            return roiRectangle, part_resultbox, part_keypoints
        else:
            logging.error(f"{partName}" is None)
            return None, None, None
        
    def _mergeResults(self, rkeypoints, wholeModelName, partName, centerAccuname, part_bbox, part_keypoints, cameraIndex):
        partAccuNames = self.modelAllCfg[partName]['accuNames']
        wholeAccunames = self.modelAllCfg[wholeModelName]['accuNames']
        for partindex, accuname in enumerate(partAccuNames):
            index = wholeAccunames.index(accuname)
            kp = part_keypoints[partindex]
            kp[0] = part_keypoints[partindex][0] + part_bbox[0]
            kp[1] = part_keypoints[partindex][1] + part_bbox[1]
            rkeypoints[index] = kp
        return

    def _mergeResults_right(self, rkeypoints, wholeModelName, partName, centerAccuname, part_bbox, part_keypoints, cameraIndex,img):
        partAccuNames = self.modelAllCfg[partName]['accuNames']
        wholeAccunames = self.modelAllCfg[wholeModelName]['accuNames']
        for partindex, accuname in enumerate(partAccuNames):
            index = wholeAccunames.index(accuname)

            kp = part_keypoints[partindex]
            kp[0] = part_keypoints[partindex][0] + part_bbox[0]
            kp[1] = img.shape[0]-(part_keypoints[partindex][1] + part_bbox[1])

            rkeypoints[index] = kp
        return
 
    def drawBox(self, image, box):
        x0 = int(box[0])
        y0 = int(box[1])
        x1 = int(0 + box[2])
        y1 = int(0 + box[3])

        cv2.rectangle(image,(x0, y0), (x1, y1), (255, 255, 0), 1)
        
        


def test_KpWholePart():
    
    from src.base.recognize.base.models_accuNames import Models_JingluoNames, g_modelAccu, g_jingluoDict
    from src.base.recognize.composite.modelsManager import ModelsManager  
    modelCfgs = Models_JingluoNames.getModelCfg()
    modelAllcfgs = Models_JingluoNames.getModelAllCfg()
    modeldir = "/home/sy/share/data/models/d2"
    modelName = 'left_up_nei'
    image = cv2.imread("/mnt/data/mergeData/result/finally_Merged_dan_left_up_neiba/test/head_0002.jpg")
    cameraIndex = 0
    modelsManager = ModelsManager(modelCfgs,modeldir)
    kpWholePart = KpWholePart(modelAllcfgs, modelsManager, 225)
    rbbox, rkeypoints = kpWholePart.predict(image, cameraIndex, modelName)
    keypointnames = modelAllcfgs[modelName]['accuNames']
    drawKeypoints(image, rkeypoints, keypointnames,rbbox)
    cv2.imshow(f"wholeimage: {modelName}{cameraIndex}" , image)
    cv2.waitKey(50)
    pass

if __name__ == "__main__":
    test_KpWholePart()
