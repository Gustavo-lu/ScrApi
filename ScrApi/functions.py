import requests
from bs4 import BeautifulSoup
from list_ import coin


def getCoin(id):

        totalindex = (len(coin)-1)
        
        if id>totalindex:
                return({"error":"Moeda não encontrada"})
        elif id<0:
                return({"error":"Moeda não encontrada"})
        try:
                Cotalink=coin[id]
                url='https://www.remessaonline.com.br/cotacao/'+Cotalink+''
                page = requests.get(url)
                soup = BeautifulSoup(page.text, 'html.parser')
                htmlNamecoin=soup.find_all('h1',class_ = "style__Title-sc-1a6mtr6-1 dUJopL")[0].get_text()
                name=htmlNamecoin.replace(" hoje",'')
                htmlpage=soup.find_all('div',class_ = "style__Text-sc-1a6mtr6-2 ljisZu")[0].get_text()
                Value=htmlpage.replace(' Reais','')
                CoinReplaceDot = Value.replace(',','.')
                CoinToFloat=float(CoinReplaceDot) 
                return({name:CoinToFloat})
        except:
                return({"Error":"Não foi possível raspar a cotação dessa moeda"})

