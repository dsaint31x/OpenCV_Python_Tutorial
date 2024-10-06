import cv2
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS

TAGS_RESERVED = {v:k for k,v in TAGS.items()}
EXPOSURE_TIME_TAG = TAGS_RESERVED.get('ExposureTime')

def get_exposure_time(img_path):
    with Image.open(img_path) as img:
        exif_data = img._getexif()
        exposure = exif_data.get(EXPOSURE_TIME_TAG,-1.)
    return exposure

def main():
    img_names = ['33','100','179','892','1560','2933']
    exposures = []
    imgs = []
    for img in img_names:
        img_path = f'./{img}.jpg'
        exposure = get_exposure_time(img_path)
        if exposure > 0:
            exposures.append(exposure)
            imgs.append(cv2.imread(img_path, cv2.IMREAD_COLOR))
    exposures = np.array(exposures).astype(np.float32)

    calibrate = cv2.createCalibrateDebevec()
    response = calibrate.process(imgs, exposures)

    merge_debevec = cv2.createMergeDebevec()
    hdr_img = merge_debevec.process(imgs, exposures, response)
    print(np.max(hdr_img), np.min(hdr_img),hdr_img.dtype)
    
    
    tmp = cv2.normalize(hdr_img, None, 0, 1, cv2.NORM_MINMAX)

    # tonemap = cv2.createTonemapDurand(gamma=2.2)
    tonemap = cv2.createTonemapReinhard(gamma=2.2)
    ldr_img = tonemap.process(hdr_img)
    ldr_img = cv2.normalize(ldr_img, None, 0, 1, cv2.NORM_MINMAX)

    cv2.namedWindow('hdr_img w/ tonemap',cv2.WINDOW_NORMAL)
    cv2.imshow('hdr_img w/ tonemap', ldr_img)
    cv2.resizeWindow('hdr_img w/ tonemap', 400,300)
    cv2.namedWindow('hdr_img w/o tonemap',cv2.WINDOW_NORMAL)
    cv2.imshow('hdr_img w/o tonemap', tmp)
    cv2.resizeWindow('hdr_img w/o tonemap', 400,300)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
        
