import reflex as rx

from portfolio.data import Donations
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.color import TextColor, Color
from portfolio.styles.styles import card_style, text_content_style


def card_donate(donations: list[Donations]) -> rx.Component:
    return rx.grid(
        *[
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.icon(
                                d.icon,
                                size=20,
                                color=TextColor.PRIMARY.value,
                            ),
                            width="40px",
                            height="40px",
                            border_radius="50%",
                            background=TextColor.SECONDARY.value,
                            display="flex",
                            align_items="center",
                            justify_content="center",
                        ),
                        rx.text.strong(
                            d.title,
                            color=TextColor.PRIMARY.value,
                            size=Size.DEFAULT.value,
                        ),
                        align_items="center",
                        spacing=Size.SMALL.value,
                        width="100%",
                        justify_content="space-between",
                    ),
                    rx.text(
                        d.description,
                        color=TextColor.SECONDARY.value,
                        size=Size.SMALL.value,
                        line_height="1.5",
                    ),
                    rx.button(
                        rx.hstack(
                            rx.icon("copy", size=16),
                            rx.text(
                                f"Copy",
                                size=Size.SMALL.value
                            ),
                            spacing=Size.SMALL.value,
                            align_items="center",
                        ),
                        width="100%",
                        variant="outline",
                        on_click=rx.set_clipboard(d.value),
                    ),
                    
                    spacing=Size.MEDIUM.value,
                    align_items="start",
                    width="100%",
                    style=text_content_style,
                ),
                style=card_style,
                width="100%",
                height="fit-content",
            ) for d in donations
        ],
        columns=rx.breakpoints(
            initial="1",   
            sm="2",      
            md="2",       
            lg="3",      
            xl="4",   
        ),
        gap=Size.BIG.value,
        width="100%",
    )