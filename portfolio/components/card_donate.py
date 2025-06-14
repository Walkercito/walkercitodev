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
                            background=f"rgba({hex_to_rgb(d.color)}, 0.2)",
                            border=f"2px solid rgba({hex_to_rgb(d.color)}, 0.4)",
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
                        variant="surface",
                        on_click=rx.set_clipboard(d.value),
                        style={
                            "background": f"rgba({hex_to_rgb(d.color)}, 0.1)",
                            "border": f"1px solid rgba({hex_to_rgb(d.color)}, 0.3)",
                            "color": TextColor.PRIMARY.value,
                            "transition": "all 0.2s",
                            "_hover": {
                                "background": f"rgba({hex_to_rgb(d.color)}, 0.2)",
                                "transform": "scale(1.02)",
                            },
                        },
                    ),
                    
                    spacing=Size.MEDIUM.value,
                    align_items="start",
                    width="100%",
                    style=text_content_style,
                ),
                style={
                    **card_style,
                    "background": f"linear-gradient(135deg, rgba({hex_to_rgb(d.color)}, 0.03) 0%, rgba(255, 255, 255, 0.02) 100%)",
                    "border": f"1px solid rgba({hex_to_rgb(d.color)}, 0.2)",
                    "border_radius": EmSize.SMALL.value,
                    "overflow": "hidden",
                },
                width="100%",
            ) for d in donations
        ],
        columns=rx.breakpoints(
            initial="1", 
            sm="1",     
            md="2",    
            lg="3",     
        ),
        gap=Size.MEDIUM.value,
        width="100%",
    )


def hex_to_rgb(hex_color: str) -> str:
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"{r}, {g}, {b}"