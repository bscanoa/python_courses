fname = input("Enter file:")
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)
di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        dic[w] = di.get(w,0) + 1 
        # if w in di:
        #     dic[w] = dic[w] + 1
        # else:
        #     dic[w] = 1
largest = -1
theword = None

for k,v in di.items() :
    if v > largest:
        largest = v
        theword = k

print(theword, largest)
    
