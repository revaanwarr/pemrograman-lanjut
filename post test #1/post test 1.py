def barang_teruntungkan(harga_dasar_A, harga_jual_A, harga_dasar_B, harga_jual_B, harga_dasar_C, harga_jual_C):
  """
  Fungsi untuk menentukan barang dengan keuntungan terbesar.

  Args:
    harga_dasar_A: Harga dasar barang A.
    harga_jual_A: Harga jual barang A.
    harga_dasar_B: Harga dasar barang B.
    harga_jual_B: Harga jual barang B.
    harga_dasar_C: Harga dasar barang C.
    harga_jual_C: Harga jual barang C.

  Returns:
    Huruf yang merepresentasikan barang dengan keuntungan terbesar.
  """

  # Hitung keuntungan masing-masing barang
  keuntungan_A = harga_jual_A - harga_dasar_A
  keuntungan_B = harga_jual_B - harga_dasar_B
  keuntungan_C = harga_jual_C - harga_dasar_C

  # Bandingkan keuntungan dan return barang dengan keuntungan terbesar
  if keuntungan_A >= keuntungan_B and keuntungan_A >= keuntungan_C:
    return "A"
  elif keuntungan_B >= keuntungan_A and keuntungan_B >= keuntungan_C:
    return "B"
  else:
    return "C"

# Input harga dari pengguna
harga_dasar_A = float(input("Masukkan harga dasar barang A: "))
harga_jual_A = float(input("Masukkan harga jual barang A: "))
harga_dasar_B = float(input("Masukkan harga dasar barang B: "))
harga_jual_B = float(input("Masukkan harga jual barang B: "))
harga_dasar_C = float(input("Masukkan harga dasar barang C: "))
harga_jual_C = float(input("Masukkan harga jual barang C: "))

# Panggil fungsi dan tampilkan hasil
barang_terbaik = barang_teruntungkan(harga_dasar_A, harga_jual_A, harga_dasar_B, harga_jual_B, harga_dasar_C, harga_jual_C)
print(f"Barang yang harus ditawarkan adalah barang {barang_terbaik}")