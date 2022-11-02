import cv2
import numpy as np
import logging
g_palette = np.array([[0, 128, 0], [230, 230, 0], [255, 0, 255],
                        [0, 102, 0], [0, 51, 0], [102, 178, 0],
                        [51, 153, 0], [0, 153, 153], [0, 102, 102],
                        [0, 51, 51], [153, 0, 153], [102, 0, 102],
                        [51, 255, 51], [0, 255, 0], [0, 0, 255]])
g_jingluoNames = ["shen_tiqian","shen_tihou","xinbao", "sanjiao", "dan", "gan", "fei", "dachang", "wei","pi", "pis2","xin", "xiaochang", "pis2","pangguangs1", "pangguangs2", "pangguang", "shen"]                        
def findFlipPair(accName, accNames):
    pass
def buildNextLabel( label):
    '''
    return:
    labelNext:"L-dan-41"
    labelsus[1]:"dan"
    lastNumber:40
    '''
    #label:"L-dan-40"
    assert len(label) > 0
    labelsus = label.split('-')
    
    if len(labelsus) != 3 or not labelsus[2].isnumeric():
        return None, None

    lastNumber = int(labelsus[2])
    labelNext = labelsus[0]+'-'+labelsus[1] +'-'+ str(lastNumber + 1)
    return labelNext, labelsus[1], lastNumber
def skeletonFromAccunames(accunames:list, startIndex = 0):
    '''
    return:
    skeleton :[[0,1]]
    skelecolor:[4]
    kptcolor:[4,4]
    name2index:{'L-dan-40':0,'L-dan-41':1}
    '''
    # jlcolorindex = g_jingluoNames.index(jingluoName)
    cnt = 1
    name2index = {}
    skeleton = []
    skelecolor, kptcolor = [], []
    FlipPairs = [] 
    for i, jlname in enumerate(accunames):

        # lr, stem, noStr = jlname.split("-")
        # no = int(noStr)
        # if i == 0:
        #     lastlr,lastStem, lastNo =  lr, stem, no
        # else:
        #     if no == lastNo + 1 and lastlr == lr and lastStem == stem:
        #         skeleton.append([cnt - 1, cnt])
        #         skelecolor.append(jlindex)
        nextLabel, stemName, No = buildNextLabel(jlname)
        curLabelIndex = accunames.index(jlname)
        jlcolorindex = g_jingluoNames.index(stemName)
        assert i == curLabelIndex
        if nextLabel in accunames:
            
            
            nextLabelIndex = accunames.index(nextLabel)
            skeleton.append([i + startIndex,  nextLabelIndex + startIndex])
            skelecolor.append(jlcolorindex)            

        kptcolor.append(jlcolorindex)
        name2index[jlname] = cnt -1
        # lastlr,lastStem, lastNo =  lr, stem, no

        cnt += 1
    return skeleton, skelecolor, kptcolor, name2index
def buildKeypointNames(namedict):
    # namedict = {"shen":19,"xinbao":9, "sanjiao":25, "dan":42, "gan":28, "fei":8, "dachang":14, "wei":30,"pi":19, "xin":6, "xiaochang":24, "pangguang":26}  
    # namedict = {"L-wei":(15, 30)}  
    Jingluodict ={}
     
    FlipPairs = []  
    skeletonDict= {}
    
    skelecolorDict, kptcolorDict, colorindexDict = {}, {}, {}
    name2index = {}
    allNames = []
    cnt = 1
    # /names = []
    skeleton = []
    skelecolor, kptcolor = [], []
    colorindex = []
    for nameindex, (jlname, num) in enumerate(namedict.items()):
        oneJingluo = []
        for between in  num:
            for i, no in enumerate(range(between[0],between[1] + 1)):
                accupointName = jlname + "-" + str(no)
                oneJingluo.append(accupointName)
                # FlipPairs.append([cnt, cnt + 1])
                allNames.append(accupointName)
                if no < between[1]:
                    skeleton.append([cnt, cnt + 1])
                    skelecolor.append(nameindex)
                kptcolor.append(nameindex + 1)
                name2index[accupointName] = cnt -1
                cnt += 1

        # __makeFlipPairs(FlipPairs, jlname, names, name2index)
        Jingluodict[jlname] = oneJingluo
        skelecolorDict[jlname] = skelecolor
        kptcolorDict[jlname] = kptcolor
        colorindexDict[jlname] = colorindex
        skeletonDict[jlname] = skeleton
    # print("total accupoints:" , len(names))
    assert len(skeleton) == len(skelecolor)
    return allNames, Jingluodict, skeleton, skelecolor, kptcolor, name2index
def __makeFlipPairs(FlipPairs, jlname, names, name2index):
    for i, lrname in enumerate(zip(names[0],names[1])):
        accupointNamel = lrname[0]
        accupointNamer = lrname[1]
        indexl = [name2index[accupointNamel]]
        indexr = [name2index[accupointNamer]]
        FlipPairs.append([indexl, indexr])

def drawBox(image, box):
    x0 = int(box[0])
    y0 = int(box[1])
    x1 = int(0 + box[2])
    y1 = int(0 + box[3])

    cv2.rectangle(image,(x0, y0), (x1, y1), (255, 255, 0), 1)
