def knapsack(items, capacity):
    n = len(items)
    # DP tablosu oluştur
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # DP tablosunu doldur
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1][0] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], items[i - 1][1] + dp[i - 1][w - items[i - 1][0]])

    # Optimum değeri ve seçilen öğeleri bul
    optimum_value = dp[n][capacity]
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return optimum_value, selected_items

# items.txt dosyasından ürünleri oku
with open("items.txt", "r") as file:
    items = []
    for line in file:
        weight, price = map(int, line.split())
        items.append((weight, price))

# Sırt çantası kapasitesi
capacity = 25

# Sırt çantası problemi çöz
optimum_value, selected_items = knapsack(items, capacity)

# Seçilen ürünleri ekrana yazdır
print("Sırt Çantasında Taşınan Ürünler:")
for item in selected_items:
    print("- Ağırlık:", item[0], ", Fiyat:", item[1])

# Sonuçları ekrana yazdır
print("Toplam Ağırlık:", sum(item[0] for item in selected_items))
print("Toplam Fiyat:", optimum_value)
