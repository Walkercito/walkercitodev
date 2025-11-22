import reflex as rx

from portfolio.data import Extra
from portfolio.components.heading import section_heading
from portfolio.components.card_detail import card_detail
from portfolio.styles.styles import Size


def blogs(extras: list[Extra]) -> rx.Component:
    return rx.vstack(
        section_heading("Blogs & More", "bookmark"),
        # Mobile: stack vertical con espaciado
        rx.mobile_only(
            rx.vstack(
                *[card_detail(extra) for extra in extras],
                spacing="5",
                width="100%",
            ),
        ),
        # Desktop: grid
        rx.tablet_and_desktop(
            rx.grid(
                *[card_detail(extra) for extra in extras],
                columns=rx.breakpoints(
                    initial="1",
                    sm="2",
                    md="2",
                    lg="3",
                ),
                gap="6",
                width="100%",
            ),
        ),
        spacing="4",
        width="100%",
        align="stretch",
        id="blogs",
    )
