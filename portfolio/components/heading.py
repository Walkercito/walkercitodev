import reflex as rx

from portfolio.styles.styles import Size, heading_style, subheading_style
from portfolio.styles.color import TextColor, Color


def heading(text: str, h1: bool = False, gradient: bool = False) -> rx.Component:
    """Componente de heading reutilizable con soporte para gradiente."""
    if gradient:
        return rx.heading(
            text,
            as_="h1" if h1 else "h2",
            size=Size.BIG.value if h1 else Size.MEDIUM.value,
            class_name="gradient-text",
            style={
                **heading_style,
                "font_size": "3rem" if h1 else "1.5rem",
            }
        )
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size=Size.BIG.value if h1 else Size.MEDIUM.value,
        style={
            **heading_style,
            "font_size": "3rem" if h1 else "1.5rem",
        }
    )


def section_heading(text: str, icon: str = None) -> rx.Component:
    """Heading para secciones con icono opcional y línea decorativa."""
    return rx.hstack(
        rx.box(
            width="40px",
            height="2px",
            background=Color.GRADIENT_PRIMARY.value,
            border_radius="full",
        ),
        rx.hstack(
            rx.icon(icon, size=20, color=Color.ACCENT_PRIMARY.value) if icon else rx.fragment(),
            rx.heading(
                text,
                as_="h2",
                size=Size.MEDIUM.value,
                style={
                    **heading_style,
                    "font_size": "1.75rem",
                }
            ),
            spacing="3",
            align="center",
        ),
        rx.box(
            flex="1",
            height="2px",
            background=f"linear-gradient(90deg, {Color.ACCENT_PRIMARY.value}, transparent)",
            border_radius="full",
        ),
        spacing="4",
        align="center",
        width="100%",
        margin_bottom="2rem",
    )


def subtitle(text: str) -> rx.Component:
    """Subtítulo estilizado."""
    return rx.text(
        text,
        style=subheading_style,
        font_size="1.125rem",
    )
