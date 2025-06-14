import reflex as rx

from portfolio.data import Donations
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.color import TextColor, Color
from portfolio.styles.styles import card_style, description_style, text_content_style


def card_donate(donations: list[Donations]) -> rx.Component:
    return rx.vstack(
        *[
            rx.card(
                rx.link(
                    rx.vstack(
                        rx.vstack(
                            rx.hstack(
                                rx.text.strong(
                                    d.title,
                                    color=TextColor.PRIMARY.value,
                                ),
                            ),
                            rx.text(
                                d.description,
                                color=TextColor.SECONDARY.value,
                                size=Size.SMALL.value,
                            ),
                            style=text_content_style,
                            align_items="start",
                            width="100%",
                            spacing=Size.SMALL.value,
                        ),
                        spacing="0",
                        align_items="start",
                        width="100%",
                    ),
                    href=d.value,
                    _hover={"text_decoration": "none"},
                ),
                style=card_style,
                width="100%",
            ) for d in donations
        ]
    )

