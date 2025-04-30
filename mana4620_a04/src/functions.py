"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-02-23"
-------------------------------------------------------
"""


def day_of_the_week(day_number):
    """
    -------------------------------------------------------

    Returns "Error" if the number is used outside parameter range 
          1 to 7.
    Use: day=day_of_the_week(day_number)

    -------------------------------------------------------
    Parameters:
       day_number-description of number
    Returns:
     day-description (the day which it is which returns a string)

    ------------------------------------------------------
    """
    if day_number == 1:
        day = "Sunday"
    elif day_number == 2:
        day = "Monday"
    elif day_number == 3:
        day = "Tuesday"
    elif day_number == 4:
        day = "Wednesday"
    elif day_number == 5:
        day = "Thursday"
    elif day_number == 6:
        day = "Friday"
    elif day_number == 7:
        day = "Saturday"
    else:
        day = "Error"
    return day


def level_of_pollution(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution_level = level_of_pollution(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution_level - name of pollution pollution_level (str)
    ------------------------------------------------------
    """
    if 0 <= air_quality_index <= 50:
        pollution_level = "Good"
    elif 51 <= air_quality_index <= 100:
        pollution_level = "Moderate"
    elif 101 <= air_quality_index <= 150:
        pollution_level = "Unhealthy for Sensitive Groups"
    elif 151 <= air_quality_index <= 200:
        pollution_level = "Unhealthy"
    elif 201 <= air_quality_index <= 300:
        pollution_level = "Very Unhealthy"
    elif air_quality_index > 300:
        pollution_level = "Hazardous"
    elif air_quality_index < 0:
        pollution_level = "Error"

    return pollution_level


def largest_product(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    val1, val2, and val3.
    Use: product = largest_product(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        product - the product of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if (val1 < val2 < val3):
        product = val2*val3
    elif (val1 > val2 > val3):
        product = val1*val2
    else:
        product = val1*val3

    return product


def colour_mix(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_mix(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if (rgb_colour1 == "red" and rgb_colour2 == "blue")or (rgb_colour1 == "blue"and rgb_colour2 == "red"):
        rgb_colour = "fuchsia"
    elif (rgb_colour1 == "red" and rgb_colour2 == "green")or (rgb_colour1 == "green"and rgb_colour2 == "red"):
        rgb_colour = "yellow"
    elif (rgb_colour1 == "green" and rgb_colour2 == "blue")or (rgb_colour1 == "blue"and rgb_colour2 == "green"):
        rgb_colour = "aqua"
    elif (rgb_colour1 == "red" and rgb_colour2 == "red"):
        rgb_colour = "red"
    elif (rgb_colour1 == "blue" and rgb_colour2 == "blue"):
        rgb_colour = "blue"
    elif (rgb_colour1 == "green" and rgb_colour2 == "green"):
        rgb_colour = "green"
    else:
        rgb_colour = "Error"

    return rgb_colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Dividing the number by 3 or 7 or both 
    Return "Nada"if not divided by 3 or 7

    Use: given = yee_ha(number): 
    -------------------------------------------------------
    Parameters:
        number -a number which could be divisible by 3 or 7

    Returns:
        given- a number which could be divisible by 3 or 7 
        or both wich prints Yee, Ha, or Yee Ha 
    -------------------------------------------------------
    """
    if(number % 3 == 0 and number % 7 == 0) or (number % 7 == 0 and number % 3 == 0):
        given = "Yee Ha"
    elif(number % 3 == 0):
        given = "Yee"
    elif(number % 7 == 0):
        given = "Ha"
    else:
        given = "Nada"

    return given
