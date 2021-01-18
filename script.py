import json #import json into python script
from difflib import get_close_matches #importing get_close_matching method from difflib to match the input word to json files word

data = json.load(open("data.json")) # Load the data.json file into python script

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn= input("Did You mean %s instead? Enter Y if yes, or N if no : "  % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "This Word Does not exists, please check the word "
        else:
            return "We Did not understand your query"

    else:
        return "This Word Does not exists , please check the  word"

word = input("Enter a word : ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)