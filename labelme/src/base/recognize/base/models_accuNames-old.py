from labelme.utils.buildKeypointNames import buildKeypointNames, g_jingluoNames
import json


class Models_JingluoNames:
    """经络名～拐点名

        经络名～模型名～摄像头之间的关系
    Returns:
        [type]: [description]
    """

    # ###########################################################################################################
    # # 肝 左侧
    # jl_gan_left = ['L-gan-1', 'L-gan-2', 'R-gan-3', 'R-gan-4', 'R-gan-5',
    #                'R-gan-6', 'R-gan-7', 'R-gan-8', 'R-gan-9', 'R-gan-10', 'R-gan-11', 'R-gan-12', 'L-gan-13',
    #                'L-gan-14', 'L-gan-15', 'L-gan-16', 'L-gan-17', 'L-gan-18']
    # # 肝 右侧
    # jl_gan_right = ['R-gan-1', 'R-gan-2', 'L-gan-3', 'L-gan-4', 'L-gan-5',
    #                 'L-gan-6', 'L-gan-7', 'L-gan-8', 'L-gan-9', 'L-gan-10', 'L-gan-11', 'L-gan-12', 'R-gan-13',
    #                 'R-gan-14', 'R-gan-15', 'R-gan-16', 'R-gan-17', 'R-gan-18']

    # ###########################################################################################################

    # 肝 左侧
    jl_gan_left = ['L-gan-1', 'L-gan-2', 'R-gan-3', 'R-gan-4', 'R-gan-5',
                   'R-gan-6', 'R-gan-7', 'R-gan-8', 'R-gan-9', 'L-gan-16']
    # 肝 右侧
    jl_gan_right = ['R-gan-1', 'R-gan-2', 'L-gan-3', 'L-gan-4', 'L-gan-5',
                    'L-gan-6', 'L-gan-7', 'L-gan-8', 'L-gan-9', 'R-gan-16']

    # 心包
    jl_xingbao = ['R-xinbao-1', 'R-xinbao-2', 'R-xinbao-3', 'R-xinbao-4', 'R-xinbao-5', 'R-xinbao-6',
                  'R-xinbao-7', 'R-xinbao-8', 'R-xinbao-9',
                  'L-xinbao-1', 'L-xinbao-2', 'L-xinbao-3', 'L-xinbao-4', 'L-xinbao-5', 'L-xinbao-6',
                  'L-xinbao-7', 'L-xinbao-8', 'L-xinbao-9']

    # 肺经
    jl_fei = ['L-fei-1', 'L-fei-2', 'L-fei-3', 'L-fei-4', 'L-fei-5', 'L-fei-6', 'L-fei-7', 'L-fei-8',
              'R-fei-1', 'R-fei-2', 'R-fei-3', 'R-fei-4', 'R-fei-5', 'R-fei-6', 'R-fei-7', 'R-fei-8']

    # 大肠
    jl_dachang = ['R-dachang-1', 'R-dachang-2', 'R-dachang-3', 'R-dachang-4', 'R-dachang-5',
                  'R-dachang-6', 'R-dachang-7', 'R-dachang-8',
                  'L-dachang-1', 'L-dachang-2', 'L-dachang-3', 'L-dachang-4', 'L-dachang-5', 'L-dachang-6',
                  'L-dachang-7', 'L-dachang-8']

    # ###########################################################################################################
    # # 脾经 左侧
    # jl_pi_left = ['R-pi-1', 'R-pi-2', 'R-pi-3', 'R-pi-4', 'R-pi-5', 'R-pi-6', 'R-pi-7',
    #               'R-pi-8', 'L-pi-9', 'L-pi-10', 'L-pi-11', 'L-pi-12', 'L-pi-13', 'L-pi-14']
    # # 脾经 右侧
    # jl_pi_right = ['L-pi-1', 'L-pi-2', 'L-pi-3', 'L-pi-4', 'L-pi-5', 'L-pi-6', 'L-pi-7',
    #                'L-pi-8', 'R-pi-9', 'R-pi-10', 'R-pi-11', 'R-pi-12', 'R-pi-13', 'R-pi-14']
    # # 脾经 中间
    # jl_pi_middle = ['L-pi-15', 'L-pi-16', 'L-pi-17', 'L-pi-18', 'L-pi-19',
    #                 'R-pi-15', 'R-pi-16', 'R-pi-17', 'R-pi-18', 'R-pi-19']
    # ###########################################################################################################
    # 脾经 左侧
    jl_pi_left = ['R-pi-1', 'R-pi-2', 'R-pi-3', 'R-pi-4', 'R-pi-5',
                  'R-pi-6', 'R-pi-7', 'R-pi-8', 'L-pi-13', 'L-pi-14']

    # 脾经 右侧
    jl_pi_right = ['L-pi-1', 'L-pi-2', 'L-pi-3', 'L-pi-4', 'L-pi-5',
                   'L-pi-6', 'L-pi-7', 'L-pi-8', 'R-pi-13', 'R-pi-14']

    # 脾经 中间
    jl_pi_middle = ['L-pi-9', 'L-pi-10', 'L-pi-11', 'L-pi-12', 'L-pi-15', 'L-pi-16', 'L-pi-17', 'L-pi-18', 'L-pi-19',
                    'R-pi-9', 'R-pi-10', 'R-pi-11', 'R-pi-12', 'R-pi-15', 'R-pi-16', 'R-pi-17', 'R-pi-18', 'R-pi-19',
                    'R-gan-10', 'R-gan-11', 'R-gan-12', 'R-gan-13', 'R-gan-14', 'R-gan-15', 'R-gan-17', 'R-gan-18',
                    'L-gan-10', 'L-gan-11', 'L-gan-12', 'L-gan-13', 'L-gan-14', 'L-gan-15', 'L-gan-17', 'L-gan-18']

    # 胃经
    jl_wei_middle = ['L-wei-15', 'L-wei-16', 'L-wei-17', 'L-wei-18', 'L-wei-19', 'L-wei-20', 'L-wei-21', 'L-wei-22', 'L-wei-23',
                     'L-wei-24', 'L-wei-25', 'L-wei-26', 'L-wei-27', 'L-wei-28', 'L-wei-29', 'L-wei-30', 'R-wei-15', 'R-wei-16', 'R-wei-17', 'R-wei-18', 'R-wei-19', 'R-wei-20', 'R-wei-21', 'R-wei-22', 'R-wei-23',
                     'R-wei-24', 'R-wei-25', 'R-wei-26', 'R-wei-27', 'R-wei-28', 'R-wei-29', 'R-wei-30']
    # jl_wei_right=['R-wei-15', 'R-wei-16','R-wei-17','R-wei-18','R-wei-19','R-wei-20', 'R-wei-21','R-wei-22','R-wei-23',
    #     'R-wei-24','R-wei-25','R-wei-26','R-wei-27','R-wei-28', 'R-wei-29','R-wei-30']

    # 心经
    jl_xin_left = ['L-xin-1', 'L-xin-2', 'L-xin-3',
                   'L-xin-4', 'L-xin-5',  'L-xin-6']
    jl_xin_right = ['R-xin-1', 'R-xin-2',
                    'R-xin-3', 'R-xin-4', 'R-xin-5', 'R-xin-6']

    # 三焦经
    jl_sanjiao = ['L-sanjiao-1', 'L-sanjiao-2', 'L-sanjiao-3', 'L-sanjiao-4', 'L-sanjiao-5',
                  'L-sanjiao-6', 'L-sanjiao-7', 'R-sanjiao-1', 'R-sanjiao-2', 'R-sanjiao-3', 'R-sanjiao-4', 'R-sanjiao-5',
                  'R-sanjiao-6', 'R-sanjiao-7']

    # 小肠
    jl_xiaochang = ['L-xiaochang-1', 'L-xiaochang-2', 'L-xiaochang-3', 'L-xiaochang-4', 'L-xiaochang-5',
                    'L-xiaochang-6', 'L-xiaochang-7', 'L-xiaochang-8', 'L-xiaochang-9', 'L-xiaochang-10',
                    'L-xiaochang-11', 'L-xiaochang-12',
                    'R-xiaochang-1', 'R-xiaochang-2', 'R-xiaochang-3', 'R-xiaochang-4', 'R-xiaochang-5',
                    'R-xiaochang-6', 'R-xiaochang-7', 'R-xiaochang-8', 'R-xiaochang-9', 'R-xiaochang-10',
                    'R-xiaochang-11', 'R-xiaochang-12']

    # 膀胱
    jl_pangguang = ['L-pangguang-9', 'L-pangguang-10', 'L-pangguang-11', 'L-pangguang-12', 'L-pangguang-13',
                    'L-pangguang-14', 'L-pangguang-15', 'L-pangguang-16', 'L-pangguang-17', 'L-pangguang-18',
                    'L-pangguang-19', 'L-pangguang-20', 'L-pangguang-21', 'L-pangguang-22', 'L-pangguang-23',
                    'L-pangguang-24', 'R-pangguang-9', 'R-pangguang-10',
                    'R-pangguang-11', 'R-pangguang-12', 'R-pangguang-13',
                    'R-pangguang-14', 'R-pangguang-15', 'R-pangguang-16', 'R-pangguang-17', 'R-pangguang-18',
                    'R-pangguang-19', 'R-pangguang-20', 'R-pangguang-21', 'R-pangguang-22', 'R-pangguang-23',
                    'R-pangguang-24']

    # 肾经-上身
    jl_shenjing_shangshen = ['R-shen-14', 'R-shen-15', 'R-shen-16', 'R-shen-17', 'R-shen-18', 'R-shen-19',
                             'L-shen-14', 'L-shen-15', 'L-shen-16', 'L-shen-17', 'L-shen-18', 'L-shen-19']

    # 肾经-下身
    jl_shenjing_xiashen = ['R-shen-1', 'R-shen-2', 'R-shen-3', 'R-shen-4', 'R-shen-5',
                           'R-shen-6', 'R-shen-7', 'R-shen-8', 'R-shen-9', 'R-shen-10', 'R-shen-11', 'R-shen-12',
                           'R-shen-13',
                           'L-shen-1', 'L-shen-2', 'L-shen-3', 'L-shen-4', 'L-shen-5',
                           'L-shen-6', 'L-shen-7', 'L-shen-8', 'L-shen-9', 'L-shen-10', 'L-shen-11', 'L-shen-12', 'L-shen-13']

    # 胆-right(之前标注中有部分人标到41，就以41为标准)
    jl_dan_right = ['R-dan-21', 'R-dan-22', 'R-dan-23', 'R-dan-24', 'R-dan-25',
                    'R-dan-26', 'R-dan-27', 'R-dan-28', 'R-dan-29', 'R-dan-30',
                    'R-dan-31', 'R-dan-34', 'R-dan-35', 'R-dan-36',
                    'R-dan-37', 'R-dan-38', 'R-dan-39', 'R-dan-40', 'R-dan-41']

    # 胆-left
    jl_dan_left = ['L-dan-21', 'L-dan-22', 'L-dan-23', 'L-dan-24', 'L-dan-25',
                   'L-dan-26', 'L-dan-27', 'L-dan-28', 'L-dan-29', 'L-dan-30',
                   'L-dan-31', 'L-dan-34', 'L-dan-35', 'L-dan-36', 'L-dan-37',
                   'L-dan-38', 'L-dan-39', 'L-dan-40', 'L-dan-41']

    # *********************************************合并经络-pointName******************************************************************

    # 经络（left-up-nei    左侧 胆经 ）
    jl_left_up_nei = jl_dan_left

    # 经络（left-up-wai    左侧 心经 肝经 脾经）
    jl_left_up_wai = jl_gan_left + jl_pi_left + jl_xin_left

    # 经络（middle-down-nei   肾经(下)）
    jl_middle_down_nei = jl_shenjing_xiashen

    # 经络（middle-down-wai   大肠  三焦  小肠   膀胱）
    jl_middle_down_wai = jl_dachang + jl_sanjiao + jl_xiaochang + jl_pangguang

    # 经络（middle-up-nei   肾经(上)  心包  肺 胃）
    jl_middle_up_nei = jl_shenjing_shangshen + jl_xingbao + jl_fei + jl_wei_middle

    # 经络（middle-up-wai   脾经）
    jl_middle_up_wai = jl_pi_middle

    # 经络（right-up-nei  right(胆经)）
    jl_right_up_nei = jl_dan_right

    # 经络（right-up-wai  right(肝经 脾经 心经)）
    jl_right_up_wai = jl_gan_right + jl_pi_right + jl_xin_right

    jl_right_down_wai = ['L-pangguang-25', 'L-pangguang-26']

    jl_left_down_wai = ['R-pangguang-25', 'R-pangguang-26']

    # 模型配置字典
    modelCfg = {
        "left_down_wai": {
            "cfg": ["left_down_wai.yaml", "left_down_wai.pth", "detectron2", "l"],
            "accuNames": jl_left_down_wai,
            "submodels": {
                "right_foot_left_down_wai": "R-pangguang-25"}
        },


        "right_down_wai": {
            "cfg": ["right_down_wai.yaml", "right_down_wai.pth", "detectron2", "r"],
            "accuNames": jl_right_down_wai,
            # "submodels": {
            #     "left_foot_right_down_wai": "L-pangguang-25"}
        },





        "left_up_nei": {
            "cfg": ["left_up_nei.yaml", "left_up_nei.pth", "detectron2", "l"],
            "accuNames": jl_left_up_nei,
            "submodels": {
                "left_foot_left_up_nei": "L-dan-40",
                "left_waist_left_up_nei": "L-dan-29"}
        },
        "left_up_wai": {
            "cfg": ["left_up_wai.yaml", "left_up_wai.pth", "detectron2", "l"],
            "accuNames": jl_left_up_wai,
            "submodels": {
                "left_hand_left_up_wai": "L-xin-5",
                "left_foot_left_up_wai": "L-gan-2",
                "right_foot_left_up_wai": "R-pi-3"}
        },
        "middle_up_nei": {
            "cfg": ["middle_up_nei.yaml", "middle_up_nei.pth", "detectron2", "m"],
            "accuNames": jl_middle_up_nei,
            "submodels": {
                "left_hand_middle_up_nei": "L-xinbao-6",
                "right_hand_middle_up_nei": "R-xinbao-6",
                "left_foot_middle_up_nei": "L-wei-28",
                "right_foot_middle_up_nei": "R-wei-28"}
        },
        "middle_up_wai": {
            "cfg": ["middle_up_wai.yaml", "middle_up_wai.pth", "detectron2", "m"],
            "accuNames": jl_middle_up_wai,
            "submodels": {}
        },
        "middle_down_nei": {
            "cfg": ["middle_down_nei.yaml", "middle_down_nei.pth", "detectron2", "m"],
            "accuNames": jl_middle_down_nei,
            "submodels": {
                "right_foot_middle_down_nei": "R-shen-2",
                "left_foot_middle_down_nei":  "L-shen-2"}
        },

        "middle_down_wai": {
            "cfg": ["middle_down_wai.yaml", "middle_down_wai.pth", "detectron2", "m"],
            "accuNames": jl_middle_down_wai,
            "submodels": {
                "left_hand_middle_down_wai": "L-dachang-2",
                "right_hand_middle_down_wai": "R-dachang-2",
                # "left_foot_middle_down_wai":"L-pangguang-25",
                # "right_foot_middle_down_wai":"R-pangguang-25",
                "middle_neck_middle_down_wai": "R-dachang-8",
                "left_shoulder_middle_down_wai": "L-dachang-7",
                "right_shoulder_middle_down_wai": "R-dachang-7", }
        },
        "right_up_nei": {
            "cfg": ["right_up_nei.yaml", "right_up_nei.pth", "detectron2", "r"],
            "accuNames": jl_right_up_nei,
            # "submodels": {
            #     "right_foot_right_up_nei": "R-dan-40",
            #     "left_waist_right_up_nei": "R-dan-29"}
        },
        "right_up_wai": {
            "cfg": ["right_up_wai.yaml", "right_up_wai.pth", "detectron2", "r"],
            "accuNames": jl_right_up_wai,
            # "submodels": {
            #     "right_hand_right_up_wai": "R-xin-5",
            #     "left_foot_right_up_wai": "L-pi-3",
            #     "right_foot_right_up_wai": "R-gan-2"}
        },




        # 新增伸直脚步局部区域


        "right_foot_left_down_wai": {
            "cfg": ["right_foot_left_down_wai.yaml", "right_foot_left_down_wai.pth", "detectron2", "l"],
            "accuNames": ["R-pangguang-25", "R-pangguang-26"],
        },



        # 新增俯卧外八 脖子，左肩膀，右肩膀  局部区域
        "middle_neck_middle_down_wai": {
            "cfg": ["middle_neck_middle_down_wai.yaml", "middle_neck_middle_down_wai.pth", "detectron2", "l"],
            "accuNames": ["L-pangguang-18", "L-pangguang-19", "R-pangguang-18", "R-pangguang-19"],
        },

        "left_shoulder_middle_down_wai": {
            "cfg": ["left_shoulder_middle_down_wai.yaml", "left_shoulder_middle_down_wai.pth", "detectron2", "l"],
            "accuNames": ["L-dachang-6", "L-dachang-7"],
        },

        "right_shoulder_middle_down_wai": {
            "cfg": ["right_shoulder_middle_down_wai.yaml", "right_shoulder_middle_down_wai.pth", "detectron2", "r"],
            "accuNames": ["R-dachang-6", "R-dachang-7"],
        },
        # 左胆  右胆   局部区域
        "left_waist_left_up_nei": {
            "cfg": ["left_waist_left_up_nei.yaml", "left_waist_left_up_nei.pth", "detectron2", "l"],
            "accuNames": ['L-dan-28', 'L-dan-29', 'L-dan-30', 'L-dan-31'],
        },

        "right_waist_right_up_nei": {
            "cfg": ["right_waist_right_up_nei.yaml", "right_waist_right_up_nei.pth", "detectron2", "r"],
            "accuNames": ['R-dan-28', 'R-dan-29', 'R-dan-30', 'R-dan-31'],
        },




        "left_foot_left_up_nei": {
            "cfg": ["left_foot_left_up_nei.yaml", "left_foot_left_up_nei.pth", "detectron2", "r"],
            "accuNames": ['L-dan-40', 'L-dan-41'],
        },
        "left_foot_middle_down_wai": {
            "cfg": ["left_foot_middle_down_wai.yaml", "left_foot_middle_down_wai.pth", "detectron2", "r"],
            "accuNames": ["L-pangguang-25", "L-pangguang-26"],
        },
        "right_foot_middle_down_wai": {
            "cfg": ["right_foot_middle_down_wai.yaml", "right_foot_middle_down_wai.pth", "detectron2", "r"],
            "accuNames": ["R-pangguang-25", "R-pangguang-26"],
        },
        "left_hand_middle_down_wai": {
            "cfg": ["left_hand_middle_down_wai.yaml", "left_hand_middle_down_wai.pth", "detectron2", "r"],
            "accuNames": ["L-dachang-1", "L-dachang-2", "L-dachang-3", "L-dachang-4", "L-xiaochang-1",
                          "L-xiaochang-2", "L-xiaochang-3", "L-sanjiao-1", "L-sanjiao-2", "L-sanjiao-3"],
        },
        "right_hand_middle_down_wai": {
            "cfg": ["right_hand_middle_down_wai.yaml", "right_hand_middle_down_wai.pth", "detectron2", "r"],
            "accuNames": ["R-dachang-1", "R-dachang-2", "R-dachang-3", "R-dachang-4", "R-xiaochang-1",
                          "R-xiaochang-2", "R-xiaochang-3", "R-sanjiao-1", "R-sanjiao-2", "R-sanjiao-3"],
        },


        "left_foot_middle_up_nei": {
            "cfg": ["left_foot_middle_up_nei.yaml", "left_foot_middle_up_nei.pth", "detectron2", "r"],
            "accuNames": ["L-wei-27", "L-wei-28", "L-wei-29", "L-wei-30"],
        },
        "right_foot_middle_up_nei": {
            "cfg": ["right_foot_middle_up_nei.yaml", "right_foot_middle_up_nei.pth", "detectron2", "r"],
            "accuNames": ["R-wei-27", "R-wei-28", "R-wei-29", "R-wei-30"],
        },
        "left_hand_middle_up_nei": {
            "cfg": ["left_hand_middle_up_nei.yaml", "left_hand_middle_up_nei.pth", "detectron2", "r"],
            "accuNames": ["L-xinbao-6", "L-xinbao-7", "L-xinbao-8", "L-fei-6", "L-fei-7", "L-fei-8"],
        },
        "right_hand_middle_up_nei": {
            "cfg": ["right_hand_middle_up_nei.yaml", "right_hand_middle_up_nei.pth", "detectron2", "r"],
            "accuNames": ["R-xinbao-6", "R-xinbao-7", "R-xinbao-8", "R-fei-6", "R-fei-7", "R-fei-8"],
        },
        "left_foot_middle_down_nei": {
            "cfg": ["left_foot_middle_down_nei.yaml", "left_foot_middle_down_nei.pth", "detectron2", "r"],
            "accuNames": ['L-shen-1', 'L-shen-2', 'L-shen-3', 'L-shen-4', 'L-shen-5', 'L-shen-6', 'L-shen-7',
                          'L-shen-8'],
        },
        "right_foot_middle_down_nei": {
            "cfg": ["right_foot_middle_down_nei.yaml", "right_foot_middle_down_nei.pth", "detectron2", "r"],
            "accuNames": ['R-shen-1', 'R-shen-2', 'R-shen-3', 'R-shen-4', 'R-shen-5', 'R-shen-6', 'R-shen-7',
                          'R-shen-8'],
        },
        "left_foot_left_up_wai": {
            "cfg": ["left_foot_left_up_wai.yaml", "left_foot_left_up_wai.pth", "detectron2", "r"],
            "accuNames": ["L-gan-1", "L-gan-2"],
        },
        "right_foot_left_up_wai": {
            "cfg": ["right_foot_left_up_wai.yaml", "right_foot_left_up_wai.pth", "detectron2", "r"],
            "accuNames": ["R-pi-1", "R-pi-2", "R-pi-3", "R-pi-4"],
        },
        "left_hand_left_up_wai": {
            "cfg": ["left_hand_left_up_wai.yaml", "left_hand_left_up_wai.pth", "detectron2", "r"],
            "accuNames": ["L-xin-4", "L-xin-5", "L-xin-6"],
        },

    }

    @classmethod
    def getModelAccuDict(self):
        modelAccuDict = {modelname: value["accuNames"]
                         for modelname, value in Models_JingluoNames.modelCfg.items()}
        return modelAccuDict

    @classmethod
    def getModel_cameraDict(self):
        modelAccuDict = {modelname: value["cfg"][3]
                         for modelname, value in Models_JingluoNames.modelCfg.items()}
        return modelAccuDict

    @classmethod
    def getModelCfg(self):
        modelAccuDict = {modelname: value["cfg"]
                         for modelname, value in Models_JingluoNames.modelCfg.items()}
        return modelAccuDict

    @classmethod
    def getModelAllCfg(self):
        return Models_JingluoNames.modelCfg

    @classmethod
    def getJingluo_AccuDictAbberv(self):
        """经络所有拐点的简写

        Returns:
            [type]: [description]
        """
        jadictAbbr = {}
        # jadictAbbr["gan"] = [(1, 18)]
        # jadictAbbr["pi"] = [(3, 14)]
        # jadictAbbr["fei"] = [(1, 8)]
        # jadictAbbr["xinbao"] = [(1, 9)]
        # jadictAbbr["dachang"] = [(1, 8)]
        # jadictAbbr["sanjiao"] = [(1, 7)]

        jadictAbbr["gan"] = ["gan", (1, 10), (12, 18)]
        jadictAbbr["pi"] = ["pi", (2, 14)]
        jadictAbbr["pis2"] = ["pi", (15, 19)]

        jadictAbbr["fei"] = ["fei", (1, 8)]
        jadictAbbr["xinbao"] = ["xinbao", (1, 9)]  # 1-9
        jadictAbbr["dachang"] = ["dachang", (4, 8)]

        # 三焦经
        jadictAbbr["sanjiao"] = ["sanjiao", (1, 7)]  # 1,7

        # 大肠
        jadictAbbr["dachang"] = ["dachang", (1, 8)]  # 1,8

        # 小肠
        jadictAbbr["xiaochang"] = ["xiaochang", (1, 11)]  # 1,12 机械臂相撞

        # 膀胱
        # jadictAbbr["pangguang"] = [(9, 24)]  #9,26 机械臂相撞
        jadictAbbr["pangguangs1"] = ["pangguang", (9, 17)]
        jadictAbbr["pangguangs2"] = ["pangguang", (19, 26)]
        jadictAbbr["dan"] = ["dan", (22, 31), (37, 41)]

        jadictAbbr["wei"] = ["wei", (15, 30)]  # 15,30
        jadictAbbr["xin"] = ["xin", (1, 6)]
        jadictAbbr["shen_tiqian"] = ["shen", (14, 19)]
        jadictAbbr["shen_tihou"] = ["shen", (1, 13)]  # 1,13(13,pengzhuang?)
        return jadictAbbr

    @classmethod
    def getJingluoName_NameDict(self, jingluoName: str) -> dict:
        splits = jingluoName.split("-")
        lr = splits[1]
        stemName = splits[0]
        upperlr = lr.lower()
        # jingluoname = stemName+"_"+lowerlr
        accuSuffix = upperlr + "-" + stemName
        betweens = g_jadictAbbr[jingluoName]
        namedict = {accuSuffix: betweens}
        return namedict

    @classmethod
    def getJingluo_AccuDict(self):
        """
        经络名->所有拐点名
        """
        jadictAbbrs = Models_JingluoNames.getJingluo_AccuDictAbberv()
        JingluoDict = {}
        for jlname, betweens in jadictAbbrs.items():
            for lr in ["L",  "R"]:
                lowerlr = lr.lower()
                abbr = betweens[0]
                jingluoname = jlname + "_"+lowerlr
                accuSuffix = lr + "-" + abbr
                namedict = {accuSuffix: betweens[1:len(betweens)]}
                AllJingluoNames, JingluoNames, skeleton, skelecolor, kptcolor, name2index, = buildKeypointNames(
                    namedict)
                JingluoDict[jingluoname] = AllJingluoNames
        return JingluoDict

    @classmethod
    def getJingluo_modelDict(self):
        """经络名->所需要用的识别模型名
21,31),(34,41
        Returns:
            [type]: [description]
        """
        jingluo_modelDict = {}
        jingluo_modelDict["gan_l"] = [
            "left_up_wai", "right_up_wai", "middle_up_wai"]
        jingluo_modelDict["gan_r"] = [
            "left_up_wai", "right_up_wai", "middle_up_wai"]
        jingluo_modelDict["xinbao_l"] = ["middle_up_nei"]
        jingluo_modelDict["xinbao_r"] = ["middle_up_nei"]
        jingluo_modelDict["fei_l"] = ["middle_up_nei"]
        jingluo_modelDict["fei_r"] = ["middle_up_nei"]
        jingluo_modelDict["dachang_l"] = ["middle_down_wai"]
        jingluo_modelDict["dachang_r"] = ["middle_down_wai"]

        # 脾经有一部分点放在middle模型上
        jingluo_modelDict["pi_l"] = [
            "left_up_wai", "right_up_wai", "middle_up_wai"]
        jingluo_modelDict["pi_r"] = [
            "left_up_wai", "right_up_wai", "middle_up_wai"]
        jingluo_modelDict["pis2_l"] = ["middle_up_wai"]
        jingluo_modelDict["pis2_r"] = ["middle_up_wai"]

        # 三焦经
        jingluo_modelDict["sanjiao_l"] = ["middle_down_wai"]
        jingluo_modelDict["sanjiao_r"] = ["middle_down_wai"]

        # dachang
        jingluo_modelDict["xiaochang_l"] = ["middle_down_wai"]
        jingluo_modelDict["xiaochang_r"] = ["middle_down_wai"]

        # pangguang
        # jingluo_modelDict["pangguang_l"]=["middle_pangguang"]
        # jingluo_modelDict["pangguang_r"]=["middle_pangguang"]

        jingluo_modelDict["pangguangs1_l"] = ["middle_down_wai"]
        jingluo_modelDict["pangguangs1_r"] = ["middle_down_wai"]

        # jingluo_modelDict["pangguangs1_r"]=["middle_down_wai"]
        # jingluo_modelDict["pangguangs1_r"]=["middle_down_wai"]

        jingluo_modelDict["pangguangs2_l"] = [
            "right_down_wai", "middle_down_wai"]
        jingluo_modelDict["pangguangs2_r"] = [
            "left_down_wai", "middle_down_wai"]

        jingluo_modelDict["dan_r"] = ["right_up_nei"]
        jingluo_modelDict["dan_l"] = ["left_up_nei"]
        jingluo_modelDict["wei_l"] = ["middle_up_nei"]
        jingluo_modelDict["wei_r"] = ["middle_up_nei"]
        jingluo_modelDict["shen_tiqian_l"] = ["middle_up_nei"]
        jingluo_modelDict["shen_tiqian_r"] = ["middle_up_nei"]

        # shen-xia
        jingluo_modelDict["shen_tihou_l"] = ["middle_down_nei"]
        jingluo_modelDict["shen_tihou_r"] = ["middle_down_nei"]

        jingluo_modelDict["xin_l"] = ["left_up_wai"]
        jingluo_modelDict["xin_r"] = ["right_up_wai"]

        return jingluo_modelDict

    @classmethod
    def getCameraJingluoNames(self, jingluoNames: list) -> list:
        cameraJLs = {}
        for cameraName in 'rlhm':
            cameraJLs[cameraName] = []
        for jingluo in jingluoNames:
            jingluo_models = g_jingluo_modelDict[jingluo]
            for model in jingluo_models:
                camera = g_Model_cameraDict[model]
                if not jingluo in cameraJLs[camera]:
                    cameraJLs[camera].append(jingluo)

        return cameraJLs

    @classmethod
    def judge_flip(self, modelName):
        flipModelList = ["right_up_wai", "right_up_nei", "right_down_wai"]
        if modelName in flipModelList:
            new_modelName = modelName.replace("right", "left")
            return "r", new_modelName
        else:
            return None, None

    @classmethod
    def getCameraModelNames(self, cameraOrder, jingluoNames: list) -> list:
        """given jingluo names

        Args:
            jingluoNames (list): [description]

        Returns:
            list: [list of models of every camera]
        """
        cameraModelNames = {}
        for cameraName in cameraOrder:
            cameraModelNames[cameraName] = []

        for jingluo in jingluoNames:
            if jingluo.lower() == "none":
                continue
            jingluo_models = g_jingluo_modelDict[jingluo]
            for modelName in jingluo_models:
                camera, new_modelName = self.judge_flip(modelName)
                if camera == "r":
                    modelName = new_modelName
                else:
                    camera = g_Model_cameraDict[modelName]

                if not modelName in cameraModelNames[camera]:
                    cameraModelNames[camera].append(modelName)

        return cameraModelNames


