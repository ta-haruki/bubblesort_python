import random


def bubble_sort_kojun(data, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]
            print(data)
    return data


def bubble_sort_shojun(data, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if data[j - 1] < data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]
            print(data)
    return data


def main():
    print('ソートしたい要素数を自然数値で入力してください。>>')
    sort_count = int(input())
    print('ソート方法を入力してください。1:昇順, 2:降順 >>')
    order = int(input())

    if order == 1:
        initial_list = random.choices(range(sort_count), k=sort_count)
        print("ランダムに生成された初期リスト->", initial_list)
        result = bubble_sort_shojun(initial_list, len(initial_list))
    else:
        initial_list = random.choices(range(sort_count), k=sort_count)
        print("ランダムに生成された初期リスト->", initial_list)
        result = bubble_sort_kojun(initial_list, len(initial_list))


if __name__ == '__main__':
    main()
