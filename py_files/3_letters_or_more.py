# Robert Jones
# 8.14.22
# narrow down list to words with 3 of the same letters

import Wordle_Words


words = Wordle_Words.WordleWords.get_words()

letter_list = []

for i in range(0,len(words),1):
    letter_list.append(list(set(words[i])))

for i in range(0,len(words),1):
    for j in range(0,len(letter_list[i]),1):
        if words[i].count(letter_list[i][j]) > 2:
            print('three of the same letters in word',words[i])