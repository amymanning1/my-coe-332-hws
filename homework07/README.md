# Vehicle CO2 Emissions By Year - Kubernetes

## What is this and Why is it Important?
### About the Data
This [data](https://www.epa.gov/automotive-trends/explore-automotive-trends-data#DetailedData) (table A-1) is collected by the EPA and NHTSA from light-duty vehicle manufacturers annually to determine the fuel efficiency and carbon footprint of vehicles. Vehicles are categorized by the regulatory class (car or truck), then further organized into vehicle type (Sedan/Wagon, Car SUV, Truck SUV, Minivan/Van, Pickup). Data labeled preliminary is estimation and final numbers have not been recorded for that year yet. Data about the automotive industry's CO<sub>2</sub> emissions and fuel economy is critical to the sustainability of transportation as concerns of climate change and environmental pollution rise. This program is meant to aid consumers in making purchase decisions when it comes to vehicles by providing them with the environmental and fuel economy data of certain car manufacturers. 
### Contents of this Repository
This repository contains: Dockerfile, this README.md, auto_trends_app.py, amym-test-deployment-pvc.yml, amym-test-flask-deployment.yml, amym-test-flask-service.yml, amym-test-redis-pvc.yml and docker-compose.yml. The python script accesses the data and contains all necessary Flask routes for the user to run. The Dockerfile containerizes the flask program so that the program can be run and distributed efficiently. The docker-compose.yml brings together the flask and redis components so the program can be initiated in a few short lines of code.  
## Cloning the Git Repository
Starting from this [repository](https://github.com/amymanning1/my-coe-332-hws), the user should click the green code button, ensure
the link is set to SSH then copy the link. Switching to the command line, the
user will type`git clone git@github.com:amymanning1/my-coe-332-hws.git`
Cloning a Git repository is essentially copying that repo that is available online to a user’s personal system. For this specific program, you will be using 'homework07'.
## How To Access and Download Data
From [this](https://www.epa.gov/automotive-trends/explore-automotive-trends-data#DetailedData) page, scroll towards the bottom of the page until you see table A-1. Click A-1 on the sidebar and once the data set is selected, click the blue rectangular export button above the table. Save this data in a place easily accessible to your local computer and name it `auto-trends-manufacturer.csv`. In your local terminal, secure copy this data over to the class TACC page or whatever secured medium you want to transport your data to by the following command: `[local]$ scp data.csv username@login-coe332.tacc.utexas.edu:~/`
Then, to copy this to your virtual machine, do this: `scp username@login-coe332.tacc.utexas.edu:~/data.csv ./`. From there, copy the raw data into the same directory where this repo is cloned.
## Getting the Docker Image
In a vm (not inside kube-access), build or pull the image from Dockerhub
### Pull the Image from Docker
To pull this image from Docker Hub, type `docker pull amymanning1/auto_trends_app:2.0` in your command line. Ensure you are in the same directory as `auto_trends_app.py`.
### Build a New Image from the Dockerfile
To build a new image using the existing Dockerfile in this repo, `docker build -t <dockerhubusername>/auto_trends_app:2.0 .` filling in the <> with your Docker Hub username. Check that the image built using `docker images`. You will have to rebuild the image using the above command any time you change the python app or Dockerfile. To push the built image to docker, `docker push<dockerhubusername>/auto_trends_app:2.0` Replace the image in `amym-test-flask-deployment.yml` image name to `<yourdockerhubusername>/auto_trends_app:2.0` instead of amymanning1 as the username.
## Launch the Containerized App & Redis from kube-access
To launch the program, the safest bet is to follow this line of commands:
1. Type the command `ssh kube-access` to get inside kubernetes
2. Follow the instructions in the section titled 'Cloning the Git Repository' and type `cd /my-coe-332-hws/homework07`
3. To apply the containers: `kubectl apply -f <each member of below list>`
- `amym-test-redis-pvc.yml`
- `amym-test-deployment-pvc.yml`
- `amym-test-redis-service.yml`
- `amym-test-flask-deployment.yml`
- `amym-test-flask-service.yml`
Check that they built using 
- `kubectl get services`
- `kubectl get deployments`
- `kubectl get pods`
4. Type `kubectl get services` and copy the IP address associated with `amym-test-redis-pvc.yml`
5. To exec into a shell means to start a shell session inside a container. For this software we will exec into the py-debug (assuming user already has this pod) 
- type `kubectl get pods` and copy the name of the py-debug pod
- to exec into the shell, type: `kubectl exec -it <py-debug-name from get pods> -- /bin/bash`
6. Once you are exec'd into the shell, you can do`<some curl command>` (examples in next section) This is where the user accesses the data
## Example Queries and Outputs
* `curl <redis service IP>:5000/data` returns the entire data set (hundreds of dictionaries like this one)
	- **Example Output**: ` {
    "2-Cycle MPG": "31.49453",
    "4 or Fewer Gears": "0.637",
    "5 Gears": "0.362",
    "6 Gears": "0.001",
    "7 Gears": "-",
    "8 Gears": "-",
    "9 or More Gears": "-",
    "Acceleration (0-60 time in seconds)": "9.7682",
    "Average Number of Gears": "4.4",
    "Cylinder Deactivation": "-",
    "Drivetrain - 4WD": "0.02",
    "Drivetrain - Front": "0.979",
    "Drivetrain - Rear": "0.001",
    "Engine Displacement": "122.8462",
    "Footprint (sq. ft.)": "-",
    "Fuel Delivery - Carbureted": "-",
    "Fuel Delivery - Gasoline Direct Injection (GDI)": "-",
    "Fuel Delivery - Other": "-",
    "Fuel Delivery - Port Fuel Injection": "1",
    "Fuel Delivery - Throttle Body Injection": "-",
    "HP/Engine Displacement": "1.10705",
    "HP/Weight (lbs)": "0.043447",
    "Horsepower (HP)": "134.3903",
    "Manufacturer": "Honda",
    "Model Year": "1994",...}`  
* `curl -X POST <redis service IP>:5000/data` adds the data to a redis database
	- **Example Output**: `data loaded into redis`
* `curl -X DELETE <redis service IP>:5000/data` deletes all the data from the redis database
	- **Example Output**: `data deleted, there are len([]) keys in the db`
* `curl <redis service IP>:5000/years` returns a list of all the years recorded in the dataset. 
	- **Example Output**: `[
  "2005",
  "1991",
  "1983",
  "1977",
  "1999",
  "1998",
  "1975",
  "2018",
  "2011", ...]`
* `curl <redis service IP>:5000/years/1999` returns a list of all the data from the year 1999
	- **Example Output**: `[
  {
    "2-Cycle MPG": "24.08907",
    "4 or Fewer Gears": "0.844",
    "5 Gears": "0.153",
    "6 Gears": "0.003",
    "7 Gears": "-",
    "8 Gears": "-",
    "9 or More Gears": "-",
    "Acceleration (0-60 time in seconds)": "10.2646",
    "Average Number of Gears": "4.1",
    "Cylinder Deactivation": "-",
    "Drivetrain - 4WD": "0.213",
    "Drivetrain - Front": "0.558",
    "Drivetrain - Rear": "0.229",
    "Engine Displacement": "203.0776",
    "Footprint (sq. ft.)": "-",
    "Fuel Delivery - Carbureted": "-",
    "Fuel Delivery - Gasoline Direct Injection (GDI)": "-",
    "Fuel Delivery - Other": "0.001",
    "Fuel Delivery - Port Fuel Injection": "0.999",
    "Fuel Delivery - Throttle Body Injection": "0.001",
    "HP/Engine Displacement": "0.921254",
    "HP/Weight (lbs)": "0.046528" ....}, {....},....
]`   
