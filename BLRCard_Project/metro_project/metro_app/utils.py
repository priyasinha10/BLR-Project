from datetime import datetime, time

def calculate_fare(journeys):
    '''The calculate_fare function takes a list of journey details as 
    input and calculates the total fare for a commuter's trips while 
    applying fare capping logic. It considers the peak and off-peak hours 
    for each journey to determine the applicable fare and keeps track of daily 
    and weekly fares to apply the respective caps.
    The function iterates through each journey in the input list and calculates
    the fare based on the journey's date, time, and zones. It keeps track of the 
    total fare and daily fare to apply the daily cap. 
    Additionally, it computes the weekly cap by summing the fares for each day in the week.

    Finally, the function applies the fare capping rules. If the daily fare exceeds 
    the daily cap, it reduces the total fare to the daily cap value. 
    If the total fare exceeds the weekly cap, it sets the total fare to the weekly cap value.
    The function returns the total fare as the output, considering both daily and weekly fare 
    capping to ensure commuters receive the most cost-effective fare for their journeys.'''
    
    valid_zones = {1, 2}

    peak_hours = [(time(7, 0), time(10, 30)), (time(17, 0), time(20, 0))]
    off_peak_hours = [(time(0, 0), time(7, 0)), (time(10, 30), time(17, 0)), (time(20, 0), time(23, 59, 59))]

    total_fare = 0
    daily_fare = 0
    weekly_fares = {}
    current_date = None

    for journey in journeys:
        from_zone = journey['fromZone']
        to_zone = journey['toZone']

        if from_zone not in valid_zones or to_zone not in valid_zones:
            raise ValueError(f"Invalid zone values. Only 1 and 2 are allowed as zone values. Got: fromZone={from_zone}, toZone={to_zone}")

        journey_datetime = datetime.strptime(journey['datetime'], '%Y-%m-%d %H:%M')
        journey_date = journey_datetime.date()
        journey_time = journey_datetime.time()

        # Check if the journey date is different from the current date
        if journey_date != current_date:
            daily_fare = 0  # Reset the daily fare for the new day
            current_date = journey_date

        is_peak = (1 <= journey_datetime.weekday() <= 5 and
                   any(start <= journey_time <= end for start, end in peak_hours)) or \
                  (6 <= journey_datetime.weekday() <= 7 and
                   any(start <= journey_time <= end for start, end in off_peak_hours))

        peak_fare = 30
        off_peak_fare = 25

        fare = peak_fare if is_peak else off_peak_fare

        total_fare += fare
        daily_fare += fare

        weekly_fares[journey_datetime.weekday()] = weekly_fares.get(journey_datetime.weekday(), 0) + fare

    weekly_cap = max(weekly_fares.values())

    # Apply fare capping
    daily_cap = 120  # Daily cap for zones 1-2
    if daily_fare >= daily_cap:
        total_fare -= daily_fare - daily_cap

    if total_fare >= weekly_cap:
        total_fare = weekly_cap

    return total_fare
