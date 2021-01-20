def simple_collecting(share_list):
    money = 0
    number_of_shares = 0
    max_var = max(share_list)
    while(True):
        ##print("I: " + str(0) + " Tabela " + str(share_list) + " Max: " + str(max_var) + " MaxIndex: "
         ##     + " Money: " + str(money) + " number of shares: " + str(number_of_shares) + "\n")
        if(share_list[0] < max_var):
            number_of_shares += 1
            money -= share_list[0]
            share_list.pop(0)
        else:
            money += number_of_shares * max_var
            number_of_shares = 0
            share_list.pop(0)
            if(not share_list):
                return money
            max_var = max(share_list)
