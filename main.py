import cv2

# Откройте видеофайл
video_capture = cv2.VideoCapture('video.mp4')  # Укажите путь к вашему видеофайлу

# Проверка успешного открытия видео
if not video_capture.isOpened():
    print("Ошибка при открытии видеофайла.")
    exit()

while True:
    # Считайте кадр из видео
    ret, frame = video_capture.read()

    # Проверьте, успешно ли считан кадр
    if not ret:
        print("Не удалось считать кадр. Возможно, достигнут конец видео.")
        break

    # Обрабатывайте кадр здесь, например, можно применить алгоритм оптического потока

    # Отображение текущего кадра
    cv2.imshow('Video', frame)

    # Проверка на нажатие клавиши 'q' для выхода из цикла
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Освобождение ресурсов и закрытие окон после завершения работы
video_capture.release()
cv2.destroyAllWindows()