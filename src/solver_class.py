class Solver:
    def my_max(self, list, shift):
        max = 0
        max_index = 0
        # print("my_max list: " + str(list) + " shift: " + str(shift))
        for i in range(len(list)):
            if (list[i] > max):
                max = list[i]
                max_index = i
        return max_index + shift

    def max_plus_func(self, list):
        isdecreasing = True
        max = 0
        max_index = 0
        last_index_in_decreasing = 0
        for i in range(len(list)):
            if (list[i] > max):
                max = list[i]
                max_index = i
            if (len(list) > i + 1 and isdecreasing and list[i + 1] <= list[i]):
                isdecreasing = True
            if (len(list) > i + 1 and isdecreasing and (list[i + 1] > list[i])):
                last_index_in_decreasing = i + 1
                isdecreasing = False
            if (isdecreasing and i == len(list) - 1):
                last_index_in_decreasing = i
                isdecreasing = False
            # print("I: " + str(i) + " Max: " + str(max) + " MaxIndex: " + str(max_index) + " lastindex: " + str(last_index_in_decreasing) + " isDEc: " + str(isdecreasing) + "\n")
        if (max_index != 0):
            return max_index
        else:
            return self.my_max(self, list[last_index_in_decreasing:], last_index_in_decreasing)
    def collecting_shares(self, share_list):
        money = 0
        number_of_shares = 0
        max_index = self.max_plus_func(self,share_list)
        max = share_list[max_index]
        for i in range(len(share_list)):
            if (share_list[i] < max):
                number_of_shares += 1
                money -= share_list[i]
            if (i == max_index):
                money += number_of_shares * max
                number_of_shares = 0
                # print("Share list: " + str(share_list[max_index:]))
                max_index += self.max_plus_func(self,share_list[max_index:])
                max = share_list[max_index]
            # print("I: " + str(i) + " Cena akcji " + str(share_list[i]) + " Max: " + str(max) + " MaxIndex: " + str(max_index) + " Money: " + str(money) + " number of shares: " + str(number_of_shares) + "\n")
        return money
