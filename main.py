import cv2
import numpy as np

frame1 = None
frame2 = None

ret1 = False
ret2 = False

visible_optic_flow = False

# Откройте видеофайл
video_capture = cv2.VideoCapture('video.mp4')  # Укажите путь к вашему видеофайлу

# Проверка успешного открытия видео
if not video_capture.isOpened():
    print("Ошибка при открытии видеофайла.")
    exit()

while True:
    # Считайте кадр из видео
    
    ret1, frame1 = video_capture.read()

    # Проверьте, успешно ли считан кадр
    if not ret1:
        print("Не удалось считать кадр. Возможно, достигнут конец видео.")
        break
    
    if ret1 and ret2:

        # Переведите кадры в градации серого
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        # Оптический поток с использованием метода Farneback
        flow = cv2.calcOpticalFlowFarneback(gray1, gray2, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # Вычислиv величину и угол оптического потока
        magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

        # Преобразуtv величину и угол в цветное изображение
        hsv = np.zeros_like(frame1)
        hsv[..., 1] = 255
        hsv[..., 0] = angle * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
        flow_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        
        # Отображение текущего кадра
        if visible_optic_flow:
            cv2.imshow('Video', flow_rgb)
        else:
            cv2.imshow('Video', frame1)

    frame2 = frame1.copy()
    ret2 = ret1
    
    key = cv2.waitKey(30) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        visible_optic_flow = not visible_optic_flow

# Освобождение ресурсов и закрытие окон после завершения работы
video_capture.release()
cv2.destroyAllWindows()