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
    if nilai == 100 :
        return "S"
    elif nilai <= 99 and nilai >= 85 :
        return "A"
    elif nilai <= 84 and nilai >= 75 :
        return "B" 
    elif nilai <= 74 and nilai >= 60 :
        return "C" 
    elif nilai <= 59 and nilai >= 50 :
        return "D" 
    elif nilai <= 49 and nilai >= 1 :
        return "E"
    elif nilai == 0 :
        return "F"
    else:
        return "Tidak Valid"

# Membuat short berdasarkan Nilai Tertinggi
short_nilai_tertinggi = sorted(data_mahasiswa, key=lambda k: k['nilai'], reverse=True)
print("\nShort berdasarkan Nilai Tertinggi:")
for mhs in short_nilai_tertinggi:
    print("NIM: ", mhs['nim'])
    print("Nama: ", mhs['nama'])
    print("Nilai:", mhs['nilai'])
    print("Grade: ", get_grade(mhs['nilai']))
    print("")