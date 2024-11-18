#write a program to find the sum of all multiples of 3 and 5 whch exit between 1 and 100
import math 
import pandas as pd
total = 0 
for x in range (1,101):
    if x % 3 == 0 and x % 5 == 0:
        total += x
#---print (total)        

#write a program that will recieve two parameters. An integer 'n' and a string "name". the function will print the name for as many times as the value integer

def print_name(n ,name):
    for x in range(1, n +1):
        print(name)    

#---print_name(3, 'Mike')

#write a program to find the max, min, and average and all scores

test_scores = {
    'Bob': [88, 72, 93, 89],
    'Alice': [90, 84, 99, 93],
    'Mike': [88, 85, 83, 84],
    'Lisa': [100, 80, 87, 98]
}

df = pd.DataFrame(test_scores)
#print (df.describe())

#----print (test_scores['Bob'])

all_scores = test_scores['Bob'] + test_scores['Lisa'] + test_scores['Alice'] + test_scores['Mike']
#print (max(all_scores)
#print (min(all_scores))
#print (sum(all_scores))
#print (sum(all_scores) / len(all_scores)))

all_ = []
for key in test_scores:
    all_ += test_scores
print (all_scores)
print   (max(all_scores),
        (min(all_scores)),
        (sum(all_scores)),
        (sum(all_scores) / len(all_scores)))

#compute the two distances on a graph 