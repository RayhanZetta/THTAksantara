import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Mengambil gambar frame tiap frame
    ret, captured_frame = cap.read()
    output_frame = captured_frame.copy()

    # Mengganti gambar yang asli menjadi BGR Convert original image to BGR, since Lab is only available from BGR
    captured_frame_bgr = cv2.cvtColor(captured_frame, cv2.COLOR_BGRA2BGR)
    # Blur pertama untuk mengurangi noise sebelum konversi ruang warna
    captured_frame_bgr = cv2.medianBlur(captured_frame_bgr, 3)
    # Mengkonversikan ke ruang warna Lab, hanya perlu memeriksa satu untuk warna merah 
    captured_frame_lab = cv2.cvtColor(captured_frame_bgr, cv2.COLOR_BGR2Lab)
    # Membatasi gambar Lab, mempertahankan piksel merah saja
    captured_frame_lab_red = cv2.inRange(captured_frame_lab, np.array([20, 150, 150]), np.array([190, 255, 255]))
    # Blur kedua untuk mengurangi lebih banyak noise, deteksi lingkaran lebih mudah
    captured_frame_lab_red = cv2.GaussianBlur(captured_frame_lab_red, (5, 5), 2, 2)
    # Menggunakan transformasi Hough untuk mendeteksi lingkaran pada gambar
    circles = cv2.HoughCircles(captured_frame_lab_red, cv2.HOUGH_GRADIENT, 1, captured_frame_lab_red.shape[0] / 8, param1=100, param2=18, minRadius=5, maxRadius=60)

	# Apabila sudah ditemukan lingkaran, maka akan digambar outline
	# Hanya perlu mendeteksi satu lingkaran , karena hanya akan ada satu objek referensi
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        cv2.circle(output_frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 255, 0), thickness=2)

    # Menampilkan bingkai yang dihasilkan, keluar dengan q
    cv2.imshow('frame', output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Setelah semuanya selesai, menampilkan gambar
cap.release()
cv2.destroyAllWindows()