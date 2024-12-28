import reflex as rx

from portfolio.data import Extra
from portfolio.components.heading import heading
from portfolio.components.card_detail import card_detail
from portfolio.styles.styles import Size


def blogs(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        heading("Blogs"),
        rx.mobile_only(
            rx.vstack(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing = Size.DEFAULT.value
            ),
            width = "100%"
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *[
                    card_detail(extra)
                    for extra in extras
                ],
                spacing = Size.DEFAULT.value,
                columns = "3",
                template_columns = "repeat(3, 1fr)",
                gap = Size.DEFAULT.value,
            ),
            width = "100%"
        ),
        spacing = Size.DEFAULT.value,
        width = "100%"
    )