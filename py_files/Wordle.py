# Robert Jones
# 8.10.22
# Wordle Solver

import re
import random
from termcolor import colored
import Wordle_Words


# Get the 12,927 5-letter words from the wordle dictionary 
words = Wordle_Words.WordleWords.get_words()

# Pick a random word from that list to be our mystery word
word = random.choice(words)

# Pick a random word to be our girst guess
guess = random.choice(words)

# Start counter to count guesses
counter = 1
counter_list = []

class Wordle_Solver:
    ''' 
    Take a random word from the wordle list and attempts to solve based on pure deduction. 
    '''

    def __init__(self,words,guess,word):
        self.words = words
        self.guess = guess
        self.word = word
        # Map out if each letter is green (match), yellow(in word at different position), or grey (not in word)
        self.mapped = Wordle_Solver.mapper(self,guess)

        print(f'{word} is our word \n{guess} is our guess')


    def mapper(self,guess):
        '''
        Map each letter in guess to an index, and to a color.
    
        Example...
            Word = Keros
            Guess = Begun
            mapper = ['e', 1, 'green', 'b', 0, 'grey', 'g', 2, 'grey', 'u', 3, 'grey', 'n', 4, 'grey']
        '''
        green = []
        yellow = []
        grey = []

        for i in range(0,len(word),1):

            # If guess has letter at some position as word (green)
            if word[i] == guess[i]:
                green.append(word[i])
                green.append(i)
                green.append('green')

            # If guess has letter in word, but not at the same position (yellow)
            if guess[i] in word and word[i] != guess[i]:
                yellow.append(guess[i])
                yellow.append(i)
                yellow.append('yellow')

            # If guess is not in word (grey)
            if guess[i] not in word:
                grey.append(guess[i])
                grey.append(i)
                grey.append('grey')

        # merge lists
        merged = green+yellow+grey

        print(merged)

        return merged


    def colorize(self):
        '''
        print out a colorized representation of the guess, how wordle would do it.
        '''

        merged = self.mapped

        print('new guess: ')

        for y in range(0,5,1):
            if y in merged[1::3]:
                ind = merged.index(y)
                print(colored(merged[ind-1],merged[ind+1]),end='')
        print('\n')


    def reduction(self):

        '''
        Remove words from possibile answers by keeping all words with matches in the right position (greens), 
        keeping all words with letters in word but not in the same position (yellows),
        and removing all words with letters not in word. 
        '''

        global counter
        mapped = self.mapped
        words = self.words

        def grey(words):

            '''
            Eliminate greys
            '''

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

            '''
            keep greens
            '''
            
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
            '''
            keep yellows
            '''

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
            

        # Run all 3 functions, if there are greys, greens, or yellows
        if 'grey' in mapped:
            words = grey(words)

        if 'green' in mapped:
            words = green(words)

        if 'yellow' in mapped:
            words = yellow(words)

        # Print possible choices at this point
        print(f'{words} are possible choices')

        # Take a guess
        guess = random.choice(words)

        # If correct word is chosen
        if guess == word:
            print(f'{guess} = {word}!')
            print(f'found in {counter} tries')
            counter_list.append(counter)
            counter = 1

        # If wrong word is chosen, try again!
        else:
            counter = counter + 1
            self.words = words
            self.mapped = Wordle_Solver.mapper(self,guess)
            Wordle_Solver.colorize(self)
            Wordle_Solver.reduction(self)



instance = Wordle_Solver(words,guess,word)
instance.colorize()
instance.reduction()



