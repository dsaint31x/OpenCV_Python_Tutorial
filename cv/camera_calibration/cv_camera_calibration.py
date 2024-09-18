import numpy as np
import cv2 as cv
import glob

import os

def calb(img_path, viz=False):
 
    # termination criteria
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6*7,3), np.float32)
    objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) # 2x7x6 matrix를 transpose후 6x7x2. 
    
    print(f'{objp.shape = }') # num of corners , (x,y)
    
    # Arrays to store object points and image points from all the images.
    obj_pnts = [] # 3d point in real world space
    img_pnts = [] # 2d points in image plane.
    
    img_str = f'{img_path}/*.jpg'
    
    images = glob.glob(img_str)
    
    for idx,fname in enumerate(images):
        img = cv.imread(fname)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if idx == 0:
            h,w = gray.shape[::-1] 
    
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    
        # If found, add object points, image points (after refining them)
        if ret == True:
            obj_pnts.append(objp)
    
            corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            img_pnts.append(corners2)
    
            # Draw and display the corners
            if viz:
                cv.drawChessboardCorners(img, (7,6), corners2, ret)
                cv.imshow('img', img)
                cv.waitKey(500)
    
    if viz:
        cv.destroyAllWindows()
        print(f'{len(img_pnts) = }')     # num of images    
        print(f'{obj_pnts[0].shape = }') # cols=7 , rows=6, 42 pnts 
        print(f'{img_pnts[0].shape = }')
        
    return obj_pnts, img_pnts, (w,h) 
    
if __name__ == "__main__":
    print(f'{os.path.dirname(__file__)}')
    
    wd = os.path.dirname(__file__)
    img_path = os.path.join(wd,'img')
    obj_pnts, img_pnts, (w,h) = calb(img_path,True)
    
    ret, k, dist, r, t = cv.calibrateCamera(obj_pnts, 
                                            img_pnts, 
                                            (w,h),
                                            None,
                                            None,
                                            )
    print(f'{ret = }')
    print(f'{k.shape = }')
    print(f'{dist.shape = }') # distortion coef. k1, k2, p1, p2, k3
    print(f'{np.array(r).shape = }') # tuple
    print(f'{np.array(t).shape = }') # tuple
    print(k)
    
    
    R, _ = cv.Rodrigues(r[0])
    T = t[0]
    RT = np.hstack((R,T))
    proj_matrix = np.dot(k,RT)
    # 투영 행렬 분해
    cameraMatrix, rotMatrix, transVect, rotMatrixX, rotMatrixY, rotMatrixZ, eulerAngles = \
        cv.decomposeProjectionMatrix(proj_matrix)

    # 결과 출력
    print("Camera Matrix:\n", cameraMatrix)
    print("Rotation Matrix:\n", rotMatrix)
    print("Translation Vector:\n", transVect)
    print("Euler Angles:\n", eulerAngles)
