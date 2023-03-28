# Input data mahasiswa
data_mahasiswa = []
while True:
    nim = input("Masukkan NIM mahasiswa (0 untuk selesai): ")
    if nim == '0':
        break
    nama = input("Masukkan Nama mahasiswa: ")
    nilai = int(input("Masukkan Nilai mahasiswa: "))
    data_mahasiswa.append({'nim': nim, 'nama': nama, 'nilai': nilai})

# Fungsi untuk menentukan grade berdasarkan nilai
def get_grade(nilai):
    if nilai >= 90:
        return 'A'
    elif nilai >= 80:
        return 'B'
    elif nilai >= 70:
        return 'C'
    elif nilai >= 60:
        return 'D'
    else:
        return 'E'


# Membuat short berdasarkan Nilai Tertinggi
short_nilai_tertinggi = sorted(data_mahasiswa, key=lambda k: k['nilai'], reverse=True)
print("\nShort berdasarkan Nilai Tertinggi:")
for mhs in short_nilai_tertinggi:
    print("NIM: ", mhs['nim'])
    print("Nama: ", mhs['nama'])
    print("Nilai:", mhs['nilai'])
    print("Grade: ", get_grade(mhs['nilai']))
    print("")