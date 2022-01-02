#!/usr/bin/env python3
"""timely.py : Media sentiment analysis through nytimes"""
import sentiment
import nytimes

def main():
    """Main Driver for timely.py"""
    for _, row in nytimes.get_articles(max_articles=5):
        raw_text = str(row['title']) + ". " + str(row['abstract'])
        sentiment_score, sentiment_magnitude = sentiment.evaluate_sentiment(raw_text)

        print(f'Article Text:\n{raw_text}\nSentiment: ' +\
              f'{sentiment_score:.2f}, {sentiment_magnitude:.2f}')


if __name__ == "__main__":
    main()
