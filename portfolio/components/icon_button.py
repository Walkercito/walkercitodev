import reflex as rx

from portfolio.styles.styles import button_solid_style, button_surface_style, kofi_button_style
from portfolio.styles.color import Color, TextColor

def icon_button(icon: str, url: str, text: str = "", solid: bool = False, is_kofi: bool = False) -> rx.Component:
    button_style = kofi_button_style if is_kofi else (button_solid_style if solid else button_surface_style)

    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    icon,
                    font_size="1.2em",
                    align_self="center",
                ),
                *([rx.text(text, align_self="center")] if text else []),
                spacing = "2",
                align_items = "center",
                justify_content = "center",
            ),
            style = button_style,
        ),
        href = url,
        is_external = True,
    )