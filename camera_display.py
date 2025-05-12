import cv2

# Membuka kamera default (0)
cap = cv2.VideoCapture(0)

# Memeriksa apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

# Loop untuk membaca dan menampilkan frame
while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()

    # Memeriksa apakah frame berhasil dibaca
    if not ret:
        print("Tidak dapat menerima frame")
        break

    # Menampilkan frame
    cv2.imshow('Frame', frame)

    # Menunggu tombol ditekan untuk keluar dari loop (misalnya tombol 'q')
    if cv2.waitKey(1)q == ord('q'):
        break

# Melepaskan objek VideoCapture dan menutup semua jendela
cap.release()
cv2.destroyAllWindows()