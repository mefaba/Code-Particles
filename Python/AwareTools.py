from difflib import SequenceMatcher
import pandas as pd
from itertools import combinations

#Dupicate Delete - Deletes similar strings in a list of strings.
#yenilistemiz = remove_duplicatish(list)
def remove_duplicatish(alist):
    list_remove = []
    alist = list(set(alist))
    listcomb = list(combinations(alist, 2))
    for birtuple in listcomb:
        item1 = birtuple[0]
        item2 = birtuple[1]
        if SequenceMatcher(None, item1.lower(), item2.lower()).ratio() > 0.6: #change this ratio
            list_remove.append(item2)
    list_difference = list(set(list_remove))
    list_final = [x for x in alist if x not in list_difference]
    return list_final

#Another duplicate deleter simple is better.
from difflib import SequenceMatcher 
liste = ["PARALAR", "paralar", "kapıcı", "parasız", "kapı", "geldiğin yere geri dön", "geldiğin yere geri dönme", "Özdilek Park Gucci", "Özdilek Park 2.Kat Gucci"]
def eliminate_duplicates(liste, ratio = 0.8):
    newlist= []
    for item in liste:
        for itemcompare in newlist:
            if SequenceMatcher(None, item.lower(), itemcompare.lower()).ratio() > ratio:
                break
        else:
            newlist.append(item)
    return newlist
print(eliminate_duplicates(liste))
