# Aplikasi Manajemen Toko Sederhana dengan Flask

Aplikasi web sederhana ini dibangun menggunakan Flask untuk mengelola daftar toko. Pengguna dapat mendaftar, masuk, dan kemudian membuat, melihat, mengedit, serta menghapus toko mereka sendiri.

## Fitur Utama

* Autentikasi Pengguna: Sistem pendaftaran dan login pengguna yang aman.

* Manajemen Toko:

    * Melihat daftar toko yang dimiliki pengguna.

    * Menambahkan toko baru.

    * Mengedit nama toko yang sudah ada.

    * Menghapus toko.

* Database SQLite: Menggunakan SQLite sebagai sistem manajemen database yang ringan dan mudah dikelola.

* Templating Jinja2: Antarmuka pengguna yang dinamis dan responsif dibangun menggunakan sistem templating Jinja2 dari Flask.

## Struktur Proyek

```
flask_store_management/
├── app.py              # Logika aplikasi utama (konfigurasi, model, routes)
├── requirements.txt    # Daftar dependensi Python yang diperlukan
└── templates/          # Direktori untuk file HTML (template Jinja2)
    ├── base.html       # Template dasar untuk semua halaman
    ├── login.html      # Halaman antarmuka login pengguna
    └── stores.html     # Halaman untuk manajemen toko (daftar, tambah, edit)
```

## Persyaratan Sistem

Pastikan Anda memiliki Python 3.x terinstal di sistem operasi Anda.

## Panduan Instalasi

Ikuti langkah-langkah di bawah ini untuk mengatur dan menjalankan aplikasi di lingkungan pengembangan lokal Anda:

1.  Kloning Repositori:
    Jika Anda belum mengkloning repositori ini, lakukan dengan perintah berikut:

    ```bash
    git clone [https://github.com/elramaholding/flask-store-management.git](https://github.com/elramaholding/flask-store-management.git)
    cd flask-store-management
    ```

2.  Buat Virtual Environment:
    Sangat disarankan untuk menggunakan virtual environment untuk mengisolasi dependensi proyek.

    ```bash
    python3 -m venv venv
    ```

3.  Aktifkan Virtual Environment:

    * Untuk macOS / Linux:

        ```bash
        source venv/bin/activate
        ```

    * Untuk Windows:

        ```bash
        venv\Scripts\activate
        ```

4.  Instal Dependensi Proyek:
    Instal semua paket Python yang diperlukan yang tercantum dalam `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Cara Menjalankan Aplikasi

Setelah semua dependensi terinstal dan virtual environment aktif:

1.  Jalankan Aplikasi Flask:

    ```bash
    flask run
    ```

    Jika perintah `flask run` tidak berfungsi, Anda bisa mencoba:

    ```bash
    python app.py
    ```

2.  Akses Aplikasi:
    Buka browser web Anda dan navigasikan ke alamat berikut:
    http://127.0.0.1:5000/

## Kredensial Pengguna Default

Untuk mempermudah pengujian dan demonstrasi, aplikasi ini dilengkapi dengan satu pengguna default yang sudah terdaftar:

* Username: admin

* Password: admin123

Anda dapat menggunakan kredensial ini untuk login dan mulai mengelola toko Anda.

## Catatan Penting untuk Pengembangan

* Kunci Rahasia (`SECRET_KEY`): Untuk lingkungan produksi, `SECRET_KEY` di `app.py` harus diubah ke nilai yang lebih kuat dan disimpan sebagai variabel lingkungan, bukan langsung di kode.

* Database: Aplikasi ini menggunakan SQLite dengan file `store.db`. File ini akan dibuat secara otomatis saat aplikasi pertama kali dijalankan. Untuk aplikasi skala besar, pertimbangkan menggunakan database relasional yang lebih kuat seperti PostgreSQL atau MySQL.

* Konfirmasi Penghapusan: Pesan konfirmasi untuk penghapusan toko saat ini menggunakan fungsi `confirm()` JavaScript bawaan. Untuk pengalaman pengguna yang lebih baik dan konsisten, disarankan untuk mengimplementasikan modal konfirmasi kustom.

---

Terima kasih telah menggunakan Aplikasi Manajemen Toko Sederhana ini!