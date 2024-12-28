import reflex as rx

from portfolio.styles.color import TextColor, Color
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.styles import link_style


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.text(
                    "Walkercito",
                    color = TextColor.PRIMARY.value,
                    font_size = EmSize.HALF.value,
                    font_weight = "light",
                    letter_spacing = "wider",
                    width = "100%",
                ),
                href = "/",
                style = link_style,
            ),
            width = "100%",
            margin_x = "auto",
            max_width = "7xl",
            justify = "between",
        ),
        top = "0",
        width = "100%",
        z_index = "999",
        position = "sticky",
        padding_y = EmSize.DEFAULT.value,
        padding_x = EmSize.HALF.value,
        background_color = Color.BACKGROUND.value,
        border_bottom = f"1px solid {Color.BORDER.value}",
    )