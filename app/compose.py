from .check import Appointment


def compose_message(available_appointments: list[Appointment] | None) -> str:
    if available_appointments:
        appointments_str = "\n\n".join(
            [
                f"{appointment.date}:\nhttps://service.berlin.de{appointment.href}"
                for appointment in available_appointments
            ]
        )
        return f"*Available Appointments*\n\n{appointments_str}"
    else:
        return "No appointments available."
