# ✋ Sign Language Recognition using CNN & OpenCV

Proyek ini merupakan aplikasi **deteksi bahasa isyarat huruf A–Y** menggunakan **model CNN (grayscale 28×28)** dan kamera laptop. Sistem mengambil area tangan pada **kotak ROI (Region of Interest)** yang berada tepat di tengah layar, kemudian memprediksi huruf secara real-time.
---

## 🚀 Fitur Utama

* ✔ **Deteksi bahasa isyarat real-time**
* ✔ **Kotak ROI otomatis di tengah layar**
* ✔ **Model CNN custom (grayscale)**
* ✔ Preprocessing otomatis:

  * Grayscale
  * Threshold (hitam-putih)
  * Resize ke 28×28
  * Normalisasi
* ✔ Menampilkan prediksi + confidence
* ✔ Jendela debug untuk melihat input ke model

---

## 📦 Instalasi

Pastikan Python 3 sudah terpasang.

Install dependensi:

```bash
pip install tensorflow
pip install opencv-python
pip install numpy
```

---

## 📁 Struktur Proyek

```
/project-folder
│
├── model/
│   └── sign_language_classifier.h5
│
├── main.py
└── README.md
```

Pastikan model `.h5` berada di folder `model/`.

---

## ▶ Cara Menjalankan

1. Pastikan webcam terhubung.
2. Jalankan program:

```bash
python main.py
```

3. Arahkan tangan Anda ke dalam kotak **tengah layar**.
4. Hasil prediksi akan tampil di layar.
5. Tekan **Q** untuk keluar.

---

## 🧠 Teknologi yang Digunakan

* **TensorFlow/Keras** → memuat model CNN
* **OpenCV** → kamera + pengolahan gambar
* **NumPy** → pemrosesan array

---

## 🔍 Cara Kerja Sistem

1. Program membuka webcam.
2. Kotak ROI (200×200 px) muncul di tengah layar.
3. Gambar dalam ROI diproses:

   * Diubah ke grayscale
   * Di-threshold
   * Di-resize menjadi 28×28
4. Gambar diprediksi oleh model CNN yang sudah Anda latih.
5. Hasil huruf + nilai confidence ditampilkan di layar.

---
