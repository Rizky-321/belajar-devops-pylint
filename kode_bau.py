"""Modul untuk demonstrasi code quality dengan Pylint."""


def hitung_hasil(nilai):
    """Menghitung total dari beberapa nilai."""
    return sum(nilai)


def main():
    """Menjalankan program utama."""
    nilai = [1, 2, 3, 4, 5, 6]
    hasil = hitung_hasil(nilai)
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()
    