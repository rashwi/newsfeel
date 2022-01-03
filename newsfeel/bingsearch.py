#!/usr/bin/env python3
"""Module to hold wrapper functions for calling the Bing Search API"""
import os
import json
from pprint import pprint
import requests
import pandas as pd
from newsfeel import articles



# Globals
API_ENDPOINT = "https://api.bing.microsoft.com/v7.0/news/search"
try:
    API_KEY = os.environ['BING_API_KEY']
except KeyError:
    raise ValueError("Expecting BING_API_KEY variable set in the environment. Cannot continue without it. Please check the environment settings.")

"""
# Read json file and get API key
with open(os.path.join('iam', 'bing-search-iam.json'), 'r') as api_json_file:
    API_PARAMS = json.load(api_json_file)
    API_KEY = API_PARAMS['key1']
"""

def find_news_about(query: str):
    #params = {'q' : query, 'textDecorations': True, "textFormat": "HTML"}
    params = {'q' : query}
    headers = {'Ocp-Apim-Subscription-Key': API_KEY}
    # Call the API
    response = requests.get(API_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()
    
    fields_to_extract = ['name', 'description']
    results_df = pd.json_normalize(response.json()['value'])[fields_to_extract]


    article_list = []
    for _, result in results_df.iterrows():
        article_list.append(articles.Article(result['name'], result['description']))

    return article_list


def main():
    results = find_news_about('Eric Adams')

if __name__ == '__main__':
    main()