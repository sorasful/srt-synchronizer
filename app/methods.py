import re

import datetime


def convert_text(text, hour=0, minuts=0, seconds=0, milliseconds=0):
    """
    Function to offset the content of a srt file.
    """
    output = ""
    regex_dialogs = re.compile(r"(^\d+\s+(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)\n[<>\w\sç'\.\/,êéèàùûôü]+\s$)", re.MULTILINE)
    for part, start_time, end_time in re.findall(regex_dialogs, text):
        print(part, start_time, end_time)
        # calculate the new date with the current date and the offset for start en end time

        # replace in part the start time and end time with the new time

        # add to output

    print(output)
    return output
def add_offset_to_date(date:str, offset):
    """ return a well formated format for the new offset with the offset applied
     Expected format : 00:00:00,000   h:m:s,ms"""
    original_date = datetime.datetime.strptime(date, '%H:%M:%S,%f')
    hours, minutes, seconds, miliseconds = offset  # time to add to original date
    new_date = original_date + datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=miliseconds)  # original date + offset applied

    formatted_new_date = datetime.datetime.strftime(new_date, "%H:%M:%S,%f")[:-3]

    return formatted_new_date



file = open('/home/hufflepuff1710/lotr.srt', 'r',encoding='latin-1')
file_content = file.read()
file.close()

convert_text(text=file_content, hour=2 )
