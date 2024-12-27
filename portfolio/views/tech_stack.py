import reflex as rx

from portfolio.styles.styles import EmSize, Size

from portfolio.data import Tech
from portfolio.components.heading import heading


def tech_stack(technologies: list[Tech]) -> rx.Component:
    return rx.vstack(
        heading("Technologies"),
        rx.flex(
            rx.foreach(
                technologies,
                lambda tech: rx.badge(
                    rx.box(
                        class_name = tech.icon,
                        font_size = "24px"
                    ),
                    rx.text(tech.name),
                    size = "2"
                )
            ),
            wrap = "wrap",
            spacing = Size.SMALL.value
        ),
        spacing = Size.DEFAULT.value
    )