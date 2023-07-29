from exchange import exchange

currency_in = input("Please, give me the orginal currency \n for example USD, MXN, COP \n ->")
currency_out = input("now, give the currency what you wanna get \n ->")
money = float(input("money: "))

total = exchange(currency_in.upper(), currency_out.upper(), money)

print(f"that's equal to {total} {currency_out.upper()}")
