
# function that generates random latitudes and longitudes, run it through for loop to get 5 
# 
import random
import json

lat_list = []
longitude_list = []

compositions = ['stony', 'iron', 'stony-iron']
site_comp_list = []

def rand_lat_long():
    
    for i in range(0,5):
        latitude = random.uniform(16.0,18.0)
        longitude = random.uniform(82.0, 84.0)
        lat_list.append(latitude)
        longitude_list.append(longitude)
    return(lat_list, longitude_list)


def rand_comp():
    
    for j in range(0,5):
        comp_key = random.randint(0, len(compositions)-1)
        site_comp_list.append(compositions[comp_key])
    return site_comp_list

rand_lat_long()
rand_comp()

# assemble data into a dictionary with one key, sites, whose value is a list of dictionaries
# make mini dictionaries for each landing

dict_1 = {'site_id' : 1, 'latitude' : lat_list[0], 'longitude' : longitude_list[0], 'composition' : site_comp_list[0]}
dict_2 = {'site_id' : 2, 'latitude' : lat_list[1], 'longitude' : longitude_list[1], 'composition' : site_comp_list[1]}
dict_3 = {'site_id' : 3, 'latitude' : lat_list[2], 'longitude' : longitude_list[2], 'composition' : site_comp_list[2]}
dict_4 = {'site_id' : 4, 'latitude' : lat_list[3], 'longitude' : longitude_list[3], 'composition' : site_comp_list[3]}
dict_5 = {'site_id' : 5, 'latitude' : lat_list[4], 'longitude' : longitude_list[4], 'composition' : site_comp_list[4]}

sites = {'Sites' : [dict_1, dict_2, dict_3, dict_4, dict_5]}
    
with open('Sites.json' ,'w') as out:
    json.dump(sites, out, indent=2)
