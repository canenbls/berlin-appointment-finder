from app.check import Appointment
from app.compose import compose_message


def test_compose_message_no_appointments():
    result = compose_message(None)
    assert result == "No appointments available."


def test_compose_message_empty_list():
    result = compose_message([])
    assert result == "No appointments available."


def test_compose_message_single_appointment():
    appointment = Appointment(date="12.12.2024", href="/1")
    result = compose_message([appointment])
    expected = "*Available Appointments*\n\n12.12.2024:\nhttps://service.berlin.de/1"
    assert result == expected


def test_compose_message_multiple_appointments():
    appointments = [
        Appointment(date="12.12.2024", href="/1"),
        Appointment(date="13.12.2024", href="/2"),
    ]
    result = compose_message(appointments)
    expected = "*Available Appointments*\n\n12.12.2024:\nhttps://service.berlin.de/1\n\n13.12.2024:\nhttps://service.berlin.de/2"
    assert result == expected
