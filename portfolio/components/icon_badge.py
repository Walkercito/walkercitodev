import reflex as rx

from portfolio.styles.styles import EmSize, Size
from portfolio.styles.color import TextColor, Color
from portfolio.styles.styles import icon_badge_style


def icon_badge(icon: str) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            font_size = EmSize.HALF.value,
        ),
        style = icon_badge_style,
        aspect_ratio = "1",
        padding = EmSize.DEFAULT.value,
    )