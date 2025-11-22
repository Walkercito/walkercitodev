import reflex as rx

from portfolio import data
from portfolio.views.navbar import navbar
from portfolio.views.footer import footer
from portfolio.components.heading import section_heading

from portfolio.styles.styles import MAX_WIDTH, divider_style, glass_card_style
from portfolio.styles.color import Color, TextColor

DATA = data.data


def ArcadiaBlog() -> rx.Component:
    return rx.box(
        # Efectos de fondo
        rx.box(
            position="fixed",
            top="-20%",
            right="-10%",
            width="500px",
            height="500px",
            border_radius="50%",
            background="radial-gradient(circle, rgba(6, 182, 212, 0.15) 0%, transparent 70%)",
            filter="blur(60px)",
            pointer_events="none",
            z_index="-1",
        ),

        navbar(),

        rx.center(
            rx.vstack(
                # Espaciado para navbar fixed
                rx.box(height="4rem"),

                section_heading("ArcadiaNET Blog", "book-open"),

                # Placeholder para contenido del blog
                rx.box(
                    rx.vstack(
                        rx.icon("construction", size=48, color=TextColor.TERTIARY.value),
                        rx.text(
                            "Coming Soon",
                            font_size="1.5rem",
                            font_weight="600",
                            color=TextColor.PRIMARY.value,
                        ),
                        rx.text(
                            "This blog post is currently under construction. Check back soon!",
                            color=TextColor.SECONDARY.value,
                            text_align="center",
                        ),
                        spacing="4",
                        align="center",
                        padding="3rem",
                    ),
                    style=glass_card_style,
                    width="100%",
                ),

                rx.box(style=divider_style, width="100%"),

                footer(DATA.media),

                spacing="6",
                padding_x="1.5rem",
                padding_y="2rem",
                max_width=MAX_WIDTH,
                width="100%",
            ),
        ),

        min_height="100vh",
        background_color=Color.BACKGROUND.value,
    )
