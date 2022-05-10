from itertools import combinations
class Potter:
    def pick_combination(self, basket, books_num):
        return list(set(basket))[:books_num]
    def remove_books_from_basket(self, basket, books):
        for b in books:
            basket.remove(b)
        return basket
    def discountprice(self, basket):
        if len(set(basket)) != len(basket):
            print('Error: only accept unique basket.')
        discount = {0:1, 1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}
        return 8*len(basket)*discount[len(basket)]
    def price(self, basket):
        minprice = 8*len(basket)
        if len(set(basket)) == len(basket):
            # no duplicate books
            return self.discountprice(basket)
        else:
            max_combine = len(set(basket))
            for i in range(max_combine, 1, -1):
                comb  = self.pick_combination(basket, i)
                # print(comb)
                combprice = self.discountprice(comb)
                if combprice + 8*(len(basket) - i)*0.75 > minprice:
                    continue
                tmp_pack = basket.copy()
                combprice += self.price(self.remove_books_from_basket(tmp_pack, comb))
                if combprice < minprice:
                    # print(minprice)
                    minprice = combprice
        return minprice
        