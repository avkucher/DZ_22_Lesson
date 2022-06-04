from classes import Request, Shop, Store

if __name__ == '__main__':
    shop = Shop('магазин')
    store = Store('склад')

    store.add('собачки', 5)
    store.add('яблоки', 2)
    store.add('машинки', 8)

    shop.add('печеньки', 1)
    shop.add('яблоки', 2)
    shop.add('машинки', 1)
    shop.add('коробки', 1)
    shop.add('лампочки', 2)

    while True:
        print(f"На складе есть \n {store.get_items()}")
        print(f"В магазине есть \n {shop.get_items()}")

        user_answer = input('Введите строку типа: "Доставить 3 собачки из склад в магазин": \n')
        data_request = Request(user_answer)

        result_store = store.remove(data_request.product, data_request.amount)
        if result_store:
            print(f'Курьер забрал {data_request.amount} {data_request.product} со склада')
            print(f'Курьер везет {data_request.amount} {data_request.product} со склада в магазин')
            result_shop = shop.add(data_request.product, data_request.amount)
            if not result_shop:
                store.add(data_request.product, data_request.amount)
            else:
                print(f'Курьер доставил {data_request.amount} {data_request.product} со склада в магазин')

        print(f'На складе есть: \n {store.get_items()}')
        print(f'В магазине есть: \n {shop.get_items()}')
        user_answer = input('Продолжаем?, Y/N: ')
        if user_answer == "N":
            break

