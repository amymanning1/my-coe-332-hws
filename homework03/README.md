# Water Turbidity Testing
## Objective & Contents
The purpose of this assignment is to determine the turbidity levels of water and indicate if it is safe to use to the user. In this folder, `homework03`, you will find 3 scipts: this `README.md`, `analyze_water.py`, and `test_analyze_water.py`. `analyze_water.py` takes in json data, calculates the turbidity, then tells the user if the water is safe, or how long until the water will be safe. The final script is used for unit testing and can be employed by typing `pytest` in the command line when inside `homework03` directory. 
## How to Access the Data
The [data](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) was imported from GitHub. Using `requests.get(url='<dataurl>')` from the requests python library to use the data in `analyze_water.py`. 
## Description of the Script
Inside `analyze_water.py`, the function `calc_turb` calculates turbidity of water based on the 5 latest recorded data from `turb_data`.This function makes a list of the last five items in the list of dictionaries `turb_data` and stores them in the list `last_five`. It uses a for loop to find the turbidity of each element in `last_five` using the turbidity formula and keeps a running total so once each element is calculated the average turbidity can be found by dividing by the size of `last_five`. Depending on if the average turbidity (T0) is above or below the safe limit as message is displayed to the user on if the water is usable. The other function, `min_time`, calculates the minimum time until turbid water is safe to consume using an exponential decay relationship, given the average turbidity returned from `calc_turb`. 
## How to Run
Begin running your code by typing `python3 analyze_water.py` into your terminal if you are in the `homework03` directory. If you are not in the directory, navigate there using the `cd` command followed by whichever direction you need to go. The output of your program should look like one of these examples depending on the turbidity levels. 
> The current water turbidity is  0.6819744  NTU.
> The water is safe.
> Minimum time required to return below a safe threshold =  0  hours 
or 
> The current water turbidity is 20 NTU.
> The water is not safe. The turbidity levels are above the safe threshold.
> Minimum time required to return below a safe threshold = 148.2837041 hours

To run the test script, simply type `pytest` in your command line once in the `homework03` directory. To check your version of pytest, type `pytest --version` and the version will be printed. 
