import requests
from bs4 import BeautifulSoup
from itertools import permutations as perm
#import time

'''
i used two methods, memory error due to permutation of words
 with more than 11 alphabets made me realise that i didnt have to
 do permutations
'''

#code to scrape list pf car manufacturers ,some are missing
#some aplhabets used are not english alphabets (the s in skoda )
'''

car_makers= []
url = requests.get('https://www.carlogos.org/car-brands-a-z/').text
print(url)
soup = BeautifulSoup(url,'lxml')
soup = soup.find_all('dd')
for i in soup:
    car_makers.append(i.text.upper())

#print(car_makers)
'''
#copied the list of scramnled car manufactureres from the 
#chat and edited mercedes (has 2 D's)
lst = ['ETECRHLVO','AKSDO','LPOE','IDAU','UZIUS','UCRAA','RBSUAU','RGAJUA', 'PEJE', 'AZMAD', 'IMNI','DOVLNARRE', 'SLXEU',
    'BASA','UPETOGE', 'UTLARNE','ONTRPO','EDWOAO','TIOCNER','GNOYAGSNS', 'ALICALDC','IATF', 'RASONTATNIM', 'ESEDRMCE', 'MHCOI', 'NLACMER', 'TIINIIFN', 'TSOLU', 'LNETEBY', 'IRATASME', 'RFEIARR', 'DHNOA','SNNSIA', 'AAVLH','RFDO','OLOVV', 'ETSA', 'YTOTAO','UODPREA', 'ELGYE','HSIBUSIMIT', 'OOEMRFAAL', 'HAIATDUS', 'GNEOVSKLWA', 'CEHSRPO', 'NIADYHU', 'ITABGTU', 'MBALNIHGROI', 'CRLOSEORYL','IKZSUU','SAELT']


#saved the supplied list of car manufacturers as a text file
#open the file
with open('newt.txt','r') as file:
    car_makers = file.readlines()

#remove the new line symnol from each car manufaruer because
#they were all on a new line and turn it to uppercase
#since scrambled is in uppercase
for names in car_makers:
    car_makers[car_makers.index(names)] = names.strip('\n').upper()
    
#created anotherblist to join manufacturers with two words together
#Land Rover --> LandRover (theres no space in scrambled)
car = [x.replace(' ','') for x in car_makers]

#numbering counter
num = 1

for i in lst: 
    #can only do permutations pf length below 11
    if len(i)<11 :
        #VOLVO --> [V,O,L,V,O]
        u = list(i)
        #VOLVO --> [[V,O,L,V,O],[O,V,L,V,O]...]
        wor = list(perm(u))
        #[[V,O,L,V,O],[O,V,L,V,O]...]--> [[VOLVO],[OVLVO]..,]
        worf = set([''.join(x) for x in wor])
        
        #checks to see if any of the list of list match a car manufacturer name
        for o in worf:
            if o in car:
                print(str(num)+'.',i , '=' ,car_makers[car.index(o)].title())
        
        
    else :
        #assign a var to the length of the scrambled name
        length = len(i)
        #u = list(i[:10])
        #wor = list(perm(u))
        #worf = set([''.join(x) for x in wor])
        #sort it after turning it to list and turn it to set to remove duplicates
        one = set(sorted(list(i)))
        
        #loop through the given car manufacturers name list
        for y in car:
            
            #checks if they both have the same length and 
            #if the same alphabets make them up after removing duplicates
            if len(y)==length and set(sorted(list(y))) == one:
                print(str(num) + '.',i, '=',car_makers[car.index(y)].title())
                
    #increase the numbe (1 to 2 to 3...)          
    num = num +1
    
#code below doesnt work, i felt of i could permutate part pf it amd check 
#if any starts any car manufactirer name
'''
        for y in car:
            for j in worf:
                if y.startswith(j[:4]):
                    print(str(num)+'.',i , '=' ,car[car.index(y)])
                break
'''
