import random

total_h = 0;
total_t = 0;

for i in range(1,5001):
    rand_num = random.random()
    rounded = round(rand_num)
    if rounded == 0:
        total_h +=1
        print "Attempt #%s: Throwing a coin... It's a head!...Got %s head(s) so far and %s tails so far" %(i, total_h, total_t)
    else:
        total_t +=1
        print "Attempt #%s: Throwing a coin... It's a tail!...Got %s head(s) so far and %s tails so far" %(i, total_h, total_t)