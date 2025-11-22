import reflex as rx

from portfolio.styles.styles import EmSize, Size, icon_badge_style
from portfolio.styles.color import TextColor, Color


def icon_badge(icon: str) -> rx.Component:
    """Badge con icono y gradiente de fondo."""
    return rx.box(
        rx.icon(icon, size=22, color=TextColor.PRIMARY.value),
        style=icon_badge_style,
    )
