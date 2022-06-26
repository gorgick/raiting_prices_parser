import requests
from bs4 import BeautifulSoup
import csv
from time import sleep


def get_html(url):
    sleep(3)
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('21vek.csv', 'a') as f:
        order = ['name', 'price']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find('ul', class_='b-result').find_all('li')
    for el in res:
        try:
            name = el.find('span', class_='result__name').text
        except:
            name = ''
        try:
            price = el.find('span', class_='g-price result__price cr-price__in').text.split(',')[0].split(' ')
            price = ''.join(price)
        except:
            price = ''
        data = {'name': name, 'price': price}
        write_csv(data)


def main():
    pattern = 'https://www.21vek.by/grass_cuts/page:{}/'
    for i in range(1, 7):
        url = pattern.format(str(i))
        get_data(get_html(url))
