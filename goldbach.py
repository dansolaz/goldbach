
from more_itertools import distinct_permutations
from  itertools import combinations
import math
print("hey")
#n is the number we are checking all primes lower than
N = int(input("please choose N:"))
#this is the amount of primes
trueBoolsNum = int(input("please choose how much true bools you want:"))
#lets create list of bools and make some of them prime(true)
bools = [False]*N
for i in range(0, trueBoolsNum):
    bools[i] = True
optionsNum = 10
goodOptionsNum = 0
goldbachOptionsNum = 0
#now lets sort them in any order we can
options = distinct_permutations(bools, len(bools))

def get_all_paires(primeList):
    mixed_paires = combinations(primeList, 2)
    # need to add identical paires ( 3,3   5,5 , 9,9...etc)
    identical_paires = [(x, x) for x in primeList]
    return identical_paires + list(mixed_paires)

def find_pair(paires,n):
    for pair in paires:  # check identical paires
        if n == pair[0] + pair[1]:
            return pair
    return None

def goldbach(primeList,N):
    all_paires = get_all_paires(primeList)
    for n in range(2,N+2,2):
        if find_pair(all_paires,n) == None:
            return False
    return True

def lnCheck(k):
    if (k - 1) == math.floor(index / math.log(index)) or math.ceil(index / math.log(index)):
        return False
    else:
        return True

if __name__ == '__main__':


    for bool_list in options:
        print(bool_list)
        k = 0
        r = range
        index = 0
        for bool in bool_list:
            index = index + 1

            if index%2 == 0 and index != 2:
                if bool:
                    break
            if index < 4:
                if not bool:
                    break
            else:
                if lnCheck(k):
                    #print("break")
                    break
            if bool:
                k = k+1
        else:
            #print(bool_list)
            primes = []
            goodOptionsNum = goodOptionsNum + 1
            index = 0
            for bool in bool_list:
                index = index + 1
                if bool:
                    primes.append(index)
            if goldbach(primes, N):
                goldbachOptionsNum = goldbachOptionsNum + 1
                #print(bool_list)

            primes.clear()



        optionsNum = optionsNum+1

    print("number of options was", optionsNum)
    print("from them", goodOptionsNum, "were good")
    print("from them", goldbachOptionsNum, "were goldbach")

