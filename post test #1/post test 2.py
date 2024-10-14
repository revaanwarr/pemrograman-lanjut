def tentukan_kelas(nrp_akhir):
  """
  Fungsi untuk menentukan kelas mahasiswa berdasarkan 3 digit akhir NRP.

  Args:
    nrp_akhir: Tiga digit akhir NRP mahasiswa.

  Returns:
    Kelas mahasiswa.
  """

  # Konversi input menjadi integer
  nrp_akhir = int(nrp_akhir)

  # Tentukan rentang NRP
  if 1 <= nrp_akhir <= 100:
    if nrp_akhir % 2 == 1:
      return "K1"
    else:
      return "K2"
  elif 101 <= nrp_akhir <= 200:
    if nrp_akhir % 2 == 1:
      return "K3"
    else:
      return "K4"
  elif 201 <= nrp_akhir <= 300:
    if nrp_akhir % 2 == 1:
      return "K5"
    else:
      return "K6"
  else:
    if nrp_akhir % 2 == 1:
      return "K7"
    else:
      return "K8"

# Contoh penggunaan
nrp_input = input("Masukan akhiran NRP: ")
kelas = tentukan_kelas(nrp_input)
print("Mahasiswa masuk ke kelas", kelas)