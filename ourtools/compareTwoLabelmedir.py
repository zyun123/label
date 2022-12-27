import glob
import os
import json
# import cv2
import numpy as np
class Comp2dir:
    def __init__(self,dir1, dir2,outdir, kpnames):
        self.dirs = [dir1,dir2]
        self.outdir = outdir
        self.kpnames = kpnames
    def getImagePath(self,jsonpath:str):
        imgpath = jsonpath.replace('json', 'jpg')
        return imgpath
    def compareImg(self,path, name, path1,name1, outdir, kpnames):
        img =None
        imgpath = self.getImagePath(path)
        imgname = self.getImagePath(name)
        img = cv2.imread(imgpath)

        points = self.getPoints(path)
        points1 = self.getPoints(path1)

        #drawimgs
        self.drawPoints(img, points, (255, 0, 0))
        self.drawPoints(img, points1, (0, 255, 0))

        #calc distance of each keypoint of dir1 with dir2
        x = np.array(points)[:,0]
        x1 = np.array(points1)[:,0]
        dx = x - x1
        y = np.array(points)[:,1]
        y1 = np.array(points1)[:,1]
        dy = y - y1    
        v = np.array(points)[:,2]
        v1 = np.array(points1)[:,2]
        dv = v*v1   > 0
        l1 = np.sqrt(dx**2 + dy**2)

        self.drawDistance(img, points1, l1, (0, 0, 255))
        outpath = os.path.join(outdir,imgname)
        cv2.imwrite(outpath, img)
        cv2.imshow("img", img)
        cv2.waitKey(0)        
        return [l1,abs(dx), abs(dy)]

    def compare(self):
        paths, names = self.getfilePaths_names()
        results = [None,None,None]
        means = [None,None,None]
        mean = [None,None,None]
        #evaluate
        for index0, (path, name) in enumerate(zip(paths[0], names[0])):
            assert names[0][index0] == name
            index1 = names[1].index(name)
            name1 = names[1][index1]
            path1 = paths[1][index1]
            resultImg = self.compareImg(path, name, path1,name1,self.outdir, self.kpnames)
            
            for i in range(3):
                if results[i] is not None:
                    results[i] = np.vstack( (results[i], resultImg[i]))
                else:
                    results = resultImg

        #accumulate
        for i in range(3):
            means[i] = np.mean(results[i], axis= 0)
            mean[i] = np.mean(results[i])
            #summarize
            print("{} mean: {}".format(i, mean[i]) )
            for index, name in enumerate(self.kpnames):
                print(name, ":", means[i][index])
        pass
    def getfilePaths_names(self):
        names=[]
        paths = []
        for dir in self.dirs:
            jsonfiles1 = glob.glob(os.path.join(dir,'*.json'))
            paths.append(jsonfiles1)
            stemFile = [os.path.basename(path) for path in jsonfiles1]
            names.append(stemFile)
        return paths, names
    def getPoints(self, path):  
        testjson = json.load(open(path))
        shapes = testjson['shapes']
        keypoints = []
        for kpname in self.kpnames:
            found = False
            for shape in shapes:
                if shape["label"] == kpname:
                    points = shape["points"]
                    x = (points[0][0] +.0)
                    y = (points[0][1] +.0)       
                    keypoints.append([x, y, 2])
                    found = True
            if not found:
                keypoints.append([0, 0, 0])
        assert len(keypoints) == len(self.kpnames)
        return keypoints
    def drawPoints(self, img, Points, color:tuple):
        for point in Points:
            x = int(point[0] +0.5)
            y = int(point[1] +0.5)
            cv2.circle(img, (x, y), 2, color)  
    def drawDistance(self, img, points1, l1, color:tuple):
        for index, point in enumerate(points1):
            x = int(point[0] +0.5)
            y = int(point[1] +0.5)
            cv2.putText(img, str(int(l1[index])), (x, y), 1, 1, color)  

def main():
    dir1 = "/home/sy/working/evaluations/Label/_time1/wai"
    dir2 = "/home/sy/working/evaluations/Label/_time2/wai"
    outdir = "/home/sy/working/evaluations/Label/wairesult"
    kpnames = ["gan-1", "gan-2", "gan-3", "gan-4", "gan-5", "gan-6", "gan-7", "gan-8", "gan-9", "gan-10", "gan-11", "gan-12", "gan-13", "gan-14", "gan-15"]
    objcomdir = Comp2dir(dir1,dir2, outdir, kpnames)
    objcomdir.compare()


if __name__ == "__main__":
    main()