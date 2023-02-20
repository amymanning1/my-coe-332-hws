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
Each route besides the first uses iterative methods to navigate through the many keys
