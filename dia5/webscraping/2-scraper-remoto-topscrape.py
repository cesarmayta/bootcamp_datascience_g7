import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = "http://books.toscrape.com"

response = requests.get(URL)

if response.status_code == 200:
    data = response.content
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article',class_='product_pod')
    print(books[0])
    print(f'total de libros : {len(books)}')