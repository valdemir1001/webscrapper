import requests
from bs4 import BeautifulSoup

# a variável site recebe o conteudo da requisição http do site
site = requests.get('https://g1.globo.com/previsao-do-tempo/rj/rio-de-janeiro.ghtml').content

# A variavel soup baixa do site html
soup = BeautifulSoup(site, 'html.parser')

#No print é mostrado a transformação do html.
#print(soup.prettify())

temperatura = soup.find("span", class_="menu-item-title")
print(temperatura.string)
#print(soup.find('temperatura'))