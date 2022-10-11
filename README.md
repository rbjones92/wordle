## Wordle: Word Solver

## Summary
Solve for a Wordle word using deduction, following the rules of Wordle. 

## Description
This project scrapes a website for all 5-letter words, and then solves for the word by using deduction.
It follows these rules:
1. Grey letters are added to a list and the next guess cannot have these letters
2. Yellow letters are added to a list and the next guess must have these letters, although not in that specified order
3. Green letters are added to a list and the next guess must included these letters in their proper index.
4. Words are removed from the list as specified above. 
5. The program, at random, takes a guess from reduced word list.
6. Continue this workflow recursively until a match is found.  

## Technologies
- Python 3.7
- VS Code

## Local Execution
![Alt Text](py_files/wordle_terminal_2.JPG?raw=true "program run in terminal")
![Alt Text](py_files/wordle_terminal_4.JPG?raw=true "program run in terminal")
![Alt Text](py_files/wordle_terminal_3.JPG?raw=true "program run in terminal")

