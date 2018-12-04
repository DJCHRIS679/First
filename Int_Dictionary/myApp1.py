import json
from difflib import get_close_matches

data = json.load(open("data.json")) #open dataset and set to dictionary data

def translate (w):
    w = w.lower() #Accounts for Case sensitivity issues
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        new_w = get_close_matches(w,data.keys())[0]
        did_in = input("Did you mean '%s' instead of '%s'? (Y = Yes, N = No): " %(new_w, w)).lower()
        if did_in == "y":
            return data[new_w]
        elif did_in == "n":
            return "Sorry. There are no matches for your word: '%s'" %w
        else:
            return "Sorry we didn't understand your query'"
        #return "Did you mean %s instead?" %get_close_matches(w,data.keys())[0]
    else:
        # new_w = get_close_matches(w,data.keys())[0]
        # did = input("Did you mean '%s'? ([Y] = Yes, [N] = No): " %new_w).lower()
        # if did == "y":
        #     return data[new_w]
        # else:
        #     return "The word doesn't exist. Please double check it."
        return "The word doesn't exist in this library. Please double check it."


word = input("Enter a word you want the definition for: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
