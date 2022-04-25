import requests
from bs4 import BeautifulSoup

pagina=requests.get("https://www.expertoanimal.com/animales-extintos-en-mexico-25704.html")
sopa= BeautifulSoup(pagina.content, 'html.parser')
animales=sopa.find_all('h2', class_="titulo titulo--h2 titulo--apartado" )
archivo=open('lista de animales extintos en mexico.txt','w')
for i in animales:
	archivo.write(str(i.text))
archivo.close()