# Deklarasi
matriks1 = []
matriks2 = []

# Meminta input untuk matriks pertama
print("Masukkan elemen untuk matriks pertama:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks1.append(baris)
    
# Meminta input untuk matriks kedua
print("/nMasukan elemen untuk matriks kedua:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukan elemen baris {i+1}, kolom {j+1}: "))
    matriks2.append(baris)
    
# Penjumlahan Matriks
hasil = []
for i in range(2):
    baris = []
    for j in range(2):
        baris.append(matriks1[i][j] + matriks2[i][j])
    hasil.append(baris)
    
# Menampilkan hasil penjumlahan
print("/nHasil penjumlahan matriks:")
for baris in hasil:
    print(baris)