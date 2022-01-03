#!/usr/bin/env python3
""": Media sentiment analysis through nytimes, bing news sources and more"""
from newsfeel import sentiment, articles
from newsfeel import nytimes, bingsearch
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('keyword', help='Keyword to search on', action='store')
    parser.add_argument('-i', '--ignore-case', help='Ignore case when searching for keyword', dest='ignorecase', action='store_true', default=False)

    return parser.parse_args()

def main():
    """Main Driver for py. Given as an example for testing only"""

    options = parse_args()
    keyword = options.keyword

    nytimes_articles = nytimes.find_news_about(keyword, options.ignorecase)
    if nytimes_articles:
        nytimes_sentiment, _ = sentiment.evaluate_sentiment(articles.concatenate(nytimes_articles))
        print(f"NYT sentiment score for headlines related to {keyword}: {nytimes_sentiment*100:.2f}%")
        print(f"NYT Headlines:")

    articles.print_articles(nytimes_articles)

    bing_results = bingsearch.find_news_about(keyword)
    if bing_results:
        bing_sentiment, _ = sentiment.evaluate_sentiment(articles.concatenate(bing_results))
        print(f"\n\nBing sentiment score for headlines related to {keyword}: {bing_sentiment*100:.2f}%")
        print(f"Bing Headlines:")
        articles.print_articles(bing_results)



if __name__ == "__main__":
    main()
