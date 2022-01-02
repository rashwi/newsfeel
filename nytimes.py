"""Module for functions related to interaction with the NY Times API"""
import json
import os.path
import requests
import pandas as pd

# Read json file and get API key
with open(os.path.join('iam', 'times-api.json'), 'r') as api_json_file:
    API_KEY = json.load(api_json_file)['api-key']

def get_articles(word_limit: int = 100, max_articles: int = 100):
    """function to get articles from the NYTimes API.

    Arguments:
        word_limit [optional]: Max length for request response. Defaults to 100
        max_articles [optional]: Max number of articles to request. Defaults to 100

    Returns:
        Pandas dataframe generator?

    """
    times_api_base = "https://api.nytimes.com/svc/news/v3/content/all/all.json"
    url = f"{times_api_base}?api-key={API_KEY}&limit={str(word_limit)}"

    print(f"GET request:\n{url}")

    page = requests.get(url, verify=False)

    fields_to_extract = ['slug_name', 'byline', 'section', 'item_type',
                         'material_type_facet', 'des_facet', 'org_facet',
                         'per_facet', 'geo_facet', 'title', 'abstract',
                         'first_published_date']

    df_page = pd.json_normalize(page.json()['results'])[fields_to_extract]

    sampled_page = df_page.sample(max_articles)

    return sampled_page.iterrows()
