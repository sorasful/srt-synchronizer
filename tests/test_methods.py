from app.methods import add_offset_to_date, convert_text_with_new_offset


def test_replace_with_positive_offset_success():
    offset = 0, 10, 10, 0

    original_text = """1
00:00:34,687 --> 00:00:37,709
De wereld is veranderdàë中文.

2
00:00:37,732 --> 00:00:40,209
Ik voel het in het water.
"""

    expected_text = """1
00:10:44,687 --> 00:10:47,709
De wereld is veranderdàë中文.

2
00:10:47,732 --> 00:10:50,209
Ik voel het in het water.
"""

    assert convert_text_with_new_offset(original_text, offset=offset) == expected_text


def test_replace_with_negative_offset_success():
    offset = 0, -10, 0, 0

    original_text = """1
00:10:34,687 --> 00:10:37,709
De wereld is veranderdàë中文.

2
00:10:37,732 --> 00:10:40,209
Ik voel het in het water.
"""

    expected_text = """1
00:00:34,687 --> 00:00:37,709
De wereld is veranderdàë中文.

2
00:00:37,732 --> 00:00:40,209
Ik voel het in het water.
"""

    assert convert_text_with_new_offset(original_text, offset=offset) == expected_text


def test_convert_date_success():
    old_date = "00:59:30,000"
    offset = (0, 10, 45, 100)
    assert add_offset_to_date(old_date, offset) == "01:10:15,100"


def test_convert_date_success_same_hour():
    old_date = "00:00:00,000"
    offset = (0, 10, 45, 100)
    assert add_offset_to_date(old_date, offset) == "00:10:45,100"

