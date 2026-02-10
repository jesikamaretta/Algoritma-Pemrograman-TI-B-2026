def rata_rata(nilai):
    if not nilai:
        return "Data kosong"
    return sum(nilai) / len(nilai)

# Contoh pemanggilan
data = [80, 75, 90, 60, 85]
print("Rata-rata:", rata_rata(data))

