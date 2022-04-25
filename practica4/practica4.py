import requests;
import json;
ts="1"
private_key="0383eeb9a68b181672acd9c91335604a9620d370"
public_key="76d64bea87949fabe7fcb3971df4d4ca"
hashed="7fb6fb5456195ab89cac4824ed05b24d"
url= "https://gateway.marvel.com:443/v1/public/characters?ts="+ts+"&apikey="+public_key+"&hash="+hashed
repuesta= requests.get(url)
personajes=[]
if repuesta.status_code==200:
	respuestaJ = json.loads(repuesta.text)
	for i in respuestaJ["data"]["results"]:
		nombre= i["name"]
		descripcion =i["description"]
		series=i["series"]["available"]
		comics=i["comics"]["available"]
		d={"nombre":nombre,"descripcion":descripcion,"series":series,"comics":comics}
		personajes.append(d)
for i in range(len(personajes)):
	print(personajes[i])