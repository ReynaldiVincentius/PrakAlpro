def nilai_fungsi(x):
    fungsi = 2 * x**3 + 2 * x + 15 / x
    return fungsi

def main():
    x = int(input("Masukkan nilai x(bilangan bulat): "))
    fungsi = nilai_fungsi(x)
    print("fungsi f(x) =", fungsi)

if __name__ == "__main__":
    main()