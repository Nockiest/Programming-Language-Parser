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
varname: str
value: number
var YOURVAR = numA + numB ;
2. scopes
This language doesn`t have scopes, everything is global
3. if statements
example:
if your_conditoin { line of code } else { line of code };
4. codelines
each line has to be seperated by ';', if and if else statements are considered one line of code
each char is seperated by a whitespace:
( 1 * ( 2 + 2) ) 


## How it works
The code works by creating a tree from the operators and numbers and evaluating them bottom to top. If the variable is created it is added to a stack. Currently, the code is inserted as a string where each char is seperated by a whitespace.

## How to run it
1. copy the repo to your pc
2. into the splitted lines variable split the desired code 
3. run the program, it should write out the values of the variables after reading each line of code
