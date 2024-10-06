import cv2
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt
from scipy import optimize

TAGS_RESERVED = {v:k for k,v in TAGS.items()}
EXPOSURE_TIME_TAG = TAGS_RESERVED.get('ExposureTime')

def get_exposure_time(img_path):
    with Image.open(img_path) as img:
        exif_data = img._getexif()
        exposure = exif_data.get(EXPOSURE_TIME_TAG,-1.)
    return exposure

def gamma_function(x, gamma, scale):
    return scale* (x)**gamma

def plot_crf(crf):
    colors = ['b','g', 'r']
    labels = ['blue','green', 'red']
    gammas = []
    scales = []

    # print(crf.shape)
    tmp = np.squeeze(crf)
    # print(tmp.shape)
    crf = np.transpose(tmp,(1,0))
    # print(crf.shape)


    plt.figure(figsize=(10,6))
    for i in range(3):
        plt.plot(
                 crf[i],
                 range(256), 
                 color=colors[i],
                 label=labels[i],
                 )

        max_b = np.max(crf)
        norm_crf = crf/max_b
        popt, _ = optimize.curve_fit(gamma_function, 
                                     norm_crf[i],
                                     np.linspace(0,255,256), 
                                     )
        gamma, scale = popt
        gammas.append(gamma)
        scales.append(scale)

    m_gamma = np.array(gammas).mean()
    m_scale = np.array(scales).mean()
    print(m_gamma, m_scale)
    plt.plot(crf[0],
             gamma_function(norm_crf[i], m_gamma, m_scale), 
             '--', 
             label='fitted gamma',
             )

    plt.ylabel('pixel value')
    plt.xlabel('relative luminance')
    plt.title('camera response funciton')
    plt.legend()
    plt.grid(True)
    plt.show()

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
    plot_crf(response)


if __name__ == "__main__":
    main()
        
