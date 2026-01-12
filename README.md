# dicoding-data-analysis
Data analysis

# 📊 RFM Customer Segmentation Dashboard

Dashboard ini merupakan hasil analisis segmentasi pelanggan menggunakan metode RFM (Recency, Frequency, Monetary).
Tujuan dari proyek ini adalah untuk memahami perilaku pelanggan berdasarkan aktivitas transaksi dan nilai kontribusinya terhadap perusahaan.

Dashboard dibangun menggunakan Streamlit dan menampilkan visualisasi interaktif untuk membantu proses analisis data secara lebih intuitif.
Keterangan:
dashboard/dashboard.py → File utama Streamlit dashboard
dashboard/rfm_result.csv → Dataset hasil perhitungan RFM
notebook.ipynb → Proses analisis data & pembuatan RFM
requirements.txt → Daftar library yang digunakan

# ⚙️ Setup Environment

🔹 Menggunakan Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

🔹 Menggunakan Shell / Terminal (Pipenv)
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

# ▶️ Menjalankan Aplikasi Streamlit

Pastikan berada di direktori submission/dashboard, lalu jalankan:
streamlit run dashboard.py
Setelah itu, aplikasi akan otomatis terbuka di browser.

# 📈 Fitur Dashboard

Dashboard ini memiliki beberapa fitur utama, antara lain:

# 📊 Ringkasan KPI
Total pelanggan
Total pendapatan
Rata-rata frekuensi transaksi

# 🧩 Distribusi Segmentasi Pelanggan

Visualisasi proporsi setiap segmen RFM

# 💰 Kontribusi Revenue per Segment

Analisis segmen pelanggan dengan kontribusi pendapatan terbesar

# 📊 Distribusi RFM Score

Persebaran nilai RFM pelanggan

# ⚙️ Filter Interaktif

Memilih segmen pelanggan secara dinamis

# 📄 Preview Data

Menampilkan data RFM pelanggan

# 🧠 Metodologi Analisis

Segmentasi pelanggan dilakukan menggunakan metode RFM, dengan penjelasan sebagai berikut:
- Recency (R): Seberapa baru pelanggan melakukan transaksi terakhir
- Frequency (F): Seberapa sering pelanggan melakukan transaksi
- Monetary (M): Total nilai transaksi pelanggan

Setiap metrik diberi skor, kemudian digabungkan untuk membentuk RFM Score dan klasifikasi segmen pelanggan.

# 🛠️ Tools & Library

Python
Pandas
Matplotlib
Streamlit

# ✅ Kesimpulan

Melalui dashboard ini, dapat diketahui segmen pelanggan yang memiliki nilai bisnis paling tinggi serta pola perilaku pelanggan berdasarkan aktivitas transaksinya.
Hasil analisis ini dapat digunakan sebagai dasar pengambilan keputusan strategi pemasaran dan retensi pelanggan.
