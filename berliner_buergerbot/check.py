import asyncio
import re

from playwright.async_api import Locator, async_playwright
from pydantic import BaseModel


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


async def check_available_appointments(
    url: str, playwright_headless: bool
) -> list[Appointment] | None:
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=playwright_headless)
        page = await browser.new_page()
        await page.goto(url)

        td_elements = await page.locator("td.buchbar").all()
        tasks = [extract_appointment(td) for td in td_elements]
        results = await asyncio.gather(*tasks)
        available_appointments = [result for result in results if result is not None]

        await browser.close()

    return available_appointments or None
