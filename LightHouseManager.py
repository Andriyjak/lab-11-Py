class LightHouseManager:
    goods = []

    def __init__(self):
        pass

    def sort_by_price(self):
        self.goods.sort(key=lambda good: good.price)

    def find_by_type(self, good_type, price):
        found_goods = []

        for good in self.goods:
            if (good.goods_type == good_type) & (good.price < price):
                found_goods.append(good)

        return found_goods

    def add_toy(self, good):
        self.goods += good

    def print_list(self):
        for good in self.goods:
            print(good)
        print("\n")

