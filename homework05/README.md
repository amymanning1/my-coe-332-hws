# Orbital Ephemeris Message (OEM) Data Query and Containerization 
This folder, `homework05` , contains a program called `iss_tracker.py`, `Dockerfile` and this `README.md` file. `iss_tracker.py` takes in xml data from [NASA](https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml) and converts the xml information to a dictionary and a json file. With this data type, the user can use flask to query for the program to return a) the entire data set, b) a list of all epochs in the data set, c) state vectors for a specific Epoch from the data set, c) The instantaneous speed for a specific epoch in the data set. d) a help page, e) an option to delete all the data, of f) an option to restore the data. This is important because by sifting through this data, the user can harvest important information about the International Space Station's trajectory to predict clear paths and prevent collisions. 
## How to Access the Data
The [data](https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml) is available through this hyperlink on ISS's trajectory website. This link is already in `iss_tracker.py` therefore downloading the raw XML data is only necessary if the user prefers to view the structure of the data. 
## Flask App
The flask app contains eight routes: 
1. `/` : returns the entire data set
2. `/epochs` : returns a list of all epochs in the data set
3. `/epochs/<epoch>`: returns state vector for a specific epoch in the data set
4.  `/epochs/<epoch>/speed`: returns the instantaneous speed for a specific epoch using the cartesian velocity vectors in the state vector.
5. `/help`: returns a string that lists all available routes and their methods
6. `/delete-data`: deletes the entire data set off the json file that is loaded from the url
7. `/post-data`: replaces the deleted data with the data from the website
### Opening and using the Flask App
To open flask, in another window navigate to the same folder that `iss_tracker.py` is located. In this case, that folder is `homework05`. In the command line of this new window type `flask --app iss_tracker --debug run`. This tells the terminal to open the flask app with respect to `iss_tracker` and the user is enabling the debug feature and telling the terminal to run flask. One flask is up and running, to run `iss_tracker.py` type `curl localhost:5000/` after the slash type one of the options listed in Flask App section. 
## Run Instructions
### To Pull an Image from Docker Hub
To pull this image from Docker Hub, type `docker pull amymanning1/iss_tracker:hw05` in your command line. Ensure you are in the same directory as `iss_tracker.py`. 
### Build a new Image
To build a new image using the existing Dockerfile in this repo, `docker build -t <dockerhubusername>/iss_tracker:hw05 .` filling in the <> with your Docker Hub username. Check that the image built using `docker images`. 
### Run the Containerized App
To test the image you either built or pulled, use `docker run -it --rm -p 5000:5000 username/iss_tracker.py` to start flask inside of the container. The `-p` flag is important to connect the port on the user's device to the port on the container. Because the virtual machines where this program is used are connected on port 5000, it is imperative that we connect that to the container's port 5000. In another window with the command line, interact with the program `curl 127.0.0.1:5000/epochs` ensuring the order of connections is `<host port>:<container port>`. If you are having issues determining the port, check the flask window where it says `* Running on http://127.0.0.1:5000`, remove the `http://` and use that address, filling in the addresses with what your flask displays. 
### Example Paths and Outputs
+ `curl 127.0.0.1:5000/`
   - `},
                "X_DOT": {
                  "#text": "5.2410359153923798",
                  "@units": "km/s"
                },
                "Y": {
                  "#text": "-5991.3267501460596",
                  "@units": "km"
                },
                "Y_DOT": {
                  "#text": "0.32894397165270001",
                  "@units": "km/s"
                },
                "Z": {
                  "#text": "1991.1683453687999",
                  "@units": "km"
                },
                "Z_DOT": {
                  "#text": "-5.57976406061041",
                  "@units": "km/s"
                }
              },
              {`
   - This is only a sample output, the actual output is much longer
- `curl 127.0.0.1:5000/epochs`
  - `[
  "2023-048T12:00:00.000Z",
  "2023-048T12:04:00.000Z",
  "2023-048T12:08:00.000Z",
  "2023-048T12:12:00.000Z",
  "2023-048T12:16:00.000Z", ...
        ]`
* `curl 127.0.0.1:5000/epochs/2023-063T11:15:00.000Z`
   - `{
  "EPOCH": "2023-063T11:15:00.000Z",
  "X": {
    "#text": "-3230.7742245286299",
    "@units": "km"
  },
  "X_DOT": {
    "#text": "-4.7139536603293903",
    "@units": "km/s"
  },
  "Y": {
    "#text": "5860.46590407639",
    "@units": "km"
  },
  "Y_DOT": {
    "#text": "-1.4242336555306401",
    "@units": "km/s"
  },
  "Z": {
    "#text": "-1183.7150780833999",
    "@units": "km"
  },
  "Z_DOT": {
    "#text": "5.8695829401146797",
    "@units": "km/s"
  }
}`
+ `curl 127.0.0.1:5000/epochs/2023-063T11:15:00.000Z/speed`
   - `7.6617102861022035`
* `curl 127.0.0.1:5000/help`
   - This program accesses different data elements from the ISS Trajectory site by NASA. Available routes include:
    /                               returns the entire data set ('GET' method) ....
+ `curl -X DELETE 127.0.0.1:5000/delete-data`
   - []
   - NOTE: Anything curled after this query will be empty until `post-data` is run
   - NOTE: you must include `-X DELETE`, you will receive an error if you do not
* `curl -X POST 127.0.0.1:5000/post-data`
   - `},
                "X_DOT": {
                  "#text": "5.2410359153923798",
                  "@units": "km/s"
                },
## About the Data
This data is coordinates on the international space station's current location. After the headers, the state vectors are listed at four-minute intervals and updated three times a week. This data is collected to determine the trajectory of the ISS to prevent collisions or it going too far off course. Determining trajectory is also important to maintain communication with the ground. There is a unique epoch for every data point which acts as an id. The data inside the state vector is the epoch, X, Y, Z, X_DOT, Y_DOT, and Z_DOT coordinates. The raw coordinates are in kilometers and the _DOT coordinates and the time derivatives or velocities at each position in km/s.   
