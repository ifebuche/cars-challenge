import pandas as pd
from collections import Counter
import random

#Read cars and makers files into dfs
df = pd.read_csv('cars.txt', delimiter='\n', encoding='latin-1', header=None)
df1 = pd.read_csv('makers1.txt', delimiter='\n', encoding='latin-1', header=None)

#chnage their col names
df.columns = ['cars']
df1.columns = ['makers']

#make list of lower cases of all removing trailing spaces after taking a split at the equal sign
makers = [line.split('=')[-1].lower().strip().replace(' ','') for line in df1.makers]
cars = [line.split()[1].lower().replace('=', '') for line in df.cars]

#Confirm matching lengths
len(makers) == len(cars)

#shuffle the makers list just to make sure
random.shuffle(makers)

##########################
# Da Flow Explained
###################
# """
# A sorted counter object is resorted to.
# Comparing the keys and values of a sorted counter object of each of the scrambled names against 
# the possible solutions is used to arrive at the right match. We could have tried to match agaisnt all the words
# of the English dictionary but that is not practical. This is why a text of the possible matches is provided.

# So:
# 'etecrhlvo' == {'e': 2, 't': 1, 'c': 1, 'r': 1, 'h': 1, 'l': 1, 'v': 1, 'o': 1}
# and 
# 'chevrolet' ==  {'e': 2, 'c': 1, 'h': 1, 'v': 1, 'r': 1, 'o': 1, 'l': 1, 't': 1})

# Sorted, they are both:
# ['c', 'e', 'h', 'l', 'o', 'r', 't', 'v'] for keys
# and
# [1, 1, 1, 1, 1, 1, 1, 2] for values

# They need to match on both key and value levels to have a higher level of accuracy. This caters for names
# with similar alphabet count. Same distribution is possible but highly unlikely.
# """
ordered = []
for car in cars:
    c = Counter(car)
    for maker in makers:
        m = Counter(maker)
        if sorted(c.keys()) == sorted(m.keys()): #compare a sorted list of keys
            if sorted(c.values()) == sorted(m.values()):#ditto for values
                ordered.append(maker)
            else:
                print("No match for '{}'.\n".format(car))


#Print the matches deleting the missed match
for c, o in zip(cars, ordered):
    if c == 'esedrmcde':
        x = cars.index('esedrmcde')
        del cars[x]
    else:
        print("{} == {}".format(c, o))

