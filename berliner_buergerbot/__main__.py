import asyncio

from .check import check_available_appointments
from .compose import compose_message
from .config import Settings
from .send import send_message

settings = Settings()


async def main():
    if not settings.appointment_id:
        raise ValueError(
            "APPOINTMENT_ID not set. Please see README.md for instructions for setting it."
        )

    available_appointments = await check_available_appointments(
        url=f"https://service.berlin.de/terminvereinbarung/termin/all/{settings.appointment_id}/",
        playwright_headless=settings.playwright_headless,
    )
    message = compose_message(available_appointments)
    await send_message(message)


if __name__ == "__main__":
    asyncio.run(main())
