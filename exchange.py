import locale
import requests

# Configurar el formato de moneda local
locale.setlocale(locale.LC_ALL, '')

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    return data["rates"][target_currency]

def exchange(currency_in: str, currency_out: str, money: float) -> float:
    rate = get_exchange_rate(currency_in, currency_out)
    total = money * rate

    total = locale.currency(total, grouping=True)
    return total
