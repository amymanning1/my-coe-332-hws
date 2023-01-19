import names
eightList = []
nameList = []

while True:
    if len(eightList) == 5: 
        break
    newName = names.get_first_name()
    nameList.insert(0, newName)
    if len(nameList[0]) == 8:
        eightList.append(newName)
        print(newName)

# get a name
# see if its 8 characters, if so add to list, if not keep going
#go until you have 5 names in list
