import reflex as rx

from portfolio.data import Donations
from portfolio.styles.styles import Size, EmSize, glass_card_style, button_surface_style
from portfolio.styles.color import TextColor, Color


def donate_card(donation: Donations) -> rx.Component:
    """Card individual de donación con glassmorphism."""
    return rx.box(
        rx.vstack(
            # Header con icono y título
            rx.hstack(
                rx.box(
                    rx.icon(donation.icon, size=22, color=donation.color),
                    width="48px",
                    height="48px",
                    border_radius="12px",
                    background="rgba(255, 255, 255, 0.05)",
                    border=f"1px solid {Color.BORDER_LIGHT.value}",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.vstack(
                    rx.text(
                        donation.title,
                        font_weight="600",
                        font_size="1.1rem",
                        color=TextColor.PRIMARY.value,
                    ),
                    rx.text(
                        donation.description,
                        color=TextColor.TERTIARY.value,
                        font_size="0.8rem",
                    ),
                    spacing="0",
                    align="start",
                ),
                spacing="3",
                align="center",
                width="100%",
            ),

            # Dirección/valor (truncado)
            rx.box(
                rx.text(
                    donation.value,
                    font_size="0.75rem",
                    font_family="monospace",
                    color=TextColor.SECONDARY.value,
                    overflow="hidden",
                    text_overflow="ellipsis",
                    white_space="nowrap",
                ),
                width="100%",
                padding="0.875rem",
                background="rgba(255, 255, 255, 0.03)",
                border_radius="10px",
                border=f"1px solid {Color.BORDER.value}",
            ),

            # Botón de copiar
            rx.button(
                rx.hstack(
                    rx.icon("copy", size=16),
                    rx.text("Copy Address"),
                    spacing="2",
                    align="center",
                ),
                style=button_surface_style,
                width="100%",
                on_click=rx.set_clipboard(donation.value),
            ),

            spacing="4",
            width="100%",
        ),
        style=glass_card_style,
        width="100%",
    )


def card_donate(donations: list[Donations]) -> rx.Component:
    """Grid de tarjetas de donación."""
    return rx.vstack(
        *[donate_card(d) for d in donations],
        spacing="5",
        width="100%",
    )
