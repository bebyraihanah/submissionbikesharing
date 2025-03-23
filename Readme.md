# 🚴‍♂️ Bike Sharing Dashboard
📌 Deskripsi Proyek
Proyek ini merupakan analisis data peminjaman sepeda menggunakan dataset Bike Sharing. Data ini mencatat pola peminjaman sepeda berdasarkan waktu, hari kerja vs akhir pekan, serta faktor cuaca yang mempengaruhi jumlah penyewaan sepeda.

Dashboard ini dibuat menggunakan Streamlit dan menampilkan berbagai visualisasi interaktif untuk memahami pola peminjaman sepeda.

### 📂 Struktur Folder

📦 SUBMISSION_BIKE_SHARING

│-- 📁 DASHBOARD

│   │-- dashboard.py      # Kode utama dashboard Streamlit

│   │-- all_data.csv      # Dataset Bike Sharing

│-- 📁 DATA             

│   │-- day.csv      # Raw Dataset Bike Sharing

│   │-- hour.csv      # Raw Dataset Bike Sharing

│   │-- Readme.txt      # Dokumentasi Dataset Bike Sharing

│-- README.md             # Dokumentasi proyek

│-- requirements.txt      # Daftar library yang dibutuhkan

│-- url.txt      #Daftar URL yang digunakan dalam

│-- Notebook.ipynb      # Daftar scipt python untuk analisis data

### 🛠 Instalasi dan Menjalankan Dashboard

1️⃣ Clone Repository
git clone https://github.com/bebyraihanah/submissionbike.git

2️⃣ Buat Virtual Environment (Opsional)
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows

3️⃣ Instal Dependencies
pip install -r requirements.txt

4️⃣ Jalankan Streamlit
streamlit run DASHBOARD/dashboard.py

### 📊 Fitur Analisis
1️⃣ Hari Kerja vs Akhir Pekan
Perbandingan jumlah peminjaman di hari kerja dan akhir pekan.
Dapat memisahkan data peminjaman antara casual users dan registered users.

2️⃣ Pola Peminjaman per Jam
Filter berdasarkan jam tertentu (01:00 - 23:00).
Identifikasi jam sibuk di pagi dan sore hari.

3️⃣ Pengaruh Cuaca
Menampilkan pengaruh cuaca terhadap jumlah peminjaman sepeda.
Filter berdasarkan musim: Spring (semi), Summer (panas), Fall (gugur), Winter (salju).

### 📑 Sumber Data
Dataset yang digunakan berasal dari Bike Sharing Dataset - Kaggle. https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset 

