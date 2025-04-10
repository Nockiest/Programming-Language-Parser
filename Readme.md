# Language interpreter

## Purpouse
This project was created in 12 hours as an asigment on a spring camp organised by the ČVUT Faculty of Information Technology. I wanted to explore the world of language interpreters and created this simple code parser in python. 

## Supported Syntax
'+' , '*' , '>' , '==' , '>=' operators
() brackets, even nested
variable asignments
counting with variables
varibale rewriting
if and else statements

## writing syntax
1. declaring variables:
- varname must be a str
- value must be a number
full example: var YOURVAR = numA + numB ;
2. scopes
This language doesn`t have scopes, everything is global
3. if statements
example:
if your_condition { line of code } else { line of code };
4. codelines
each line has to be seperated by ';', if and if else statements are considered one line of code
each char is seperated by a whitespace:
( 1 * ( 2 + 2) ) 


## How it works
The code works by creating a tree from the operators and numbers and evaluating them bottom to top. The tree contains numbers as leaves. The parents are * then + then >= and so on. When the code needs the value of the syntax tree it calls ROOTNODE.evaluate(), it goes recursively throught the tree and when it evaluates code in the leaf nodes it is inserted as a numer to the parent then to its parent, until it reaches the root.  

## How to run it
1. copy the repo to your pc
2. Insert desired code into code.txt 
3. run the  main.py program, it should write out the values of the variables after reading each line of code
