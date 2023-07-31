import locale
import requests

# Configurar el formato de moneda local
locale.setlocale(locale.LC_ALL, '')

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)

    if response.status_code == 404:
        return False
    else:
        data = response.json()

        if target_currency not in data["rates"]:
            return False
        else:
            return data["rates"][target_currency]

def exchange(currency_in: str, currency_out: str, money: float) -> float:
    rate = get_exchange_rate(currency_in, currency_out)

    if rate == False:
        return False
    else: 
        total = money * rate
        total = locale.currency(total, grouping=True)
        return total
