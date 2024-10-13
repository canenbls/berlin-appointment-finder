from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest
from playwright.async_api import Locator

from berliner_buergerbot.check import (
    Appointment,
    check_available_appointments,
    extract_appointment,
)


@pytest.fixture
def mock_locator():
    return MagicMock(spec=Locator)


@pytest.mark.asyncio
async def test_extract_appointment(mock_locator: MagicMock):
    mock_locator.locator.return_value = mock_locator
    mock_locator.get_attribute = AsyncMock(
        side_effect=["12.12.2024 - Example", "https://example.com"]
    )
    result = await extract_appointment(mock_locator)
    assert result == Appointment(date="12.12.2024", href="https://example.com")


@pytest.mark.asyncio
async def test_extract_appointment_no_title(mock_locator: MagicMock):
    mock_locator.locator.return_value = mock_locator
    mock_locator.get_attribute = AsyncMock(side_effect=[None, "https://example.com"])
    result = await extract_appointment(mock_locator)
    assert result is None


@pytest.mark.asyncio
async def test_extract_appointment_no_href(mock_locator: MagicMock):
    mock_locator.locator.return_value = mock_locator
    mock_locator.get_attribute = AsyncMock(side_effect=["12.12.2024 - Example", None])
    result = await extract_appointment(mock_locator)
    assert result is None


@pytest.mark.asyncio
async def test_extract_appointment_no_date(mock_locator: MagicMock):
    mock_locator.locator.return_value = mock_locator
    mock_locator.get_attribute = AsyncMock(
        side_effect=["No Date", "https://example.com"]
    )
    result = await extract_appointment(mock_locator)
    assert result is None


@pytest.mark.asyncio
async def test_check_available_appointments_no_appointment():
    taken_html_file_path = Path(__file__).parent / "fixtures" / "Taken.html"
    result = await check_available_appointments(
        f"file://{str(taken_html_file_path)}", True
    )
    assert result is None


@pytest.mark.asyncio
async def test_check_available_appointments_single_appointment():
    taken_html_file_path = Path(__file__).parent / "fixtures" / "Day.html"
    result = await check_available_appointments(
        f"file://{str(taken_html_file_path)}", True
    )
    assert result == [
        Appointment(
            date="12.12.2024",
            href="https://service.berlin.de/terminvereinbarung/termin/time/1733958000/",
        )
    ]
