nameList = []
import names

def nameLen(gvnName):
    newLen = len(gvnName)
    for j in range(len(gvnName)):
        if gvnName[j] == " ":
            newLen = len(gvnName) - 1

    print(gvnName + ', ')
    print(newLen)

for i in range(5):
        nameList.append(names.get_full_name())

for k in range(len(nameList)):
    nameLen(nameList[k])
# generate a list of five full names
# define a function that determines the length of a given name
    # take each name as input, check for any spaces, remove spaces, find length and print origial name and length

