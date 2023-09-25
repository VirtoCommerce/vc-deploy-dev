import datetime
import os
import requests
from jinja2 import Template
import time
import pyodbc

def get_pagespeed_insights_data(url, locale, strategy):
    api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    params = {
        'url': url,
        'strategy': strategy,
        'locale': locale
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data

def generate_document(url, locale, strategy, data):
    document = {
        'url': url,
        'locale': locale,
        'strategy': strategy,
        'datetime': datetime.datetime.now(),
        'performance_score': data['lighthouseResult']['categories']['performance']['score'],
        'first_contentful_paint': data['lighthouseResult']['audits']['first-contentful-paint']['numericValue'],
        'largest_contentful_paint': data['lighthouseResult']['audits']['largest-contentful-paint']['numericValue'],
        'first_meaningful_paint': data['lighthouseResult']['audits']['first-meaningful-paint']['numericValue'],
        'speed_index': data['lighthouseResult']['audits']['speed-index']['numericValue'],
        'server_response_time': data['lighthouseResult']['audits']['server-response-time']['numericValue'],
        'cumulative_layout_shift': data['lighthouseResult']['audits']['cumulative-layout-shift']['numericValue'],
        'total_blocking_time': data['lighthouseResult']['audits']['total-blocking-time']['numericValue']
    }
    return document

# variable for db
server = os.environ.get('serverDB')
database = os.environ.get('nameDB')
username = os.environ.get('usernameDB')
password = os.environ.get('passwordDB')

# connection string
conn_str = f'Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# create connection
conn = pyodbc.connect(conn_str)

# create cursor
cursor = conn.cursor()

# get urls from file
with open('urls.txt', 'r') as file:
    urls = file.readlines()

locales = ["en-US", "nl-NL", "ru-RU"]

for url in urls:
    url = url.strip()  # remove unsupported symbol
    
    for locale in locales:
        for strategy in ['desktop', 'mobile']:  # select strategy
            data = get_pagespeed_insights_data(url, locale, strategy)
            document = generate_document(url, locale, strategy, data)

            # save in DB
            query = """INSERT INTO pagespeed_collection (url, locale, strategy, datetime, performance_score, first_contentful_paint, first_meaningful_paint, speed_index, server_response_time, total_blocking_time, largest_contentful_paint, cumulative_layout_shift) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            values = (
                document['url'], document['locale'], document['strategy'], document['datetime'],
                document['performance_score'], document['first_contentful_paint'], document['first_meaningful_paint'],
                document['speed_index'], document['server_response_time'], document['total_blocking_time'],
                document['largest_contentful_paint'], document['cumulative_layout_shift']
            )
            cursor.execute(query, values)
            conn.commit()

            print(f"Result for {url} with local {locale} and {strategy} saved to DB")
            time.sleep(10)

# close connection
cursor.close()
conn.close()
