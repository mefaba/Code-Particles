from difflib import SequenceMatcher
import pandas as pd
from itertools import combinations

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
