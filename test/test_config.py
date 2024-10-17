from unittest.mock import patch

from app.config import Settings


def test_default_settings():
    with patch.dict(Settings.model_config, {"env_file": None}):
        settings = Settings()

        assert settings.appointment_id is None
        assert settings.checking_interval == 90
        assert settings.playwright_headless is True
        assert settings.twilio_account_sid is None
        assert settings.twilio_auth_token is None
        assert settings.twilio_from_no_sms is None
        assert settings.twilio_from_no_whatsapp is None
        assert settings.twilio_to_no is None
        assert settings.twilio_use_whatsapp is True
