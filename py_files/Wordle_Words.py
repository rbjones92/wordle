# Robert Jones
# 8.10.22
# Wordle Words


class WordleWords:

    def get_words():

        with open('C:/Users/Bob/Desktop/SpringBoard/Python_Projects/Wordle/words/wordle_words.txt') as f:
            words = f.read().splitlines()
        return words

