from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    appointment_id: int | None = Field(default=None, alias="APPOINTMENT_ID")
    checking_interval: int = Field(default=90, alias="CHECKING_INTERVAL")
    playwright_headless: bool = Field(default=True, alias="PLAYWRIGHT_HEADLESS")
    twilio_account_sid: str | None = Field(default=None, alias="TWILIO_ACCOUNT_SID")
    twilio_auth_token: str | None = Field(default=None, alias="TWILIO_AUTH_TOKEN")
    twilio_from_no_sms: str | None = Field(default=None, alias="TWILIO_FROM_NO_SMS")
    twilio_from_no_whatsapp: str | None = Field(
        default=None, alias="TWILIO_FROM_NO_WHATSAPP"
    )
    twilio_to_no: str | None = Field(default=None, alias="TWILIO_TO_NO")
    twilio_whatsapp: bool = Field(default=True, alias="TWILIO_WHATSAPP")
