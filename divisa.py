from exchange import exchange

def message(total, value):
    print("-" * 50)

    if total == False:
        print("error whit the currency")
    else:
        print(f"that's equal to {total} {value.upper()}")
    
    print("-" * 50)

def main():
    while True:
        currency_in = input("Please, give me the orginal currency \n -> ")
        currency_out = input("now, give the currency what you wanna get \n -> ")
        money = float(input("money: "))

        total = exchange(currency_in.upper(), currency_out.upper(), money)

        message(total, currency_out)

        exit = input("you want to do any other transaction? \ny: yes / n: ")
        if exit == "n":
            break

        print("/" * 50)

main()