g_jingluoDict = Models_JingluoNames.getJingluo_AccuDict()
g_modelAccu = Models_JingluoNames.getModelAccuDict()
g_Model_cameraDict = Models_JingluoNames.getModel_cameraDict()
g_jingluo_modelDict = Models_JingluoNames.getJingluo_modelDict()
g_modelCfg = Models_JingluoNames.getModelCfg()
g_jadictAbbr = Models_JingluoNames.getJingluo_AccuDictAbberv()


def test_modelConfigCompleteNess():
    jingluo_modelDict_Values = g_jingluo_modelDict.values()
    jingluo_modelDict_keys = g_jingluo_modelDict.keys()
    jlModels = [item for sublist in jingluo_modelDict_Values for item in sublist]
    jlmodelsSet = set(jlModels)

    with open("therapys.json", 'r') as f:
        therapyMap = json.load(f)
        textname = "疗法一"
        postrues = therapyMap[textname].keys()
        poseture_jingluonamesDict = therapyMap[textname]

        jlnames = [jlname for pose, jingluoNames in poseture_jingluonamesDict.items(
        ) for jlname in jingluoNames.split(",") if jlname != 'All']
        for jlname in jlnames:
            assert jlname in jingluo_modelDict_keys
            subJlname = jlname[:-2]
            assert subJlname in g_jingluoNames

    for key, value in g_modelAccu.items():
        assert key in g_Model_cameraDict
        assert key in g_modelCfg
        assert key in jlmodelsSet

    for key, values in g_jingluo_modelDict.items():
        for value in values:
            assert value in g_modelAccu


