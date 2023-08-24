"""
                        🚀 Frontier Tech Leaders Programme
||||||||||||||||||||||||||||||||| ASSIGNMENT 3 ||||||||||||||||||||||||||||||||||

"""

import re

#For example, "A man, a plan, a canal, Panama" is a valid palindrome.

def is_palindrome_while(input_string:str)->bool:
    i=0
    my_string_list=[]
    while i<len(input_string):

        if input_string[i].isalnum():
            my_string_list.append(input_string[i].lower())
        i+=1
    output_string="".join(my_string_list)
    return output_string==output_string[::-1]


def is_palindrome_for(input_string:str)->bool:

    output_string=""
    reversed_output_string=""
    
    for char in re.split("",input_string.lower()):

        if char.isalnum():
            output_string+=char
            reversed_output_string=char+reversed_output_string
            

    return output_string==reversed_output_string


my_string="A man, a plan, a canal, Panama"

def print_message(checker:bool):
  if checker:
     print(f"\n'{my_string}': Is a valid palindrome")
  else:
    print("\nInvalid palindrome")
    

print("IS_PALINDROME_WHILE".center(50,"*"))

"""if is_palindrome_while(my_string):
    print(f"\n{my_string}Is a valid palindrome")
else:
    print("\nInvalid palindrome")"""

print_message(is_palindrome_while(my_string))
  
print("\n")

print("IS_PALINDROME_FOR".center(50,"*"))

"""if is_palindrome_for(my_string):
  print(f"\n{my_string}Is a valid palindrome")
else:
    print("\nInvalid palindrome")"""

print_message(is_palindrome_for(my_string))