import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time
import json
from Telegram import *

with open('data.json') as f:
    data = json.load(f)

urls = [item['url'] for item in data]
max_values = [item['max_values'] for item in data]
check_currencies = ['CASH', 'Moeda de RMT']
time_between_scrapes = 5; #time in seconds

def scrape_url(url, values):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'nova-sale-table'})
    title = soup.find_all('h2')[1].text
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        valor = int(cols[3].text.strip().replace(',', '').replace('c', '').replace('z', ''))
        venda_por = cols[5].text.strip()
        max_value_printed = False
        for check_currency in check_currencies:
            if check_currency in venda_por and valor < values[check_currency] and not max_value_printed:
                send_to_telegram(title)
                send_to_telegram(f'Valor: {valor}, Venda Por: {venda_por}')
                send_to_telegram(f"Value is less than the specified maximum of {values[check_currency]} for {check_currency}.")
                print(title, flush=True)
                print(f'Valor: {valor}, Venda Por: {venda_por}', flush=True)
                print(f"Value is less than the specified maximum of {values[check_currency]} for {check_currency}.", flush=True)
                max_value_printed = True
                
while True:
    time.sleep(time_between_scrapes)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(scrape_url, url, values) for url, values in zip(urls, max_values)]
        for future in concurrent.futures.as_completed(futures):
            if future.exception() is not None:
                print(f"Exception raised during scraping: {future.exception()}", flush=True)
