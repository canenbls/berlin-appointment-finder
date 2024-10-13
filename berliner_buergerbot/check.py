import asyncio
import re

from playwright.async_api import Locator, async_playwright
from pydantic import BaseModel

from .config import Settings

URL_BASE = "https://service.berlin.de/terminvereinbarung/termin"

settings = Settings()


class Appointment(BaseModel):
    date: str
    href: str


date_pattern = re.compile(r"\d{2}\.\d{2}\.\d{4}")


async def extract_appointment(td: Locator) -> Appointment | None:
    a = td.locator("a")
    title = await a.get_attribute("title")
    href = await a.get_attribute("href")

    if title and href:
        date_match = date_pattern.search(title)

        if date_match:
            return Appointment(
                date=date_match.group(),
                href=href,
            )

    return None


async def check_available_appointments() -> list[Appointment] | None:
    if not settings.appointment_id:
        raise ValueError(
            "APPOINTMENT_ID not set. Please see README.md for instructions for setting it."
        )

    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=settings.playwright_headless)
        page = await browser.new_page()
        await page.goto(f"{URL_BASE}/all/{settings.appointment_id}/")

        available_appointments: list[Appointment] = []

        if page.url == f"{URL_BASE}/day/":
            td_elements = await page.locator("td.buchbar").all()
            tasks = [extract_appointment(td) for td in td_elements]
            results = await asyncio.gather(*tasks)
            available_appointments.extend(
                result for result in results if result is not None
            )

        await browser.close()

    return available_appointments if available_appointments else None


async def main():
    available_appointments = await check_available_appointments()
    print(
        "\n".join(
            appointment.model_dump_json() for appointment in available_appointments
        )
        if available_appointments
        else "No appointments available."
    )


if __name__ == "__main__":
    asyncio.run(main())
