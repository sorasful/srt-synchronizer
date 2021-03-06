import re

import datetime

def add_offset_to_date(date:str, offset):
    """ return a well formated format for the new offset with the offset applied
     Expected format : 00:00:00,000   h:m:s,ms"""
    original_date = datetime.datetime.strptime(date, '%H:%M:%S,%f')
    hours, minutes, seconds, miliseconds = offset  # time to add to original date
    new_date = original_date + datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=miliseconds)  # original date + offset applied

    formatted_new_date = datetime.datetime.strftime(new_date, "%H:%M:%S,%f")[:-3]

    return formatted_new_date


def convert_text_with_new_offset(text, offset):
    """
    Function to offset the content of a srt file.
    """
    dialog_parts = []
    text = text.replace('\r', '')
    regex_dialogs = re.compile(r"(\d+\s+(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)\s+(.+\s?)+)", re.MULTILINE)
    for dialog_part, start_time, end_time, _ in re.findall(regex_dialogs, text):
        new_start_time = add_offset_to_date(start_time, offset)
        new_end_time = add_offset_to_date(end_time, offset)
        new_dialog_part = re.sub(r"\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+", f"{new_start_time} --> {new_end_time}", dialog_part)

        dialog_parts.append(new_dialog_part)

    output = "\n".join(dialog_parts)
    return output
