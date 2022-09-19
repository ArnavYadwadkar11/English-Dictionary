import json
from difflib import get_close_matches

f = open("/Users/chetanyadwadkar/Desktop/Python/LEVEL2/English Dictionary/dictionary.json")
data = json.load(f)
# print(data)

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yes_no = input('Did you mean %s instead? Enter y for yes and n for no: ' % get_close_matches(w,data.keys())[0])
        # yes_no = input('Did you mean %s instead? Enter y for yes and n for no ' % get_close_matches(w,data.keys())[0])
        if yes_no == 'y':  
            return data[get_close_matches(w,data.keys())[0]]
        elif yes_no == 'n':
            return "The word doesn't exist please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist please double check it"

word = input("Please enter a word to get the meaning: ")
output = translate(word)
print(output)
input('Please enter to exit ')