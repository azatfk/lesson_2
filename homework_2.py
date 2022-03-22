arr = list(map(int, input('Введите некоторое количество целых чисел через пробел: ').split()))
# Например: Введите некоторое количество целых чисел через пробел: 1 2 3 4 5 6 7
print(arr)  # [1, 2, 3, 4, 5, 6, 7]

k = 1
el = 2

for i in range(len(arr)//el):
    print("\nбыло - ", i, arr)
    arr[k], arr[i] = arr[i], arr[k]
    print("стало    ", arr)
    k -= 1

