import requests
from bs4 import BeautifulSoup


COIN_LINKS = {
    "dolar": "cotacao-dolar",
    "euro": "cotacao-euro",
    "libra": "cotacao-libra-esterlina",
    "dolar australiano": "cotacao-dolar-australiano",
    "dolar canadense": "cotacao-dolar-canadense",
    "franco suico": "cotacao-franco-suico",
    "iene japones": "cotacao-iene-japones",
    "peso argentino": "cotacao-peso-argentino",
    "novo sol": "cotacao-novo-sol",
    "boliviano": "cotacao-boliviano",
    "yuan chines": "cotacao-yuan-chines",
    "peso uruguaio": "cotacao-peso-uruguaio",
    "dolar singapura": "cotacao-dolar-singapura",
    "lira turca": "cotacao-lira-turca",
    "dolar hong kong": "cotacao-dolar-hong-kong",
}


def getCoin(id):
    if id < 0 or id >= len(COIN_LINKS):
        return {"error": "Moeda não encontrada"}

    coin_name = list(COIN_LINKS.keys())[id]
    coin_link = COIN_LINKS[coin_name]
    url = f"https://www.remessaonline.com.br/cotacao/{coin_link}"

    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        name = soup.find("h1", class_="style__Title-sc-1a6mtr6-1 dUJopL").get_text().replace(" hoje", "")
        value = soup.find("div", class_="style__Text-sc-1a6mtr6-2 ljisZu").get_text().replace(" Reais", "").replace(",", ".")
        value_float = float(value)
        return {name: value_float}
    except:
        return {"error": "Não foi possível raspar a cotação dessa moeda"}
