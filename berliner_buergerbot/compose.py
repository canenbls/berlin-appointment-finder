from .check import Appointment


def compose_message(available_appointments: list[Appointment] | None) -> str:
    if available_appointments:
        appointments_str = "\n".join(
            [
                f"{appointment.date}:\n{appointment.href}"
                for appointment in available_appointments
            ]
        )
        return f"*Available Appointments*\n\n{appointments_str}"
    else:
        return "No appointments available."
