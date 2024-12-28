import reflex as rx

from portfolio.styles.styles import EmSize, Size
from portfolio.data import Tech
from portfolio.components.heading import heading
from portfolio.styles.styles import tech_badge_style


def tech_stack(technologies: list[Tech]) -> rx.Component:
    return rx.vstack(
        heading("Technologies"),
        rx.box(
            rx.flex(
                rx.foreach(
                    technologies,
                    lambda tech: rx.box(
                        rx.badge(
                            rx.hstack(
                                rx.box(
                                    class_name = tech.icon,
                                    font_size = "1.5em",
                                    align_self = "center",
                                ),
                                rx.text(
                                    tech.name,
                                    align_self = "center",
                                ),
                                spacing = "2",
                                align_items = "start",
                            ),
                            style = tech_badge_style,
                            size = "2"
                        ),
                        padding = "0.5em",  # Añade padding alrededor de cada badge
                    )
                ),
                wrap = "wrap",
                gap = Size.DEFAULT.value,
                justify_content = "center",
                style = {
                    "display": "flex",
                    "flex_wrap": "wrap",
                    "gap": "1rem",
                    "padding": "1rem",
                }
            ),
            width = "100%",
        ),
        spacing = Size.DEFAULT.value,
        align_items = "stretch",
        width = "100%"
    )