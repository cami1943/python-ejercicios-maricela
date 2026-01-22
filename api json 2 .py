import urllib.request
import urllib.parse
import json
import unicodedata   # <--- necesario

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address = input("Enter location: ").strip()
    if len(address) < 1:
        break

    # Quitar acentos para que la API entienda la dirección
    address = unicodedata.normalize('NFKD', address).encode('ASCII', 'ignore').decode('utf-8')

    parms = {"q": address, "key": 42}
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)

    data = urllib.request.urlopen(url).read().decode()
    print("Retrieved", len(data), "characters")

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    if "features" not in js or len(js["features"]) == 0:
        print("❌ No hubo resultados.")
        continue

    props = js["features"][0]["properties"]

    pc = props.get("plus_code")
    if isinstance(pc, dict):
        pc = pc.get("global_code") or pc.get("compound_code")

    print("✔️ Plus code encontrado:", pc)
