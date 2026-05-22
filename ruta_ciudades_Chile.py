import requests

API_KEY = "80a3e251-d42c-44aa-a89f-d4ff13692f8b"

while True:

    origen = input("Ciudad de Origen (q para salir): ")

    if origen == "q":
        print("Programa terminado")
        break

    destino = input("Ciudad de Destino (q para salir): ")

    if destino == "q":
        print("Programa terminado")
        break

    # origen
    url1 = "https://graphhopper.com/api/1/geocode?q=" + origen + "&limit=1&key=" + API_KEY
    datos1 = requests.get(url1).json()

    # destino
    url2 = "https://graphhopper.com/api/1/geocode?q=" + destino + "&limit=1&key=" + API_KEY
    datos2 = requests.get(url2).json()

    if len(datos1["hits"]) == 0 or len(datos2["hits"]) == 0:
        print("Ciudad no encontrada")
        continue

    lat1 = datos1["hits"][0]["point"]["lat"]
    lon1 = datos1["hits"][0]["point"]["lng"]

    lat2 = datos2["hits"][0]["point"]["lat"]
    lon2 = datos2["hits"][0]["point"]["lng"]

    # pedir ruta
    url_ruta = "https://graphhopper.com/api/1/route?point=" + str(lat1) + "," + str(lon1) + \
               "&point=" + str(lat2) + "," + str(lon2) + \
               "&vehicle=car&locale=es&key=" + API_KEY

    ruta = requests.get(url_ruta).json()

    path = ruta["paths"][0]

    distancia = path["distance"] / 1000
    tiempo = path["time"] / 1000

    horas = tiempo // 3600
    minutos = (tiempo % 3600) // 60
    segundos = tiempo % 60

    combustible = distancia / 12

    print("\nRESULTADO")
    print("Origen:", origen)
    print("Destino:", destino)
    print("Distancia:", round(distancia, 2), "km")
    print("Tiempo:", int(horas), "h", int(minutos), "m", int(segundos), "s")
    print("Combustible:", round(combustible, 2), "litros")

    print("\nPasos:")
    for i in path["instructions"]:
        print("-", i["text"])

    print("\n")