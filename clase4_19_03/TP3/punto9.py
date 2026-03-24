import requests

# Monto en pesos argentinos
pesos = float(input("Ingrese la cantidad de pesos argentinos: "))

# Tasas fijas
usd_rate = 80.5
brl_rate = 14.1
eur_rate = 69.5

# Conversiones
usd = pesos / usd_rate
brl = pesos / brl_rate
eur = pesos / eur_rate


print(f"Usted tiene ${pesos} pesos argentinos, los cuales se convierten en:")
print(f"- U${usd:.2f} dólares.")
print(f"- R${brl:.2f} reales.")
print(f"- €{eur:.2f} euros.")

# URL de la API ExchangeRate.host (sin API key)
url = "https://open.er-api.com/v6/latest/ARS"

# Hacemos la petición
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Obtenemos las tasas de cambio
    usd_rate = data["rates"]["USD"]
    brl_rate = data["rates"]["BRL"]
    eur_rate = data["rates"]["EUR"]

    # Conversiones
    usd = pesos * usd_rate
    brl = pesos * brl_rate
    eur = pesos * eur_rate

    print(f"Usted tiene ${pesos} pesos argentinos, los cuales se convierten en:")
    print(f"- U${usd:.2f} dólares.")
    print(f"- R${brl:.2f} reales.")
    print(f"- €{eur:.2f} euros.")
else:
    print("Error al obtener los datos de la API.")