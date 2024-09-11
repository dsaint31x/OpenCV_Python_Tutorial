import numpy as np
import cv2 
import sys

def get_vc_prop(vc):
    """
    중요하지 않은 video camera관련 정보 출력 메서드

    parameters:
    - vc: VideoCapture Object

    return value:
    - None
    """
    b = vc.get(cv2.CAP_PROP_BRIGHTNESS) # brightness
    c = vc.get(cv2.CAP_PROP_CONTRAST)   # contrast
    s = vc.get(cv2.CAP_PROP_SATURATION) # saturation
    h = vc.get(cv2.CAP_PROP_HUE)        # hue
    print(f'{b = } ; {c = } ; {s = } ; {h = }')


def main(file_str,api_backend = cv2.CAP_ANY):
    cv2.namedWindow('Video from File', 
                    # cv2.WINDOW_GUI_NORMAL,
                    cv2.WINDOW_GUI_EXPANDED,
                    )
    vc = cv2.VideoCapture(file_str) 
    if not vc.isOpened():
        sys.exit(f'ERROR: Can\'t opne file: {file_str}')

    frame_w = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_h = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = vc.get(cv2.CAP_PROP_FPS)
    fourcc = int(vc.get(cv2.CAP_PROP_FOURCC)) # codec info. 4character
    
    fourcc_str = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])
    print(f"Camera resolution: {frame_w}x{frame_h}")
    print(f"FPS: {fps}")
    print(f"Codec: {fourcc_str}")
    get_vc_prop(vc)
        
    t = np.round(1000./fps).astype(int)

    while True:
        is_ok, frame = vc.read()
        
        if not is_ok:
            print('Can\'t acquire video frame!')
            break
        
        cv2.imshow('Video from Webcam', frame)
        
        key = cv2.waitKey(t)
        if key & 0xff == ord('q'):
            break
        elif key & 0xff == 27: #esc
            break
    
    cv2.destroyAllWindows()
    vc.release()

if __name__ == "__main__":
    file_str = 'vtest.avi'

    main(file_str)

