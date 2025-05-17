with open("26.txt") as f:
    n, k = [int(x) for x in f.readline().split()]
    travels = [] # варианты путешествия м-у зонами
    for s in f:
        frm, to, price = [int(x) for x in s.split()]
        travels.append([frm, to, p])
# логично сначала смотреть все маршруты из первой, потом все маршруты из второй и тд
travels.sort()

# минимальная стоимость трансфера в зоны
mnPrice = [10 ** 20] * 10 ** 6
mnPrice[1] = 0 # в зоне "1" затраты равны 0

for i in range(n):
    frm, to, p = travels[i]
    sumPrice = minPrice[frm] + p # с учетом предыдущих перелётов
    if sumPrice <= k:
        minPrice[to] = min(minPrice[to], sumPrice) # если результат равен 10 ** 20 -> в пункт невозможно попасть
ans1 = max(i for i in range(10 ** 6) if minPrice[i] != 10 ** 20)
# максимальный номер зоны <=> максимальный индекс, в котором значение стоимости != 10 ** 20
ans2 = k - minPrice[ans1] # вычитаем из всей суммы минимальный затрат средств до клнечной зоны
print(ans1, ans2)
