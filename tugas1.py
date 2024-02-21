def berat(tinggi, bmi_harapan):
    berat_badan = bmi_harapan * (tinggi ** 2)
    return berat_badan

def main():
    tinggi = float(input("Masukkan tinggi badan Anda (dalam meter): "))
    bmi_harapan = float(input("Masukkan nilai BMI yang diharapkan: "))
   
    berat_badan = berat(tinggi, bmi_harapan)

    print(f"Berat badan yang diperlukan untuk menyesuaikan BMI adalah {berat_badan} kilogram")

if __name__ == "__main__":
    main()