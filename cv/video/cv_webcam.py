import cv2
import sys, os
import contextlib


def find_available_devices(max_devices=3):
    available_devices = []
    
    # cv2.utils.logging.setLogLevel(cv2.utils.logging.LOG_LEVEL_SILENT)
    cv2.setLogLevel(0)
    for device_id in range(max_devices):
        cap = cv2.VideoCapture(device_id)
        print('----------------')
        if cap.isOpened():  # 장치가 열렸다면, 사용 가능
            available_devices.append(device_id)
            cap.release()  # 장치를 닫아줍니다.
    
    # cv2.utils.logging.setLogLevel(cv2.utils.logging.LOG_LEVEL_ERROR)
    cv2.setLogLevel(3)

    return available_devices

def check_available_backends(cam_id):
    """
    사용 가능한 API 백엔드를 확인하는 함수
    
    parameters:
    - None

    return value:
    - available_backends: list
    """
    backends = {
        "CAP_V4L2": cv2.CAP_V4L2,
        "CAP_DSHOW": cv2.CAP_DSHOW,
        "CAP_MSMF": cv2.CAP_MSMF,
        "CAP_AVFOUNDATION": cv2.CAP_AVFOUNDATION,
        "CAP_FFMPEG": cv2.CAP_FFMPEG
    }

    available_backends = []

    for name, api in backends.items():
        cap = cv2.VideoCapture(cam_id, api)  # 0번 카메라로 시도
        if cap.isOpened():
            available_backends.append(name)
            cap.release()

    return available_backends

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


def main(cam_id,api_backend=cv2.CAP_ANY,save=False):
    cv2.namedWindow('Video from Webcam', 
                    # cv2.WINDOW_GUI_NORMAL,
                    cv2.WINDOW_GUI_EXPANDED,
                    )
    vc = cv2.VideoCapture(cam_id) #, cv2.CAP_DSHOW)
    if not vc.isOpened():
        sys.exit(f'ERROR: Can\'t connect camera: {cam_id}')

    frame_w = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_h = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = vc.get(cv2.CAP_PROP_FPS)
    fourcc = int(vc.get(cv2.CAP_PROP_FOURCC)) # codec info. 4character
    
    fourcc_str = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])
    print(f"Camera resolution: {frame_w}x{frame_h}")
    print(f"FPS: {fps}")
    print(f"Codec: {fourcc_str}")
    get_vc_prop(vc)

    if save:
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_w, frame_h))
        
    while True:
        is_ok, frame = vc.read()
        
        if not is_ok:
            print('Can\'t acquire video frame!')
            break
        
        cv2.imshow('Video from Webcam', frame)
        if save: out.write(frame)
        
        key = cv2.waitKey(10)
        if key & 0xff == ord('q'):
            break
        elif key & 0xff == 27: #esc
            break
    
    cv2.destroyAllWindows()
    vc.release()
    out.release()

if __name__ == "__main__":
    available_devices = find_available_devices()
    print("Available devices:", available_devices)
    
    if len(available_devices) >0 :
        # 확인된 사용 가능한 백엔드 출력
        available_apis = check_available_backends(available_devices[0])
        print("Available Video Capture APIs:", available_apis)

        if len(available_apis) > 0:
            main(available_devices[0],
                 available_apis[0],
                 True,
                 )
        else:
            print('There is not an available api backend!')
    else:
        print('There is not an available camera!')
