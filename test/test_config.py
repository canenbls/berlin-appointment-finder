from berliner_buergerbot.config import Settings


def test_default_settings():
    settings = Settings(
        APPOINTMENT_ID=None,
        CHECKING_INTERVAL=90,
        PLAYWRIGHT_HEADLESS=True,
        TWILIO_ACCOUNT_SID=None,
        TWILIO_AUTH_TOKEN=None,
        TWILIO_FROM_NO_SMS=None,
        TWILIO_FROM_NO_WHATSAPP=None,
        TWILIO_TO_NO=None,
        TWILIO_WHATSAPP=True,
    )

    assert settings.appointment_id is None
    assert settings.checking_interval == 90
    assert settings.playwright_headless is True
    assert settings.twilio_account_sid is None
    assert settings.twilio_auth_token is None
    assert settings.twilio_from_no_sms is None
    assert settings.twilio_from_no_whatsapp is None
    assert settings.twilio_to_no is None
    assert settings.twilio_whatsapp is True
