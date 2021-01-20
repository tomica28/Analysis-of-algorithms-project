from random import seed
from random import randint

class Generator:
    ## p - prawdopodobienstwo ze kolejny element listy jest wiekszy od poprzedniego
    def generate(self, number_of_shares, lower_price_limit, upper_price_limit, p):
        seed()
        list = []
        for k in range(number_of_shares):
            if(k == 0):
                list.append(randint(lower_price_limit, upper_price_limit))
                continue
            bound = int(p * 100)
            pro = randint(0,100)
            if (pro < bound):
                list.append(randint(list[k-1], upper_price_limit))
            else:
                list.append(randint(lower_price_limit, list[k-1]))
        return list
    def generate_decreasing(self,number_of_shares,lower_price_limit, upper_price_limit, p):
        seed()
        list = []
        for k in range(number_of_shares):
            if (k % 2 == 0):
                if(number_of_shares < upper_price_limit):
                    list.append(number_of_shares+lower_price_limit-k)
                elif(upper_price_limit-k < lower_price_limit):
                    list.append(lower_price_limit)
                else:
                    list.append(upper_price_limit-k)
            else:
                bound = int(p * 100)
                pro = randint(0, 100)
                if (pro < bound):
                    list.append(randint(list[k - 1], upper_price_limit))
                else:
                    list.append(randint(lower_price_limit, list[k - 1]))
        return list
    def hardest_test(self, number_of_shares, rand_parametr):
        list = []
        seed()
        bound = randint(number_of_shares, number_of_shares+rand_parametr)
        const_var = bound - number_of_shares
        for k in range(number_of_shares):
            if(k % 2 == 0):
                list.append(bound - k)
            else:
                list.append(const_var)
        return list