def test_getJingluo_AccuDict():
    jingluoDict = Models_JingluoNames.getJingluo_AccuDict()
    print("jingluoDict", jingluoDict)
    print("\n")
    modelAccu = Models_JingluoNames.getModelAccuDict()
    print("modelAccu", modelAccu)
    print("\n")
    getJingluo_modelDict = Models_JingluoNames.getJingluo_modelDict()
    print("getJingluo_modelDict", getJingluo_modelDict)
    print("\n")
    getModel_cameraDict = Models_JingluoNames.getModel_cameraDict()
    print("getModel_cameraDict", getModel_cameraDict)
    pass


def test_getCameraModels():
    cameraOrder = 'rhlm'
    pi_lcameras = Models_JingluoNames.getCameraModelNames(cameraOrder, [
                                                          "pi_l"])
    print("pi_lcameras:", pi_lcameras)

    xinbaol_lcameras = Models_JingluoNames.getCameraModelNames(cameraOrder, [
                                                               "xinbao_l"])
    print("xinbaol_lcameras:", xinbaol_lcameras)
    cameraJingluoNames = Models_JingluoNames.getCameraJingluoNames(
        ["xinbao_l", "pi_l"])
    print("cameraJingluoNames:", cameraJingluoNames)


if __name__ == "__main__":
    # test_modelConfigCompleteNess()
    # test_getCameraModels()
    test_getJingluo_AccuDict()
