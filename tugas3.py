def hitung_pendapatan(gaji_perjam, jam_kerja_perminggu):
    # Hgaji sebelum pajak
    pendapatan_sebelum_pajak = gaji_perjam * jam_kerja_perminggu * 5

    # pajak
    pajak = 14 * (pendapatan_sebelum_pajak / 100)
    pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak

    #  belanja
    belanja_baju_aksesoris = 10 * (pendapatan_setelah_pajak/100)
    belanja_alat_tulis = 1 * (pendapatan_setelah_pajak / 100)

    # sedekah
    sisa_uang = pendapatan_setelah_pajak - belanja_baju_aksesoris - belanja_alat_tulis
    sedekah = 25 * (sisa_uang/100)
    yatim = 30 * (sedekah /100)
    kaum_dhuafa = sedekah - yatim

    return pendapatan_sebelum_pajak, pendapatan_setelah_pajak, belanja_baju_aksesoris, belanja_alat_tulis, sedekah, yatim, kaum_dhuafa

def main():
    gaji_per_jam = float(input("Masukkan gaji per jam yang Anda inginkan: "))
    jam_kerja_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))

    pendapatan_sebelum_pajak, pendapatan_setelah_pajak, belanja_baju_aksesoris, belanja_alat_tulis, sedekah, yatim, kaum_dhuafa = hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu)

    print("1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: Rp.", pendapatan_sebelum_pajak)
    print("2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp.", pendapatan_setelah_pajak)
    print("3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp.", belanja_baju_aksesoris)
    print("4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp.", belanja_alat_tulis)
    print("5. Jumlah uang yang akan Budi sedekahkan: Rp.", sedekah)
    print("6. Jumlah uang yang akan diterima anak yatim: Rp.",yatim)
    print("7. Jumlah uang yang akan diterima kaum dhuafa: Rp.", kaum_dhuafa)

if __name__ == "__main__":
    main()