# `add`(<название>, <количество>)  - увеличивает запас items
#
# `remove`(<название>, <количество>) - уменьшает запас items
#
# `get_free_space()` - вернуть количество свободных мест
#
# `get_items()` - возвращает сожержание склада в словаре {товар: количество}
#
# `get_unique_items_count()` - возвращает количество уника
...
from abc import abstractmethod

class Storage:
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        if self.get_free_space() > 0:
            if self.get_free_space() >= count:
                if name in self.items.keys():
                    self.items[name] += count
                    print(f'Товар {name} добавлен')
                else:
                    self.items[name] = count
                    print(f'Товар {name} добавлен')
                return True
            else:
                 print(f'Не хватает места для хранения. Возможен прием в количестве {self.get_free_space()} шт.')
        else:
            print(f'Нет места для хранения')
        return False


    def remove(self, name, count):
        if name in self.items.keys():
            if self.items[name] >= count:
                print('Есть нужное количество.')
                self.items[name] -= count
                return True
            else:
                print(f'Нет такого количества на складе.Всего - {self.items[name]} шт.')

        else:
            print(f'Товара {name} на складе нет')
            return False
        return False

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        self.items = {}
        self.capacity = 20
        self.unit_limit = 5

    def add(self, name, count):
        if self.get_unique_items_count() <= self.unit_limit:
            super().add(name, count)
            return True
        else:
            print(f'Kоличество уникальных товаров не может быть больше {self.unit_limit} шт.')
            return False

class Request:
    def __init__(self, req_input):
        data = req_input.split(' ')
        self.from_ = data[4]
        self.to = data[6]
        self.amount = int(data[1])
        self.product = data[2]

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'








