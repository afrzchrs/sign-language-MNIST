#✋ Sign Language Recognition using CNN & OpenCV
Proyek ini merupakan aplikasi deteksi bahasa isyarat huruf A–Y menggunakan model CNN (grayscale 28×28) dan kamera laptop. Sistem mengambil area tangan pada kotak ROI (Region of Interest) yang berada tepat di tengah layar, kemudian memprediksi huruf secara real-time.

Aplikasi ini cocok digunakan untuk pembelajaran bahasa isyarat atau tugas Computer Vision dasar.

#🚀 Fitur Utama
✔ Deteksi bahasa isyarat real-time

✔ Kotak ROI otomatis di tengah layar

✔ Model CNN custom (grayscale)

✔ Preprocessing otomatis:

Grayscale

Threshold (hitam-putih)

Resize ke 28×28

Normalisasi

✔ Menampilkan prediksi + confidence

✔ Jendela debug untuk melihat input ke model

#📦 Instalasi
Pastikan Python 3 sudah terpasang.

Install dependensi:

bash
Copy code
pip install tensorflow
pip install opencv-python
pip install numpy

#📁 Struktur Proyek
bash
Copy code
/project-folder
│
├── model/
│   └── sign_language_classifier.h5
│
├── main.py
└── README.md
Pastikan model .h5 berada di folder model/.

#▶ Cara Menjalankan
Pastikan webcam terhubung.

Jalankan program:

bash
Copy code
python main.py
Arahkan tangan Anda ke dalam kotak tengah layar.

Hasil prediksi akan tampil di layar.

Tekan Q untuk keluar.

#🧠 Teknologi yang Digunakan
TensorFlow/Keras → memuat model CNN

OpenCV → kamera + pengolahan gambar

NumPy → pemrosesan array

#🔍 Cara Kerja Sistem
Program membuka webcam.

Kotak ROI (200×200 px) muncul di tengah layar.

Gambar dalam ROI diproses:

Diubah ke grayscale

Di-threshold

Di-resize menjadi 28×28

Gambar diprediksi oleh model CNN yang sudah Anda latih.

Hasil huruf + nilai confidence ditampilkan di layar.

