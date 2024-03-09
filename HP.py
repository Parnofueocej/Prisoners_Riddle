import random
import statistics
listwin = []
for m in range (40):

    win = 0
    for s in range (100):
        list = []
        for i in range (100):
            list.append(i+1)

        random.shuffle(list)


        y = 0
        no = 0

        for i in range (100):
            n = i+1 # number we need to find
            curr = list[i] # current box
            for j in range (50):
                if (n == curr):
                    y += 1
                    break
                else:
                    curr = list[curr-1]


        if (y == 100):
            win += 1

    listwin.append(win)    

print(listwin)

print ("Mean = ", sum(listwin) / len(listwin))
print ("Median = ", statistics.median(listwin))
print("Standard Deviation = ", statistics.stdev(listwin))

        







