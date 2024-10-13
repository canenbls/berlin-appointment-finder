from berliner_buergerbot.check import Appointment
from berliner_buergerbot.compose import compose_message


def test_compose_message_no_appointments():
    result = compose_message(None)
    assert result == "No appointments available."


def test_compose_message_empty_list():
    result = compose_message([])
    assert result == "No appointments available."


def test_compose_message_single_appointment():
    appointment = Appointment(date="12.12.2024", href="https://example.com")
    result = compose_message([appointment])
    expected = "*Available Appointments*\n\n12.12.2024:\nhttps://example.com"
    assert result == expected


def test_compose_message_multiple_appointments():
    appointments = [
        Appointment(date="12.12.2024", href="https://example.com/1"),
        Appointment(date="13.12.2024", href="https://example.com/2"),
    ]
    result = compose_message(appointments)
    expected = "*Available Appointments*\n\n12.12.2024:\nhttps://example.com/1\n13.12.2024:\nhttps://example.com/2"
    assert result == expected
