jumlah = int(input("Jumlah mahasiswa : "))
if jumlah <= 0:
  print("Jumlah mahasiswa harus lebih dari 0")
else:
  total = 0
  for i in range(1, jumlah + 1):
    nilai = float(input(f"Masukkan Nilai Mahasiswa {i} : "))
    total += nilai

  rata = total / jumlah
  print(f"Nilai Rata-rata : {rata:g}")
