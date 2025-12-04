from src.rpi_clock.clock import current_time_str


def test_current_time_str_format():
    s = current_time_str()
    assert len(s) == 8
    assert s.count(":") == 2
