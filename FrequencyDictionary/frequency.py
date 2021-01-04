import json, os
from pathlib import Path
from collections import Counter, OrderedDict

with open(Path("ebooks.json")) as f:
    data = json.load(f)

##converts json dictionary list to a single
##list to work with data
def json_to_list_parser(li1=[]):
    for dat in data:
        li1.extend(list(dat.values()))
    return li1

##takes strings of data from a list and returns the 
##frequency of each word in a new list
def list_to_word_freq_dict(li2=[], newlist = []):
    for page in li2:
        chars = ",.“”"
        for c in chars:
            if c in page:
                page=page.replace(c,'')
                
        newlist.extend(page.lower().split(' '))
    return Counter(newlist)
tkam_dict = (list_to_word_freq_dict(json_to_list_parser()))
print(tkam_dict)


