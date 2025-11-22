import reflex as rx

from portfolio.components.icon_button import icon_button, social_icon
from portfolio.data import Media
from portfolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    """Media links para el footer."""
    return rx.flex(
        icon_button(
            icon="mail",
            url=f"mailto:{data.email}",
            text=data.email,
            solid=True
        ),
        icon_button(
            icon="coffee",
            url=data.kofi,
            text="Donate",
            is_kofi=True
        ),
        rx.hstack(
            social_icon("file-text", data.cv, "Resume"),
            social_icon("github", data.github, "GitHub"),
            social_icon("linkedin", data.linkedin, "LinkedIn"),
            social_icon("twitter", data.twitter, "Twitter"),
            social_icon("send", data.telegram, "Telegram"),
            spacing="2",
        ),
        spacing="3",
        flex_direction="column",
        align="center",
        justify="center",
    )
