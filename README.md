# Web Aplikasi Sistem Informasi OSIS

## 1. Deskripsi Proyek

Proyek ini merupakan pembuatan aplikasi web **Sistem Informasi 
OSIS** yang dibangun menggunakan **Python Flask** dan **SQLite**. Aplikasi ini dirancang untuk membantu pengelolaan data anggota OSIS, kegiatan OSIS, dan surat administrasi dengan fitur login, tambah/edit/hapus data, serta pencarian data.

Dengan adanya aplikasi ini, pengurus OSIS dapat lebih mudah 
mengelola informasi secara terpusat dan efisien.

---

## 2. Teknologi yang Digunakan (Tech Stack)

- **Bahasa Pemrograman:** Python 3
- **Framework Web:** Flask
- **Database:** SQLite
- **Version Control:** Git
- **Editor Kode:** VSCode / Vim / Nano
- **Library Tambahan:**
  - Flask-Login
  - Flask-SQLAlchemy

---

## 3. Persiapan Lingkungan di Debian

### 1. Install Python dan Git
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git

## 4. Fitur Teknis (Functional Requirements)

- **Sistem Autentikasi:** 
  Pengguna dapat melakukan login menggunakan username dan 
password yang terdaftar untuk mengakses dashboard aplikasi.
  
- **Manajemen Data Anggota OSIS:**
  Menambahkan, mengedit, dan menghapus data anggota OSIS yang 
meliputi nama, kelas, dan kontak.

- **Manajemen Data Kegiatan:**
  Fitur untuk mengelola kegiatan OSIS, termasuk menambah,
 mengubah, dan menghapus kegiatan dengan atribut nama kegiatan 
dan tanggal.

- **Manajemen Data Surat/Administrasi:**
  Memudahkan pengelolaan surat keluar/masuk, dengan nomor



## 5. Non-Functional Requirements (Persyaratan Non-Teknis)

**User Interface (UI) / User Experience (UX):**  
Aplikasi menggunakan desain sederhana dan responsif dengan bantuan framework CSS Bootstrap. Hal ini membuat tampilan aplikasi nyaman di berbagai perangkat, baik desktop maupun mobile, sehingga pengguna dapat dengan mudah mengakses dan mengoperasikan 
 aplikasi.

**Keamanan:**  
Password pengguna di-hash menggunakan library `werkzeug.security` untuk mencegah kebocoran data. Sistem login menggunakan Flask-Login dengan session management yang aman. Input dari pengguna 
divalidasi untuk mencegah serangan seperti SQL Injection dan 
Cross-Site Scripting (XSS).

**Performa:**  
Penggunaan SQLite sebagai database ringan memastikan respon 
aplikasi cepat, terutama untuk penggunaan dalam skala kecil 
sampai menengah. Struktur kode yang modular juga membantu 
mempercepat pengembangan dan pemeliharaan aplikasi.

**Skalabilitas:**  
Kode aplikasi didesain modular menggunakan blueprint Flask, 
sehingga mudah dikembangkan ke fitur tambahan atau migrasi ke 
database lain jika diperlukan, tanpa harus menulis ulang seluruh kode.

**Ketergunaan:**  
Aplikasi mudah digunakan oleh pengguna dengan latar belakang non-teknis. Form input dilengkapi validasi yang jelas dan feedback langsung sehingga meminimalkan kesalahan input data.

---

## 6. Penggunaan Git dan Manajemen Kode

**Inisialisasi Repositori:**  
Repositori Git diinisialisasi dengan perintah:  
```bash
git init

## 7. Hasil dan Kesimpulan

### Fitur yang Berhasil Diimplementasikan
- Sistem login user dengan autentikasi username dan password.
- Manajemen data anggota OSIS: tambah, edit, hapus, dan daftar 
  anggota.
- Manajemen kegiatan OSIS: tambah, edit, hapus, dan daftar 
  kegiatan.
- Manajemen surat/administrasi: tambah, edit, hapus surat serta   pencarian surat berdasarkan nomor dan perihal.
- Fitur pencarian data anggota dan surat berjalan dengan baik.
- Tampilan antarmuka yang responsif dan mudah digunakan.

### Kendala yang Dihadapi
- Kesulitan konfigurasi environment dan instalasi dependencies 
  di Debian.
- Beberapa error sintaksis di kode awal yang perlu diperbaiki, seperti penggunaan `__file__` dan `__name__`.
- Penyesuaian fitur pencarian agar hasilnya relevan dan cepat.
- Pengelolaan session dan keamanan password masih perlu peningkatan lebih lanjut.

### Kesimpulan
Proyek pembuatan aplikasi web Sistem Informasi OSIS ini berhasil mengimplementasikan fitur utama yang dibutuhkan oleh OSIS untuk 
pengelolaan anggota, kegiatan, dan surat administrasi. Meskipun terdapat beberapa kendala teknis, pengalaman ini memberikan pemahaman yang lebih dalam tentang pengembangan aplikasi web menggunakan Python Flask dan SQLite di lingkungan Debian. Ke depan, aplikasi ini dapat dikembangkan dengan fitur keamanan tambahan dan antarmuka yang lebih menarik agar lebih efektif digunakan oleh pengguna.

