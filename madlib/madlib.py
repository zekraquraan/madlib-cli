import re
import os
def welcomeMessage():
    '''
    This function to show the welcome message.
    '''
    return "welcom to us !!\nThe program prompts you to input words, and then generates a unique story by inserting these words into a pre-written tale.\nsimply!! run the program from the command line and follow the prompts. Have fun!"



def read_template(path):
    try:
        with open(path,'r') as f:
            text=f.read()
        return text
    except FileNotFoundError:
        raise FileNotFoundError (f'File not found at path: {path}')

   

def parse_template(text):
    '''
    Takes a Madlib template as input and print a tuple of empty strings and a modified string with empty curly brace placeholders.

    Arguments:
        text (str): The Madlib template string to be parsed.

    return:
        tuple: A tuple containing empty strings and a modified string with empty curly brace placeholders.

    Example:
        parse_template("It was a {adjective} and {adjective} {noun}.")
        Output: 
          "It was a {} and {} {}."  
          ("adjective", "adjective", "noun")
            
    '''
    new_text = re.sub(r'{.*?}', '{}', text)
    matchesWord = re.findall(r'{(.*?)}', text)
    tupleWord = tuple(matchesWord)
    return  new_text,tupleWord



def prompt(lst):
    '''
    This function to prompt user to enter specific types of words then print it as a tuple. 
    '''
    tupleUser=()
    for element in lst :
      user_Input = input(f'enter a {element}\n')
      tupleUser+=(user_Input,)
    return tupleUser
   
   




def merge(text,wordTuple):
    '''
    Merge the given word tuple into the text to create a Madlib story.

    Arguments:
        text (str): The Madlib template string, with placeholders for the words.
        wordTuple (tuple): The words to be inserted into the placeholders in the text.

    return:
        merge the The Madlib template string with The words in wordTuple.

    Example:
        merge("It was a {} and {} {}.", ("dark", "stormy", "night")
        # Output: "It was a dark and stormy night."
    '''
    madlibText = text.format(*wordTuple)
    return madlibText



def new_file(path,mergedText):
   with open(path,'w' ) as nf:
      nf.write(mergedText)
      

if __name__ == "__main__":
    print("bayan")
    print(welcomeMessage())
    read_content = read_template("./assets/original_text.txt") 
    stripped, parts = parse_template(read_content)
    user_prompt = prompt(parts)
    merge_text=merge(stripped,user_prompt)
    print(merge_text)
    new_file("assets/new_file.txt",merge_text)
   
  
  
 

