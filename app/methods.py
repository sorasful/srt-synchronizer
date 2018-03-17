import re


def apply_offset(text, hour=0, minuts=0, seconds=0, milliseconds=0):
    """
    Function to offset the content of a srt file.
    """
    output = ""
    regex_dialogs = re.compile(r"(^\d+\s+(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)\n[<>\w\sç'\.\/,êéèàùûôü]+\s$)", re.MULTILINE)
    for part, start_time, end_time in re.findall(regex_dialogs, text):
        print(part, start_time, end_time)

    print(output)

file = open('/home/hufflepuff1710/lotr.srt', 'r',encoding='latin-1')
file_content = file.read()
file.close()

apply_offset(text=file_content, hour=2 )
