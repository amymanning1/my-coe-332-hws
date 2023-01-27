import json
import math

mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float: 
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])

    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

with open('Sites.json', 'r') as f:
    meteor_data = json.load(f)


count = 0 # allows us to iterate through if statement with the initial latitude and longitude and keep track of which leg of journey rover is on
max_speed = 10 # km / hr
tot_time = 0 # hr

for i in meteor_data['Sites']:    

    if count == 0:
        #this is for the first iteration with initial coordinates
        latitude_1 = 16.0
        longitude_1 = 82.0

        latitude_2 = i['latitude']
        longitude_2 = i['longitude']
        

    else: 
        #this is for every other case besides the first
        
        latitude_1 = latitude_2
        longitude_1 = longitude_2

    # checking composition of meteorite to determine how long it will take to sample 
    if i['composition'] == 'stony':
        sample_time = 1 # hr
    elif i['composition'] == 'iron':
        sample_time = 2 # hrs
    else:
        sample_time = 3 # hrs

    latitude_2 = i['latitude']   
    longitude_2 = i['longitude']   
    
    count = count + 1

    dist = calc_gcd(latitude_1, longitude_1, latitude_2, longitude_2) # calculates distance tranveled from one site to the next
    
    travel_time = dist / max_speed
    tot_time = sample_time + travel_time

    print('leg = ', count, ', time to travel = ' , travel_time, 'hr, time to sample = ', sample_time, ' hr') # prints after each leg of trip

print('=================================')
print('number of legs = ' , count, ', total time elapsed = ' , tot_time, ' hr') # summary of entire trip

