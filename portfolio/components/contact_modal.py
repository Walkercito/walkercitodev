import reflex as rx

from portfolio.styles.styles import button_solid_style, button_surface_style
from portfolio.styles.color import TextColor, Color


def contact_modal() -> rx.Component:
    """Modal de contacto para email."""
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("mail", size=16),
                rx.tablet_and_desktop(rx.text("Contact")),
                style=button_surface_style,
                size="2",
            ),
        ),
        rx.dialog.content(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.box(
                        rx.icon("mail", size=32, color="#EA4335"),
                        width="64px",
                        height="64px",
                        border_radius="16px",
                        background="rgba(234, 67, 53, 0.1)",
                        border="1px solid rgba(234, 67, 53, 0.2)",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                    ),
                    rx.text(
                        "Send me an email",
                        font_size="1.5rem",
                        font_weight="700",
                        color=TextColor.PRIMARY.value,
                    ),
                    rx.text(
                        "I'll get back to you as soon as possible!",
                        color=TextColor.SECONDARY.value,
                        font_size="0.95rem",
                        text_align="center",
                    ),
                    spacing="3",
                    align="center",
                ),

                # Email display
                rx.box(
                    rx.text(
                        "walkercitoliver@gmail.com",
                        font_size="1rem",
                        font_family="monospace",
                        color=TextColor.PRIMARY.value,
                    ),
                    width="100%",
                    padding="1rem",
                    background="rgba(255, 255, 255, 0.03)",
                    border_radius="12px",
                    border=f"1px solid {Color.BORDER.value}",
                    text_align="center",
                ),

                # Botones
                rx.hstack(
                    rx.button(
                        rx.icon("copy", size=16),
                        rx.text("Copy"),
                        style=button_surface_style,
                        on_click=rx.set_clipboard("walkercitoliver@gmail.com"),
                    ),
                    rx.link(
                        rx.button(
                            rx.icon("send", size=16),
                            rx.text("Send Email"),
                            style=button_solid_style,
                        ),
                        href="mailto:walkercitoliver@gmail.com",
                        is_external=True,
                    ),
                    spacing="3",
                    width="100%",
                    justify="center",
                ),

                spacing="5",
                width="100%",
                align="center",
            ),
            rx.dialog.close(
                rx.button(
                    rx.icon("x", size=18),
                    position="absolute",
                    top="1rem",
                    right="1rem",
                    background="transparent",
                    color=TextColor.SECONDARY.value,
                    border="none",
                    cursor="pointer",
                    _hover={
                        "color": TextColor.PRIMARY.value,
                    },
                ),
            ),
            style={
                "background": Color.BACKGROUND_SECONDARY.value,
                "border": f"1px solid {Color.BORDER_LIGHT.value}",
                "border_radius": "20px",
                "padding": "2rem",
                "max_width": "380px",
                "width": "90vw",
            },
        ),
    )
