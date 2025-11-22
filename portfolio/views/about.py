import reflex as rx

from portfolio.components.heading import section_heading
from portfolio.styles.styles import glass_card_style, description_style
from portfolio.styles.color import TextColor, Color


def about(description: str) -> rx.Component:
    return rx.vstack(
        section_heading("About Me", "user"),
        rx.box(
            rx.text(
                description,
                style={
                    **description_style,
                    "line_height": "1.8",
                }
            ),
            style=glass_card_style,
            padding="1.5rem",
            width="100%",
        ),
        spacing="4",
        width="100%",
        align="stretch",
        id="about",
    )
