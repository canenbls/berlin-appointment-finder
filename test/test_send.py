from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from app.send import send_message


@pytest.fixture
def mock_twilio(mocker: MockerFixture):
    mock_client = MagicMock()
    mocker.patch("berliner_buergerbot.send.Client", return_value=mock_client)
    return mock_client


@pytest.mark.asyncio
async def test_send_message(mock_twilio: MagicMock):
    mock_twilio.messages.create = MagicMock(return_value=None)
    message = "Hello!"
    await send_message(message)
    mock_twilio.messages.create.assert_called_once()


@pytest.mark.asyncio
async def test_send_message_missing_setting(mocker: MockerFixture):
    mocker.patch("berliner_buergerbot.send.settings.twilio_account_sid", None)
    with pytest.raises(ValueError, match="Required Twilio settings not found."):
        await send_message("Hello!")
