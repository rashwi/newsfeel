"""Definition for a single 'Article'
Using to standardize reddit posts, news articles etc."""
from dataclasses import dataclass
from newsfeel import sentiment

@dataclass
class Article:
    title: str
    content: str

    def __str__(self):
        if self.title:
            return f'{self.title}. {self.content}'
        else:
            return self.content

    def contains(self, test_str, ignorecase=False):
        if ignorecase:
            return test_str.lower() in str(self).lower()

        return test_str in str(self)

    def get_sentiment(self):
        return sentiment.evaluate_sentiment(str(self))


def print_articles(article_list):
    """Print utility to print out a list of articles"""
    for index, article in enumerate(article_list):
        print(f"{index + 1}. {article}")


def filter(article_list, keyword:str, ignorecase=False):
    """Filters a list of articles by a keyword based on if the keyword appears in the title or body of the article"""

    return [article for article in article_list if article.contains(keyword, ignorecase)]

def concatenate(article_list) -> str:
    return ' '.join([str(article) for article in article_list])

