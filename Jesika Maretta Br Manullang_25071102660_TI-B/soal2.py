def bilangan_prima(n):
    prima_list = []
    for num in range(2, n + 1):
        is_prima = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prima = False
                break
        if is_prima:
            prima_list.append(num)
    return prima_list

# Memanggil fungsi
hasil = bilangan_prima(50)
print("Bilangan prima dari 1 sampai 50:")
print(hasil)
