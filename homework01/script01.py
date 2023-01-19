

# first five words get length and store in list
# read in next word and get its length, compare length to words in list
#if smaller, ignore, if larger, replace word do this for every word

# read all words in list
# sort list 

words = []

with open('words', 'r') as f:
        words = f.read().splitlines()

words.sort(key=len, reverse=True)

for i in range(5):
    print(words[i])
