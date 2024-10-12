import asyncio
from time import sleep

from playwright.async_api import Playwright, async_playwright

from .config import Settings

settings = Settings()


async def check(playwright: Playwright):
    if not settings.appointment_id:
        raise ValueError(
            "APPOINTMENT_ID not set. Please see README.md for instructions for setting it."
        )

    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto(
        f"https://service.berlin.de/terminvereinbarung/termin/all/{settings.appointment_id}/"
    )
    sleep(5)
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await check(playwright)


if __name__ == "__main__":
    asyncio.run(main())
