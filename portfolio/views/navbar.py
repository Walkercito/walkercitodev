import reflex as rx

from portfolio.styles.color import TextColor, Color
from portfolio.styles.styles import (
    Size, EmSize, MAX_WIDTH,
    link_style, glass_navbar_style, nav_link_style, button_surface_style
)
from portfolio.components.contact_modal import contact_modal


def nav_link(text: str, href: str) -> rx.Component:
    """Link de navegación individual."""
    return rx.link(
        rx.text(text, style=nav_link_style),
        href=href,
        style=link_style,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo simple - solo texto
            rx.link(
                rx.text(
                    "Walkercito",
                    color="var(--text-primary)",
                    font_size="1.25rem",
                    font_weight="600",
                    letter_spacing="-0.02em",
                ),
                href="/",
                style=link_style,
            ),

            # Links de navegación (solo desktop)
            rx.tablet_and_desktop(
                rx.hstack(
                    nav_link("About", "#about"),
                    nav_link("Projects", "#projects"),
                    nav_link("Experience", "#experience"),
                    nav_link("Donate", "/donations/links"),
                    spacing="1",
                ),
            ),

            # Botones de acción
            rx.hstack(
                # Link de donaciones (móvil)
                rx.mobile_only(
                    rx.link(
                        rx.button(
                            rx.icon("heart", size=16),
                            style=button_surface_style,
                            size="2",
                        ),
                        href="/donations/links",
                        style=link_style,
                    ),
                ),
                # Modal de contacto
                contact_modal(),
                spacing="2",
            ),

            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            justify="between",
            align="center",
            padding_x="1.5rem",
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="1000",
        padding_y="0.75rem",
        style=glass_navbar_style,
    )
