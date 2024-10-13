import asyncio

from .check import check_available_appointments
from .compose import compose_message
from .send import send_message


async def main():
    available_appointments = await check_available_appointments()
    message = compose_message(available_appointments)
    await send_message(message)


if __name__ == "__main__":
    asyncio.run(main())