def drawKeypoints(image, keypoints, KeypointNames, box = None, color = None):   
    '''points 和 names 的长度一样，，在图片上画线 put txt'''
    if keypoints is None:
        logging.warning("keypoints is None")
        return
    #
    skeletonIndex, skelecolorIndex, kptcolorIndex, name2index = skeletonFromAccunames(KeypointNames)
    if color:
        kptcolor = color
        txtcolor = color
    else:
        kptcolor = (0, 0, 255)
        txtcolor = (255, 0, 0)
    for i , keypoint, in enumerate(keypoints):
        
        cv2.circle(image, (int(keypoints[i][0]), int(keypoints[i][1])), 3, kptcolor)
        confidenceStr = str(int(keypoints[i][2] * 100))
        # cv2.putText(image, confidenceStr, (int(keypoints[i][0]), int(keypoints[i][1])),1, 0.6, )
        if not KeypointNames is None:
            cv2.putText(image, KeypointNames[i], (int(keypoints[i][0]), int(keypoints[i][1])),1, 0.6, txtcolor)
    for i, askel in enumerate(skeletonIndex):
        if color :
            skelcolor = color
        else:
            skelcolor = g_palette[skelecolorIndex[i] % 15].tolist()
        x0 = int(keypoints[askel[0] ][0])
        pt0 = (x0, int(keypoints[askel[0]][1] ))
        x1 = int(keypoints[askel[1]][0])
        pt1 = (x1, int(keypoints[askel[1]][1]))
        if x0 == 0 or x1 == 0: 
            continue
        cv2.line(image, pt0, pt1, skelcolor,2)
    if not box is None:
        drawBox(image, box)

def KpDrawPoint(image, keypoints, KeypointNames, box = None):   
    '''points 和 names 的长度一样，，在图片上画线 put txt'''
    if keypoints is None:
        logging.warning("keypoints is None")
        return
    #
    skeletonIndex, skelecolorIndex, kptcolorIndex, name2index = skeletonFromAccunames(KeypointNames)
    for i , keypoint, in enumerate(keypoints):
        if i %10 == 0:
            # i = i/10
            kptcolor = (0, 0, 255)
            cv2.circle(image, (int(keypoints[i][0]), int(keypoints[i][1])), 3, kptcolor)
            confidenceStr = str(int(keypoints[i][2] * 100))
            cv2.putText(image, confidenceStr, (int(keypoints[i][0]), int(keypoints[i][1])),1, 0.6, (255, 0, 0))
            # if not KeypointNames is None:
            #     cv2.putText(image, KeypointNames[i], (int(keypoints[i][0]), int(keypoints[i][1])),1, 0.4, (255, 0, 0))
    for i, askel in enumerate(skeletonIndex):
        skelcolor = g_palette[skelecolorIndex[i] % 15]
        askel = [num*10 for num in askel]
        x0 = int(keypoints[askel[0] ][0])
        pt0 = (x0, int(keypoints[askel[0]][1] ))
        x1 = int(keypoints[askel[1]][0])
        pt1 = (x1, int(keypoints[askel[1]][1]))
        if x0 == 0 or x1 == 0: 
            continue
        cv2.line(image, pt0, pt1, skelcolor.tolist(),2)
    if not box is None:
        drawBox(image, box)

if __name__ == "__main__":
    # namedict = {"L-wei":(15, 30), "R-wei":(15, 30)}
    jl_gan_left = ['L-gan-1','L-gan-2', 'R-gan-3','R-gan-4','R-gan-5',
    'R-gan-6','R-gan-7','R-gan-8','R-gan-9','R-gan-10','R-gan-11','R-gan-12','L-gan-13',
    'L-gan-14','L-gan-15','L-gan-16','L-gan-17','L-gan-18']

    jl_xingbao = ['R-xinbao-1','R-xinbao-2', 'R-xinbao-3','R-xinbao-4','R-xinbao-5','R-xinbao-6',
    'R-xinbao-7','R-xinbao-8','R-xinbao-9',
    'L-xinbao-1','L-xinbao-2','L-xinbao-3','L-xinbao-4','L-xinbao-5','L-xinbao-6',
    'L-xinbao-7','L-xinbao-8','L-xinbao-9']

    jl_fei = ['L-fei-1','L-fei-2', 'L-fei-3','L-fei-4','L-fei-5','L-fei-6','L-fei-7','L-fei-8',
        'R-fei-1','R-fei-2','R-fei-3','R-fei-4','R-fei-5','R-fei-6','R-fei-7','R-fei-8']

    jl_dachang = ['R-dachang-1','R-dachang-2', 'R-dachang-3','R-dachang-4','R-dachang-5',
    'R-dachang-6','R-dachang-7','R-dachang-8',
        'L-dachang-1','L-dachang-2','L-dachang-3','L-dachang-4','L-dachang-5','L-dachang-6',
        'L-dachang-7','L-dachang-8']
    
    #脾经
    jl_pi_left = ['R-pi-1','R-pi-2', 'R-pi-3','R-pi-4','R-pi-5',
    'R-pi-6','R-pi-7','R-pi-8','R-pi-9',
    'L-pi-9','L-pi-10','L-pi-11','L-pi-12','L-pi-13','L-pi-14']

    jl_pi_right = ['L-pi-1','L-pi-2', 'L-pi-3','L-pi-4','L-pi-5',
    'L-pi-6','L-pi-7','L-pi-8','L-pi-9',
    'R-pi-9','R-pi-10','R-pi-11','R-pi-12','R-pi-13','R-pi-14']

    jl_pi_middle = ['L-pi-15','L-pi-16', 'L-pi-17','L-pi-18','L-pi-19',
                    'R-pi-15','R-pi-16','R-pi-17','R-pi-18','R-pi-19']
    skeleton, skelecolor, kptcolor, name2index = skeletonFromAccunames(jl_fei, 'wei')
    namedict = {"L-gan":[(1,2),(13,18)],"R-gan":[(3,12)]}
    namedict = {"L-fei":[(1,8)], "R-fei":[(1,8)]}
    AllKpNames, Jingluodict, skeleton, skelecolor, kptcolor, name2index = buildKeypointNames(namedict)
    pass