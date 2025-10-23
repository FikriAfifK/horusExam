# HORUS FULLSTACK EXAM (Vue.js & Flask)

Repositori ini berisi aplikasi *full-stack* sederhana yang berfungsi sebagai sistem manajemen pengguna dengan otentikasi (Login/Register), otorisasi (Router Guards), dan operasi CRUD (Create, Read, Update, Delete) dasar.

Aplikasi ini dibagi menjadi dua bagian utama: *Backend* (Python/Flask) dan *Frontend* (Vue.js).

---

## 🛠️ Teknologi yang Digunakan

### Frontend (Client)
* **Vue.js:** Kerangka kerja utama untuk membangun UI.
* **Pinia:** State Management untuk mengelola status otentikasi global.
* **Vue Router:** Mengelola navigasi dan proteksi rute (*router guards*).
* **Vite:** *Build tool* dan *development server* yang cepat.
* **Axios:** Klien HTTP untuk berkomunikasi dengan API *backend*.

### Backend (Server)
* **Python:** Bahasa pemrograman utama.
* **Flask:** *Web framework* mikro untuk membangun RESTful API.
* **Flask-SQLAlchemy:** ORM (Object-Relational Mapper) untuk interaksi database.
* **Flask-CORS:** Untuk menangani masalah *Cross-Origin Resource Sharing* (CORS).
* **JWT (JSON Web Tokens):** Untuk otentikasi dan otorisasi.

---

## ⚙️ Cara Menjalankan Proyek

### A. Persiapan Backend

1.  **Clone Repositori:**
    ```bash
    git clone [https://github.com/FikriAfifK/horusExam.git](https://github.com/FikriAfifK/horusExam.git)
    cd horusExam/backend
    ```

2.  **Buat Virtual Environment dan Instal Dependensi:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # atau `venv\Scripts\activate` di Windows
    pip install -r requirements.txt
    ```

3.  **Konfigurasi Environment:**
    Buat file `.env` di dalam direktori `backend/` berdasarkan `.env.example`, dan isi variabel database serta *secret key*.

4.  **Jalankan Migrasi Database:**
    ```bash
    flask db upgrade
    ```

5.  **Jalankan Server Backend:**
    ```bash
    python run.py
    ```
    Server akan berjalan di `http://127.0.0.1:5000` (default).

### B. Persiapan Frontend

1.  **Pindah ke Direktori Frontend:**
    ```bash
    cd ../frontend
    ```

2.  **Instal Dependensi:**
    ```bash
    npm install
    # atau
    yarn install
    ```

3.  **Konfigurasi Environment:**
    Buat file `.env` di dalam direktori `frontend/` (di *root* `frontend`) dan set variabel `VITE_API_BASE_URL` sesuai alamat backend (misalnya, `VITE_API_BASE_URL=http://localhost:5000/api`).

4.  **Jalankan Aplikasi Frontend:**
    ```bash
    npm run dev
    # atau
    yarn dev
    ```
    Aplikasi akan berjalan di `http://localhost:5173` (default Vite).

---

## 🔑 Fitur Utama

* **Otentikasi Aman:** Menggunakan JWT untuk otentikasi.
* **Router Guards:** Memastikan halaman `/dashboard` hanya dapat diakses oleh pengguna yang sudah *login*.
* **Auto-Logout:** Axios Interceptor menangani *error* 401 (Unauthorized) untuk membersihkan *token* dan mengalihkan pengguna ke halaman *login*.
* **State Management:** Pinia digunakan untuk mengelola status `user` dan `token` yang persisten menggunakan `localStorage`.
