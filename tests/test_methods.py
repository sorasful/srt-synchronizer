import datetime

from app.methods import add_offset_to_date, convert_text


def test_replace_with_offset():
    orginal_content = """
    
    """

    expected_output = """
    
    
    """

    assert 1 == "ok"


def test_convert_date_success():
    old_date = "00:59:30,000"
    offset = (0, 10, 45, 100)
    assert add_offset_to_date(old_date, offset) == "01:10:15,100"

def test_convert_date_success_same_hour():
    old_date = "00:00:00,000"
    offset = (0, 10, 45, 100)
    assert add_offset_to_date(old_date, offset) == "00:10:45,100"

