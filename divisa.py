import requests
import locale

# Configurar el formato de moneda local
locale.setlocale(locale.LC_ALL, '')

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]

moneda = int(input("Seleccione conversión \nUSD -> COP: 0 \nCOP -> USD: 1 \n"))
cantidad = float(input("Cantidad: "))

resultado = 0

if moneda == 0:
    rate = get_exchange_rate("USD", "COP")
    resultado = cantidad * rate
elif moneda == 1:
    rate = get_exchange_rate("COP", "USD")
    resultado = cantidad * rate

# Formatear el resultado a la moneda local del sistema
resultado_formateado = locale.currency(resultado, grouping=True)

print(f"La cantidad de dinero es {resultado_formateado}")
