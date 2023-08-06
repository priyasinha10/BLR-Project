from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import calculate_fare
from django.shortcuts import render
import json
from datetime import datetime


"""calculate_fare_api takes a list of journey details, 
converts datetime strings, calculates the fare with 
fare capping rules, and returns the result in a JSON response."""

@api_view(['POST'])
def calculate_fare_api(request):
    data = json.loads(request.body)  # Parse the JSON data
    journeys = data.get('journeys', [])

    # Convert datetime strings from '%Y-%m-%dT%H:%M' to '%Y-%m-%d %H:%M'
    if journeys:
        for journey in journeys:
            datetime_str = journey.get('datetime')
            if datetime_str:
                # strptime() -- Convert the datetime string to a datetime object
                dt_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
                # strftime() -- Convert the datetime object back to a formatted string
                journey['datetime'] = dt_obj.strftime('%Y-%m-%d %H:%M')
            else:
                return Response({'error': "Please provide the datetime for all journeys."})

        fare = calculate_fare(journeys)
        return Response({'fare': fare})
    return Response({'error': 'Please provide Details'})


def fare_calculator_page(request):
    return render(request, 'index.html')
