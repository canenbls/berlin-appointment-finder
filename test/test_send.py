from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from app.send import send_message


@pytest.fixture
def mock_twilio(mocker: MockerFixture):
    mock_client = MagicMock()
    mocker.patch("app.send.Client", return_value=mock_client)
    return mock_client


@pytest.mark.asyncio
async def test_send_message(mock_twilio: MagicMock, mocker: MockerFixture):
    mocker.patch("app.send.settings.twilio_account_sid", "fake_sid")
    mocker.patch("app.send.settings.twilio_auth_token", "fake_auth_token")
    mocker.patch("app.send.settings.twilio_from_no_whatsapp", "fake_whatsapp_no")
    mocker.patch("app.send.settings.twilio_to_no", "fake_to_no")
    mock_twilio.messages.create = MagicMock(return_value=None)
    message = "Hello!"
    await send_message(message)
    mock_twilio.messages.create.assert_called_once()


@pytest.mark.asyncio
async def test_send_message_missing_setting(mocker: MockerFixture):
    mocker.patch("app.send.settings.twilio_account_sid", None)
    with pytest.raises(ValueError, match="Required Twilio settings not found."):
        await send_message("Hello!")
