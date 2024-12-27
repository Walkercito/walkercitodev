import reflex as rx

from portfolio.styles.styles import button_solid_style, button_surface_style, button_base_style


def icon_button(icon: str, url: str, text: str = "", solid: bool = False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    icon,
                    font_size = "1.2em", 
                    align_self = "center", 
                ),
                *([rx.text(text, align_self="center")] if text else []), 
                spacing = "2",
                align_items = "center", 
                justify_content = "center", 
            ),
            style = button_solid_style if solid else button_surface_style,
        ),
        href = url,
        is_external = True,
    )