from classes import Shop, Store, Request

if __name__ == '__main__':
    shop = Shop()
    store = Store()

    store.add('собачки', 5)
    store.add('яблоко', 2)
    store.add('машинки', 8)

    print('Наличие на складе:')
    print(store.get_items())


    user_answer = input('Введите запрос, например: "Доставить 3 собачки из склад в магазин": \n')
    data_request = Request(user_answer)

    result_store = store.remove(data_request.product, data_request.amount)
    if result_store:
        print(f'Курьер забрал {data_request.amount} {data_request.product} со склада')
        print(f'Курьер везет {data_request.amount} {data_request.product} со склада в магазин')
        result_shop = shop.add(data_request.product, data_request.amount)
        if not result_shop:
            store.add(data_request.product, data_request.amount)
        else:
            print(f'Курьер доставил {data_request.amount} {data_request.product} в магазин')


    print('Наличие на складе:')
    print(store.get_items())

    print('Наличие в магазине:')
    print(shop.get_items())

