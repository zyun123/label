import os
# from labelme.src.base.recognize.base.predictor import Predictor
import logging


class ModelsManager:
    def __init__(self, modelCfgs:dict, modeldir, device='cuda:0') -> None:
        self.cameraModels = {}
        # self.kpFramework = kpFramework
        self.modelCfgs = modelCfgs
        self.models = {}
        self.device = device
        self.modeldir = modeldir
        pass
    def initAnModel(self, cfg, modelpath, kpframework, modelName= None):
        from labelme.src.base.recognize.base.kppredictor import KpPredictor
        from labelme.src.base.recognize.base.mmposePredictor import MmposePredictor        
        model = None
        predictor = None
        if kpframework == "detectron2":
            predictor = KpPredictor(cfg, modelpath, modelName)
        elif kpframework == "mmpose" or kpframework is None or kpframework == "":
            predictor = MmposePredictor(cfg, modelpath, modelName, self.device)
        return predictor
    def getModel(self, modelName):
        if modelName not in self.models:
            if modelName in self.modelCfgs:
                cfg = self.modelCfgs[modelName]
                model = self.initAnModel("configs/" + cfg[0], os.path.join(self.modeldir, cfg[1]), cfg[2], modelName)
                self.models[modelName] = model
                return model
            else:
                logging.error(f"{modelName} not configured")
                return None
        else:
            return  self.models[modelName]
    def getCameraModels(self, cameraModelNames:dict)->dict:
        cameraModels = {}
        for camera in cameraModelNames:
            modelNames = cameraModelNames[camera]
            models = []
            for modelName in modelNames:
                model = None
                if modelName not in self.models:
                    if modelName not in self.modelCfgs:
                        print("warning: model: {} is not configured".format(modelName))
                    else:
                        cfg = self.modelCfgs[modelName]
                        model = self.initAnModel("configs/" + cfg[0], os.path.join(self.modeldir, cfg[1]), cfg[2], modelName)
                        self.models[modelName] = model
                else:
                    model = self.models[modelName]
                models.append((modelName, model))
            cameraModels.update({camera:models})
        return cameraModels
def test_ModelsManager():
    from labelme.src.base.recognize.base.models_accuNames import Models_JingluoNames
    modelCfgs = Models_JingluoNames.getModelCfg()
    cameraOrder = "mlhr"
    aModelsManager = ModelsManager(modelCfgs)
    cameraModelNames = Models_JingluoNames.getCameraModelNames(cameraOrder, ["gan_l","fei_l", "fei_r"])
    # cameraModelNames = ['left_gan', 'middle_fei']
    cameraModels = aModelsManager.getCameraModels(cameraModelNames)
    print("cameraModels", cameraModels)
    pass

if __name__ == "__main__":
    test_ModelsManager()