# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

from menu import menu
from requests import get
menu('114', 'Acessando Site')

try:
    inicioURL = "https://www."
    userURL = str(input(f'\33[1:33mInforme a URL: {inicioURL}'))
    site = inicioURL + userURL
    get(site)
except:
    print("\33[1:31mSite está indisponível.")
else:
    print("\33[1:32mSite está disponível.")

