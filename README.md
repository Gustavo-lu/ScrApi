
# ScrAPI 🕷️

Esse projeto tem como intuito fazer a utilização da raspagem de dados da web e enviar para uma Api Rest.


## Documentação da API

#### Ao acionar essa rota você extrai o valor da cotação de uma moeda

```http
  GET /scrapi/coin/{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `integer` | **Obrigatório**. O ID da Moeda desejada |

#### 

#### Valores que podem ser enviados nos parâmetros da requisição

    0:Dólar
    1:Euro
    2:Libra Esterlina 
    3:Dólar Australiano 
    4:Dólar Canadense 
    5:Franco Suíço 
    6:Iene 
    7:Peso Argentino 
    8:Novo Sol 
    9:Boliviano 
    10:Yuan Chinês 
    11:Peso Uruguaio
    12:Dólar de Singapura 
    13:Lira Turca 
    14:Dólar de Hong-Kong
### Retorno da API
```bash
{
  "Dólar americano": 5.14
}
```
## Instalação
Para executar esse projeto será necessário a instalação das bibliotecas:
```bash
python install requeriments.txt
```
### Executando inicialização o projeto
No diretório da aplicação execute esse comando em seu terminal:
```bash
python main.py
```
Em seguida é só consumir 😉



## LinkedIn

www.linkedin.com/in/gustavo-lu-6b9236217
