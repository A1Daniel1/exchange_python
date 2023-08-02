from exchange import exchange

def message(total, value):
    print("-" * 50)

    if total == False:
        print("error whit the currency")
    else:
        print(f"that's equal to {total} {value.upper()}")

def main():
    currency_in = input("Please, give me the orginal currency \n -> ")
    currency_out = input("now, give the currency what you wanna get \n -> ")
    money = float(input("money: "))

    total = exchange(currency_in.upper(), currency_out.upper(), money)

    message(total, currency_out)

main()