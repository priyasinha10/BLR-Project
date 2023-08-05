BLR Metro Fare Calculator
The BLR Metro Fare Calculator is a web application that calculates the fare for a metro journey based on the zones traveled. It also implements fare capping, which rewards commuters with free rides after they meet the fare equivalent of a daily or weekly pass. This allows for social equity by removing upfront cost barriers associated with recurrent passes.


Requirements
Python 3.10
Django 
Django Rest Framework
SQLite 


git clone https://github.com/priyasinha10/BLR-Project.git
virtualenv env --python=3.10
pip install django
python manage.py runserver




Fare Capping Rules
Daily Cap:

Zones 1-1: 120
Zones 1-2 or 2-1: 120
Zones 2-2: 80
Weekly Cap (Monday to Sunday):

Zones 1-1: 500
Zones 1-2 or 2-1: 600
Zones 2-2: 400



APIs
Calculate Fare API
Endpoint: /api/calculate_fare/

Method: POST

curl --location 'http://localhost:8000/api/calculate_fare/' \
--header 'Content-Type: application/json' \
--data '{
    "journeys": [
        {
            "datetime": "2023-08-05T10:16",
            "fromZone": 1,
            "toZone": 1
        }
    ]
}
'

curl for Daily capping -- 

curl --location 'http://localhost:8000/api/calculate_fare/' \
--header 'Content-Type: application/json' \
--data '{
    "journeys": [
        {
            "datetime": "2023-08-05T10:20",
            "fromZone": 2,
            "toZone": 1
        },
        {
            "datetime": "2023-08-05T10:45",
            "fromZone": 1,
            "toZone": 1
        },
        {
            "datetime": "2023-08-05T16:15",
            "fromZone": 1,
            "toZone": 1
        },
        {
            "datetime": "2023-08-05T18:15",
            "fromZone": 1,
            "toZone": 1
        },
        {
            "datetime": "2023-08-05T19:00",
            "fromZone": 1,
            "toZone": 2
        }
    ]
}'

Usage
Start the development server:

python manage.py runserver

1) Access the BLR Metro Fare Calculator web application at http://localhost:8000/.

2) Enter the journey details in the form, including date and time, and the from and to zones.

3) Click on "Add Journey" to add the journey details to the list.

4) Add multiple journeys to the list.

5) Click on "Calculate Fare" to calculate the fare based on the journey details and fare capping rules.

6) The calculated fare will be displayed on the page.

<img width="960" alt="image" src="https://github.com/priyasinha10/BLR-Project/assets/91273459/18421ea0-c736-4b91-9d16-ba818e9ef720">

