# Orbital Ephemeris Message (OEM) Data Query 
This folder, `homework04` , contains a program called `iss_tracker.py` and this `README.md` file. `iss_tracker.py` takes in xml data from [NASA](https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml) and converts the xml information to a dictionary. With this data type, the user can use flask to query for the program to return a) the entire data set, b) a list of all epochs in the data set, c) state vectors for a specific Epoch from the data set, or c) The instantaneous speed for a specific epoch in the data set. This is important because by sifting through this data, the user can harvest important information about the International Space Station's trajectory to predict clear paths and prevent collisions. 
## How to Access the Data
The [data](https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml) is available through this hyperlink on ISS's trajectory website. This link is already in `iss_tracker.py` therefore downloading the raw XML data is only necessary if the user prefers to view the structure of the data. 
## Flask App
The flask app contains four routes: 
1. `/` : returns the entire data set
2. `/epochs` : returns a list of all epochs in the data set
3. `/epochs/<epoch>`: returns state vector for a specific epoch in the data set
4.  `/epochs/<epoch>/speed`: returns the instantaneous speed for a specific epoch using the cartesian velocity vectors in the state vector.
### Opening and using the Flask App
To open flask, in another window navigate to the same folder that `iss_tracker.py` is located. In this case, that folder is `homework04`. In the command line of this new window type `flask --app iss_tracker --debug run`. This tells the terminal to open the flask app with respect to `iss_tracker` and the user is enabling the debug feature and telling the terminal to run flask. One flask is up and running, to run `iss_tracker.py` type `curl localhost:5000/` after the slash type one of the options listed in Flask App section. Below are some examples of acceptable inputs. 
+ `curl localhost:5000/`
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
   - This is only a sample output, the actual output is much lengthier
- `curl localhost:5000/epochs`
  - `[
  "2023-048T12:00:00.000Z",
  "2023-048T12:04:00.000Z",
  "2023-048T12:08:00.000Z",
  "2023-048T12:12:00.000Z",
  "2023-048T12:16:00.000Z", ...
	]`
* `curl localhost:5000/epochs/2023-063T11:15:00.000Z`
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
+ `curl localhost:5000/epochs/2023-063T11:15:00.000Z/speed` 
   - `7.6617102861022035`
