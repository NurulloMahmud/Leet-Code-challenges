"""
https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""

def timeConversion(s):
    # Split the input string into hours, minutes, seconds, and AM/PM parts
    time_parts = s.split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    second = int(time_parts[2][:2])  # Extract seconds and ignore AM/PM part
    am_pm = time_parts[2][-2:]  # Get AM/PM part

    # Check if it's PM and not 12 PM, then add 12 to the hour
    if am_pm == 'PM' and hour != 12:
        hour += 12
    # If it's 12 AM (midnight), set the hour to 0
    elif am_pm == 'AM' and hour == 12:
        hour = 0

    # Format the hour, minute, and second to have two digits
    formatted_hour = str(hour).zfill(2)
    formatted_minute = str(minute).zfill(2)
    formatted_second = str(second).zfill(2)

    # Return the time in 24-hour format as a string
    return f"{formatted_hour}:{formatted_minute}:{formatted_second}"

