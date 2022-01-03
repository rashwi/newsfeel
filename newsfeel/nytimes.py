"""Module for functions related to interaction with the NY Times API"""
import json
import os
import requests
import pandas as pd
from dataclasses import dataclass
from typing import List
from newsfeel import articles

# get API key from the environment
try:
    API_KEY = os.environ['NYTIMES_API_KEY']
except KeyError:
    raise ValueError("Expecting 'NYTIMES_API_KEY' to be set in the environment. Cannot continue without it. Please check environment settings and run again.")

def get_article_list(word_limit=500, max_articles=0) -> List[articles.Article]:
    """function to get articles from the NYTimes API.

    Arguments:
        word_limit [optional]: Max length for request response. Defaults to 100
        max_articles [optional]: Max number of articles to request. Defaults to 100

    Returns:
        List of Article objects

    """
    times_api_base = "https://api.nytimes.com/svc/news/v3/content/all/all.json"
    url = f"{times_api_base}?api-key={API_KEY}&limit={str(word_limit)}"

    print(f"GET request:\n{url}")

    page = requests.get(url, verify=False)

    fields_to_extract = ['title', 'abstract']

    results_df = pd.json_normalize(page.json()['results'])[fields_to_extract]

    if max_articles:
        # sample based on arguments
        results_df = results_df.sample(max_articles)

    # Iterate and convert to Article data type
    article_list = []
    for _, df_entry in results_df.iterrows():
        article_list.append(articles.Article(df_entry['title'], df_entry['abstract']))
    return article_list

def find_news_about(keyword:str, ignorecase=False):
    """Searches the NYTimes news page for articles with select keyword in the title of abstract"""

    return articles.filter(get_article_list(), keyword, ignorecase)

def main():
    """Main Driver for nytimes.py. Used for testing purposes only"""

    article_list = find_news_about('Eric Adams')

    concatenated_news = ' '.join([str(article) for article in article_list])

    print('Articles found:')
    articles.print_articles(article_list)

if __name__ == "__main__":
    main()