# cars-challenge

Apart from my solution, we also have one from user https://github.com/Uchencho
https://github.com/Femlexx

#########################
Da Flow Explained
##################
"""
A sorted counter object is resorted to.
Comparing the keys and values of a sorted counter object of each of the scrambled names against 
the possible solutions is used to arrive at the right match. We could have tried to match agaisnt all the words
of the English dictionary but that is not practical. This is why a text of the possible matches is provided.

So:
'etecrhlvo' == {'e': 2, 't': 1, 'c': 1, 'r': 1, 'h': 1, 'l': 1, 'v': 1, 'o': 1}
and 
'chevrolet' ==  {'e': 2, 'c': 1, 'h': 1, 'v': 1, 'r': 1, 'o': 1, 'l': 1, 't': 1})

Sorted, they are both:
['c', 'e', 'h', 'l', 'o', 'r', 't', 'v'] for keys
and
[1, 1, 1, 1, 1, 1, 1, 2] for values

They need to match on both key and value levels to have a higher level of accuracy. This caters for names
with similar alphabet count. Same distribution is possible but highly unlikely.
"""
