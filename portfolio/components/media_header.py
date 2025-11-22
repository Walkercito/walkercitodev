import reflex as rx

from portfolio.components.icon_button import icon_button
from portfolio.data import Media
from portfolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    """Media links para el header (desktop)."""
    return rx.flex(
        icon_button(
            icon="mail",
            url=f"mailto:{data.email}",
            text=data.email,
            solid=True
        ),
        rx.hstack(
            icon_button(icon="file-text", url=data.cv),
            icon_button(icon="github", url=data.github),
            spacing="2",
        ),
        spacing="3",
        flex_direction="column",
        align="center",
    )
