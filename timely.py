#!/usr/bin/env python3
import json
import requests
import os
import pandas as pd
from tqdm import tqdm
from google.cloud import language_v1


# Setup OCP IAM environmental var
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'timely-gcp-iam.json'

def call_gcp(nyt_text):
    nlp_client = language_v1.LanguageServiceClient()
    document = {"content" : nyt_text,
        "type": language_v1.Document.Type.PLAIN_TEXT,
        "language": "en"}

    # Call GCP
    response = nlp_client.analyze_sentiment(document, encoding_type= language_v1.EncodingType.UTF8)

    # Print some starting info
    document_score = response.document_sentiment.score
    print(f"Title + Abstract:\n{nyt_text}")
    print(f'Article sentiment score: {float(response.document_sentiment.score)}')

def main():
    # Read json file and get API key
    with open('times-api.json','r') as api_json_file:
        api_json_rawfile = json.load(api_json_file)
        API_KEY = api_json_rawfile['api-key']

    print(f'API KEY is {API_KEY}')
    limit = 500
    url = f"https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key={API_KEY}&limit={str(limit)}"

    print(f"GET request:\n{url}")

    page = requests.get(url, verify=False)
    

    df_page=pd.json_normalize(page.json()['results'])[['slug_name','byline','section','item_type','material_type_facet','des_facet','org_facet','per_facet','geo_facet','title','abstract','first_published_date']]
    df_page['first_published_date_parsed']=pd.to_datetime(df_page['first_published_date'],format='%Y-%m-%d %H:%M:%S').dt.tz_convert('Europe/London')
    sampled_page = df_page.sample(10)

    #print(sampled_page)

    # Call gcp once
    print('Calling GCP Once')
    call_gcp('Test')

    # Iterate over frames
    for index,row in tqdm(sampled_page.iterrows()):
        print(row.keys())
        raw_text = str(row['title']) + ". "+ str(row['abstract'])
        document_name = row['slug_name']

        #print(f'Document : {document_name}\nText:\n{raw_text}\n\n\n')
        print(f'\n\nCALLING GCP for {document_name}')
        call_gcp(raw_text)
        

if __name__ == "__main__":
    main()