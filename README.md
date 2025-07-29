# Love Potions Karaoke Player

Proyek ini berisi aplikasi karaoke sederhana untuk lagu "Love Potions", lengkap dengan sinkronisasi lirik dan pemutar audio. Terdapat dua cara untuk menikmati karaoke: melalui antarmuka web (HTML/JavaScript) dan aplikasi desktop berbasis Python (Tkinter & pygame).

## Struktur Folder

- **index.html**  
  Halaman web karaoke interaktif. Menampilkan lirik yang disinkronkan dengan lagu, tombol kontrol (play, pause, restart), dan fitur skip ke bagian tertentu lirik.  
  - Menggunakan file audio `Love Potions.mp3` dan lirik dari `lyrics.txt` (data lirik juga tertanam di script).

- **Love Potions.mp3**  
  File audio lagu yang digunakan untuk karaoke.

- **lyrics.txt**  
  File teks berisi lirik lagu lengkap beserta timestamp (format `[mm:ss.xx]`) untuk sinkronisasi.

- **play_lyrics_enhanced.py**  
  Aplikasi desktop karaoke berbasis Python.  
  - Menampilkan lirik secara bertahap (efek mengetik) sesuai waktu lagu.
  - Menggunakan `pygame` untuk pemutaran audio dan `tkinter` untuk antarmuka grafis.
  - Terdapat tombol Play, Pause/Resume, serta tampilan waktu dan lirik berikutnya.

## Cara Menjalankan

### 1. Web Karaoke (index.html)
1. Pastikan file `Love Potions.mp3` berada satu folder dengan `index.html`.
2. Buka `index.html` menggunakan browser modern (Chrome, Edge, Firefox).
3. Gunakan tombol Play/Pause/Restart dan fitur skip untuk bernyanyi mengikuti lirik yang tampil.

### 2. Desktop Karaoke (play_lyrics_enhanced.py)
1. Pastikan Python 3 sudah terinstal.
2. Install dependensi:
   ```sh
   pip install pygame
   ```
3. Jalankan aplikasi:
   ```sh
   python play_lyrics_enhanced.py
   ```
4. Akan muncul jendela karaoke dengan lirik yang berjalan sesuai lagu.

## Catatan

- Lirik pada `lyrics.txt` mengandung konten eksplisit.
- Untuk menambah lagu lain, ganti file mp3 dan lirik, serta sesuaikan timestamp pada lirik.

---

Selamat bernyanyi ya!