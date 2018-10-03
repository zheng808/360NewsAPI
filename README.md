# API_News360

# Technologies
Python3, Flask, Sqlite3
The given data set needs around 10 mins to load. csvparser.py is the file that reads the data from csv and load it to database. mysql.py is the file that has all db configuration. rest.api.py has all the api endpoints and query construction

# Results
It takes around 10 mins to load all data-1.csv. If it is too long, change the filename to test.csv inside the csvparser.py file
API provided
/unique-users with options os and device
/loyal-users with options os and device


# Docker
I created a bash file that runs the docker image and it runs on port 5000
It builds the image and runs on container when the bash file is running


# How to run
# option 1
Run the bash file ./bash.sh

# option 2
Make sure you have flask installed
python app.py 

# CickHouse 
I used Clickhouse Docker image to run the database server. But the flask app does not connect to the clickhouse server properly. I am using https://github.com/mymarilyn/clickhouse-driver this connector. 