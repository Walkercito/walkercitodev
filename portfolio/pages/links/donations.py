import reflex as rx

from portfolio import data
from portfolio.views.navbar import navbar
from portfolio.views.footer import footer
from portfolio.components.heading import section_heading
from portfolio.components.card_donate import card_donate

from portfolio.styles.styles import MAX_WIDTH, divider_style
from portfolio.styles.color import Color, TextColor

DATA = data.data


def Donations() -> rx.Component:
    return rx.box(
        navbar(),

        rx.box(
            rx.vstack(
                # Espaciado para navbar fixed
                rx.box(height="5rem"),

                # Header section
                rx.vstack(
                    rx.icon("heart", size=40, color=Color.ACCENT_PINK.value),
                    rx.heading(
                        "Support My Work",
                        font_size="2rem",
                        font_weight="700",
                        color=TextColor.PRIMARY.value,
                        text_align="center",
                    ),
                    rx.text(
                        "If you find my work helpful, consider supporting me through cryptocurrency donations.",
                        color=TextColor.SECONDARY.value,
                        text_align="center",
                        max_width="500px",
                        font_size="1rem",
                        line_height="1.6",
                    ),
                    spacing="3",
                    align="center",
                    margin_bottom="2rem",
                ),

                # Cards de donación
                card_donate(DATA.donations),

                # Espaciador
                rx.box(height="2rem"),

                # Footer
                footer(DATA.media),

                spacing="4",
                padding_x="1.5rem",
                padding_bottom="2rem",
                max_width=MAX_WIDTH,
                width="100%",
                margin_x="auto",
                align="center",
            ),
            width="100%",
        ),

        min_height="100vh",
        background_color=Color.BACKGROUND.value,
    )
