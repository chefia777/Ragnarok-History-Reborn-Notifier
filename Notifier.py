import requests
from bs4 import BeautifulSoup
import time
from Telegram import *

def scrape_data():
    # URL of the page to scrape
    url = 'https://historyreborn.net/?module=vending&action=viewshop&id=3220'

    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', class_='horizontal-table')
    rows = table.find_all('tr')[1:]
    data = []

    for row in rows:
        columns = row.find_all('td')
        item_name = columns[1].find('a').text.strip()
        price = columns[9].text.strip().replace(',', '')
        quantity = columns[10].text.strip()
        data.append((item_name, price, quantity))

    try:
        with open('data.txt', 'r') as file:
            previous_data = [tuple(line.strip().split(',')) for line in file.readlines()]
    except FileNotFoundError:
        previous_data = []

    added_items = [item for item in data if item not in previous_data]
    removed_items = [item for item in previous_data if item not in data]

    if added_items or removed_items:
        print("Changes detected!")

        with open('data.txt', 'w') as file:
            for item in data:
                file.write(','.join(item) + '\n')

        if added_items:
            send_to_telegram("Added items:")
            print("Added items:")
            for item in added_items:
                send_to_telegram(f"Item: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")
                print(f"Item: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")

        if removed_items:
            send_to_telegram("Removed items:")
            print("Removed items:")
            for item in removed_items:
                send_to_telegram(f"Item: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")
                print(f"Item: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")
    else:
        print("No changes detected.")

while True:
    scrape_data()
    time.sleep(3)
