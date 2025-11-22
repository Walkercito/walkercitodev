import reflex as rx

from portfolio.components.icon_button import icon_button, social_icon
from portfolio.data import Media
from portfolio.styles.styles import Size, glass_base
from portfolio.styles.color import TextColor, Color


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        # Contenido del footer
        rx.vstack(
            # CTA de contacto
            rx.vstack(
                rx.text(
                    "Let's work together",
                    font_size="1.5rem",
                    font_weight="600",
                    color="var(--text-primary)",
                    class_name="gradient-text",
                ),
                rx.text(
                    "Have a project in mind? Let's create something amazing.",
                    font_size="0.9rem",
                    color="var(--text-secondary)",
                    text_align="center",
                ),
                spacing="2",
                align="center",
            ),

            # Botones de acción principales
            rx.hstack(
                icon_button(
                    "mail",
                    f"mailto:{data.email}",
                    "Get in Touch",
                    solid=True,
                ),
                icon_button(
                    "coffee",
                    data.kofi,
                    "Support Me",
                    is_kofi=True,
                ),
                spacing="3",
                justify="center",
                flex_wrap="wrap",
            ),

            # Social links
            rx.hstack(
                social_icon("github", data.github, "GitHub"),
                social_icon("linkedin", data.linkedin, "LinkedIn"),
                social_icon("twitter", data.twitter, "X"),
                social_icon("message-circle", data.discord, "Discord"),
                social_icon("send", data.telegram, "Telegram"),
                social_icon("file-text", data.cv, "Resume"),
                spacing="2",
                justify="center",
                flex_wrap="wrap",
            ),

            spacing="6",
            align="center",
            padding_y="2rem",
        ),

        # Copyright
        rx.hstack(
            rx.text(
                "Made with",
                font_size="0.8rem",
                color="var(--text-tertiary)",
            ),
            rx.icon("heart", size=14, color=Color.ACCENT_PINK.value),
            rx.text(
                "by Walkercito",
                font_size="0.8rem",
                color="var(--text-tertiary)",
            ),
            rx.text(
                " | ",
                font_size="0.8rem",
                color="var(--text-muted)",
            ),
            rx.text(
                "Built with Reflex",
                font_size="0.8rem",
                color="var(--text-tertiary)",
            ),
            spacing="1",
            align="center",
            justify="center",
            flex_wrap="wrap",
            padding_bottom="1.5rem",
        ),
        spacing="4",
        width="100%",
        align="center",
        id="contact",
    )
