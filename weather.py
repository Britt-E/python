import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

#  NUMBER ONE
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

#  NUMBER TWO
def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")

# NUMBER THREE
def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    return round(5/9*(float(temp_in_fahrenheit) - 32),1)

# NUMBER FOUR
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    for num in weather_data:
        total += float(num)
 
    return total/len(weather_data)

# NUMBER FIVE
def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row != []:
                # date = row[0]
                # min_temp = int(row[1])
                # max_temp = int(row[2])
                list.append([row[0], int(row[1]), int(row[2])]) 
 
    return list

# NUMBER SIX
def find_min(weather_data: list) -> tuple:
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) < 1:
        return ()
    minimum = weather_data[0]
    minIndex = 0
    for i, num in enumerate(weather_data):
        if num <= (minimum):
            minimum = num
            minIndex = i
 
    return (float(minimum),minIndex)

# NUMBER SEVEN
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) < 1:
        return ()
    maximum = weather_data[0]
    maxIndex = 0
    for i, num in enumerate(weather_data):
        if num >= (maximum):
            maximum = num
            maxIndex = i
    # print('test', (float(maximum),maxIndex))  

    return (float(maximum),maxIndex)

# NUMBER EIGHT
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # calculate number of days
    number_of_days = str(len(weather_data))
    
    # extract minimum and maximum temperatures
    min_temps = []
    for day in weather_data:
        min_temp = int(day[1])
        min_temps.append(min_temp)
    
    
    max_temps = []
    for day in weather_data:
        max_temp = int(day[2])
        max_temps.append(max_temp)

    # find overall minimum and maximum temperatures
    # min_temp_tuple = find_min(min_temps)
    # overall_min = min_temp_tuple[0]
    # overall_min_index = min_temp_tuple[1]

    overall_min, overall_min_index = find_min(min_temps) # (min_temp, min_index)
    formatted_min_temp = format_temperature(convert_f_to_c(overall_min))
    overall_max, overall_max_index = find_max(max_temps)
    formatted_max_temp = format_temperature(convert_f_to_c(overall_max))

    # convert dates for min/max temperatures
    overall_max_day = convert_date(weather_data[overall_max_index][0])  
    overall_min_day = convert_date(weather_data[overall_min_index][0])

    # calculate average temperatures
    average_min = format_temperature(convert_f_to_c(calculate_mean(min_temps)))
    average_max = format_temperature(convert_f_to_c(calculate_mean(max_temps)))

    # create the summary string
    summary = (f"{number_of_days} Day Overview\n  The lowest temperature will be {formatted_min_temp}, and will occur on {overall_min_day}.\n  The highest temperature will be {formatted_max_temp}, and will occur on {overall_max_day}.\n  The average low this week is {average_min}.\n  The average high this week is {average_max}.\n")
 
    return summary

# NUMBER NINE
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for row in weather_data:
        number_of_days = convert_date(row[0])
        overall_min = format_temperature(convert_f_to_c(row[1]))
        overall_max = format_temperature(convert_f_to_c(row[2]))
        summary += (f"---- {number_of_days} ----\n  Minimum Temperature: {overall_min}\n  Maximum Temperature: {overall_max}\n\n")
    
    return summary
