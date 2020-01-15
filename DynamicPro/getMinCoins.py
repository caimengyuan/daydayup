'''
设有n种不同面值的硬币，各硬币的面值存于数组T[1:n]中。现要用这些面值的硬币来找钱，可以实用的各种面值的硬币个数不限。
当只用硬币面值T[1],T[2],…,T[i]时，可找出钱数j的最少硬币个数记为C(i,j)。若只用这些硬币面值，找不出钱数j时，记C(i,j)=∞。
'''

def get_min_coins(coin_combinations, amount_rem):
    coin_list = []
    sorted_coin_combinations = sorted(coin_combinations, reverse=True)

    for coin_val in sorted_coin_combinations:
        coin_count = int(amount_rem/coin_val)
        coin_list += [coin_val]*coin_count
        amount_rem -= coin_val * coin_count
        if amount_rem <= 0:
            break
    if amount_rem != 0:
        print('无法找零')
    else:
        return coin_list

if __name__ == "__main__":
    n = (int)(input("请输入面值个数："))
    coin_combinations = []
    for i in range(n):
        coin_combinations.append((int)(input("面值：")))
    money = (int)(input("需要找的零钱："))
    print(get_min_coins(coin_combinations,money))
