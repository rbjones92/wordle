## Wordle: Word Solver

## Summary
Solve for a Wordle word using deduction, following the rules of Wordle. 

## Description
This project scrapes a website for all 5-letter words, and then solves for the word by using deduction.
It follows these rules:
1. Grey letters are added to a list and the next guess cannot have these letters
2. Yellow letters are added to a list and the next guess must have these letters, although not in that specified order
3. Green letters are added to a list and the next guess must included these letters in their proper index.
Using these rules, words are removed from the list of potential words it could be. The program then takes a random guess of reduced words.  
Continue this workflow recursively until a match is found.  

## Technologies
- Python 3.7
- VS Code

## Local Execution
Solving for the word: <br>
![Alt Text](py_files/wordle_terminal.JPG?raw=true "load output")

