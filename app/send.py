from twilio.rest import Client  # type: ignore[import]

from .config import Settings

settings = Settings()


async def send_message(message: str) -> None:
    if not (
        settings.twilio_account_sid
        and settings.twilio_auth_token
        and (
            settings.twilio_from_no_whatsapp
            if settings.twilio_use_whatsapp
            else settings.twilio_from_no_sms
        )
        and settings.twilio_to_no
    ):
        raise ValueError(
            "Required Twilio settings not found. Please see README.md for instructions on how to set them."
        )

    from_no = (
        f"whatsapp:{settings.twilio_from_no_whatsapp}"
        if settings.twilio_use_whatsapp
        else settings.twilio_from_no_sms
    )
    to_no = (
        f"whatsapp:{settings.twilio_to_no}"
        if settings.twilio_use_whatsapp
        else settings.twilio_to_no
    )

    client = Client(settings.twilio_account_sid, settings.twilio_auth_token)
    client.messages.create(
        from_=from_no,
        to=to_no,  # type: ignore[arg-type]
        body=message,
    )
