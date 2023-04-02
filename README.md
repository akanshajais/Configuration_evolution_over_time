# Configuration_evolution_over_time
--------------------------------------------------------------
I am submitting my contribution for microtask **T331202 Configuration evolution over time**, I worked along with the given description i.e., 

![image](https://user-images.githubusercontent.com/85181086/229358755-142092ca-f907-468a-ab24-548716a84f4f.png)

# Steps I followed 
----------------------------------------
with using the subprocess module to run Git commands. I used the csv module to parse and write CSV file. parse_csv function reads the CSV file into the data list of dictionaries.Then by initializing a Git repository, adding and removing the initial data file, and commit it.
next i used to looping over all Git commits and checking out the data file at each commit then call the parse_csv function to parse the data at that commit and add a commit_timestamp field to each row of data.

# Libraries Used
-----------------------------------------------------
subprocess 

csv

datetime
