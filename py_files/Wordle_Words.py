# Robert Jones
# 8/16/22
# Scraping a website to download wordle words

import requests # For DLing HTML
from bs4 import BeautifulSoup as bs # To work with HTML
 

class WordleWords:

    # function to parse website and return wordle words
    def get_words():
        # Website with all 5 letter words
        URL = 'https://raw.githubusercontent.com/tabatkins/wordle-list/main/words'
        words = str(bs(requests.get(URL).text, 'html.parser'))
        words = words.split()
        return words


