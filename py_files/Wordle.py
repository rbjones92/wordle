# Robert Jones
# 8.10.22
# Wordle Solver

import re
import random
from termcolor import colored
import Wordle_Words

words = Wordle_Words.WordleWords.get_words()
word = random.choice(words)
guess = random.choice(words)

counter = 1
counter_list = []

class Wordle_Solver:

    def __init__(self,words,guess,word):
        self.words = words
        self.guess = guess
        self.word = word
        self.mapped = Wordle_Solver.mapper(self,guess)

        print(f'{word} is our word \n{guess} is our guess')


    def mapper(self,guess):

        green = []
        yellow = []
        grey = []

        for i in range(0,len(word),1):
            if word[i] == guess[i]:
                green.append(word[i])
                green.append(i)
                green.append('green')


            if guess[i] in word and word[i] != guess[i]:
                yellow.append(guess[i])
                yellow.append(i)
                yellow.append('yellow')


            if guess[i] not in word:
                grey.append(guess[i])
                grey.append(i)
                grey.append('grey')

        merged = green+yellow+grey

        return merged


    def colorize(self):

        merged = self.mapped

        for y in range(0,5,1):
            if y in merged[1::3]:
                ind = merged.index(y)
                print(colored(merged[ind-1],merged[ind+1]),end='')
        print('\n')


    def reduction(self):
        global counter
        mapped = self.mapped
        words = self.words

        def grey(words):

            grey_letters = []
            grey_words = []
            for g in range(2,len(mapped),3):
                if mapped[g] == 'grey':
                    grey_letters.append(mapped[g-1])
                    grey_letters.append(mapped[g-2])

            grey_letters = grey_letters[1::2]
            grey_letters = "".join(grey_letters)

            # Find all words with grey letters in them
            for w in words:
                if set(grey_letters).intersection(w):
                    grey_words.append(w)
                    
            # Eliminate those words for word list 
            grey_words = list(set(grey_words).symmetric_difference(words))

            return grey_words        

        def green(words):
            
            green_letters = []
            green_words = []
            for g in range(2,len(mapped),3):
                if mapped[g] == 'green':
                    green_letters.append(mapped[g-1])
                    green_letters.append(mapped[g-2])

            regex_list = [['a-z'],['a-z'],['a-z'],['a-z'],['a-z']]

            for i in range(1,len(green_letters),2):
                regex_list[green_letters[i-1]] = green_letters[i]

            regex_list = ''.join(str(regex_list).split(','))
            regex_list = regex_list.replace(" ","")
            regex_list = regex_list.replace("'","")
            regex_list = regex_list[1:-1]

            pattern = re.compile(regex_list)
            matches = re.findall(pattern,str(words))

            for match in matches:
                green_words.append(match)

            return green_words


        def yellow(words):
            yellow_letters = []
            yellow_words = []
            for g in range(2,len(mapped),3):
                if mapped[g] == 'yellow':
                    yellow_letters.append(mapped[g-1])
                    yellow_letters.append(mapped[g-2])

            for i in range(0,len(words),1):
                for l in range(1,len(yellow_letters),2):
                    if yellow_letters[l] in words[i] and words[i][yellow_letters[l-1]] != yellow_letters[l]:
                        yellow_words.append(words[i])

            return yellow_words 
            

        if 'grey' in mapped:
            words = grey(words)

        if 'green' in mapped:
            words = green(words)

        if 'yellow' in mapped:
            words = yellow(words)

        # print(f'{words} are possible choices')

        guess = random.choice(words)

        if guess == word:
            print(f'{guess} = {word}!')
            print(f'found in {counter} tries')
            counter_list.append(counter)
            counter = 1

        else:
            counter = counter + 1
            self.words = words
            self.mapped = Wordle_Solver.mapper(self,guess)
            Wordle_Solver.colorize(self)
            Wordle_Solver.reduction(self)

instance = Wordle_Solver(words,guess,word)
instance.colorize()
instance.reduction()



