# Tugas Kecil 3 Strategi Algoritma: 15 Puzzle


Program menerima sebuah file konfigurasi 15 puzzle dan mencoba menyelesaikan puzzle. Rincian puzzle seperti nilai fungsi kurang dan banyak simpul yang dibangkitkan. Jika puzzle dapat diselesaikan, maka program akan memberikan opsi pada pengguna untuk melihat animasi penyelesaian puzzle mulai dari keadaaan awal puzzle sampai solusi dicapai.

## Requirement Program
```
  - Python 3.x
  - Library tkinter
```

## Cara Penggunaan
### Windows
Pada direktori utama repositori, jalankan:
```
 $py src/main.py
```

### Linux
Pada direktori utama repositori, jalankan:
```
 $Python3 src/main.py
```

## File Config
File config memiliki aturan sebagai berikut:
- Terdiri dari tepat 4 baris
- Tiap baris memiliki tepat 4 bilangan yang dipisahkan spasi
- Ke-16 bilangan yang terdapat pada config merupakan permutasi dari 0..15
- Tile kosong pada puzzle direpresentasikan dengan angka 0 pada config
