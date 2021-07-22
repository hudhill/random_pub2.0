# RandomPubGenerator
The RPG is a web application for finding a random pub within 1 mile of Edinburgh's City Centre.

[Check it out here!](https://random-pub-generator.herokuapp.com)
__________________________

<img width="1148" alt="Screenshot 2021-07-14 at 12 30 59" src="https://user-images.githubusercontent.com/78811642/125616489-346cfbbe-c4bc-4264-af6b-4830ae855008.png">

___________________________
<img width="1129" alt="Screenshot 2021-07-14 at 12 44 34" src="https://user-images.githubusercontent.com/78811642/125616681-22e49fff-276e-400e-b51b-2f22d163f533.png">


SETUP
------

Clone down this repository

Install dependencies:

     pip3 install flask
     pip3 install psycopg2
     pip3 install psycopg2-binary
    
Create a random_pub database on your local machine:

     createdb random_pub
    
cd into db and run the sql file:

     psql -d random_pub -f random_pub.sql
    
Run the console.py file to populate the app with the list of all pubs within a mile of Edinburgh's City Centre.

     python3 console.py
     flask run
--------
TL;DR:

If you want a random pub NOW, then just snag the play_random.py file and run it in your terminal.
___________________________________________________

### Possible Extensions:

- Add information about the pubs, i.e., location, phone number, type of bar, link to website.

- Add pages for different cities with their own lists of pubs.
