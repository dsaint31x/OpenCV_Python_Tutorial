import numpy as np
import cv2 as cv

def create_chessboard(corners_cols, corners_rows, tile_size=50):
    """
    체스보드 이미지를 생성하는 함수입니다.
    :param corners_cols: 체스보드의 열 방향 코너 수
    :param corners_rows: 체스보드의 행 방향 코너 수
    :param tile_size: 각 타일(셀)의 크기 (픽셀 단위)
    :return: 생성된 체스보드 이미지 (NumPy 배열)
    """
    # 실제 칸 수는 코너 수보다 한 개 더 많음
    cols = corners_cols + 1
    rows = corners_rows + 1
    
    # 체스보드 총 크기 계산
    board_width = cols * tile_size
    board_height = rows * tile_size
    
    # 체스보드 이미지 생성
    chessboard = np.zeros((board_height, board_width), dtype=np.uint8)
    
    # 흰색(255)과 검은색(0) 타일 생성
    for row in range(rows):
        for col in range(cols):
            if (row + col) % 2:
                chessboard[row*tile_size:(row+1)*tile_size,
                           col*tile_size:(col+1)*tile_size] = 255  # 흰색 셀

    return chessboard

# 함수 사용 예
corners_cols = 9  # 열 방향 코너 수
corners_rows = 5  # 행 방향 코너 수
tile_size = 50    # 각 타일의 크기는 50x50 픽셀

# 체스보드 생성
chessboard_image = create_chessboard(corners_cols, corners_rows, tile_size)

# 생성된 체스보드 이미지 보여주기
cv.imshow('Generated Chessboard', chessboard_image)

ret, corners = cv.findChessboardCorners(chessboard_image, (corners_cols,corners_rows), None)
if ret:
    img = chessboard_image.copy()
    img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    cv.drawChessboardCorners(img, (corners_cols, corners_rows), corners, ret)
    cv.imshow('Detected Corners', img)

cv.waitKey(0)
cv.destroyAllWindows()