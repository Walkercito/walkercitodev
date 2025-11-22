import reflex as rx

from portfolio.components.heading import heading, subtitle
from portfolio.components.icon_button import icon_button, social_icon
from portfolio.data import Data, Media
from portfolio.styles.styles import Size, EmSize, avatar_style
from portfolio.styles.color import TextColor, Color


def hero_media_buttons(data: Media) -> rx.Component:
    """Botones de acción principales del hero."""
    return rx.hstack(
        icon_button(
            icon="mail",
            url=f"mailto:{data.email}",
            text="Contact Me",
            solid=True,
        ),
        icon_button(
            icon="file-text",
            url=data.cv,
            text="Resume",
        ),
        spacing="3",
        flex_wrap="wrap",
        justify="center",
    )


def hero_social_links(data: Media) -> rx.Component:
    """Links de redes sociales."""
    return rx.hstack(
        social_icon("github", data.github, "GitHub"),
        social_icon("linkedin", data.linkedin, "LinkedIn"),
        social_icon("message-circle", data.discord, "Discord"),
        social_icon("send", data.telegram, "Telegram"),
        social_icon("coffee", data.kofi, "Ko-fi"),
        spacing="2",
        justify="center",
    )


def status_badge() -> rx.Component:
    """Badge de estado disponible."""
    return rx.hstack(
        rx.box(
            width="8px",
            height="8px",
            border_radius="full",
            background=Color.SUCCESS.value,
            class_name="animate-pulse-dot",
        ),
        rx.text(
            "Available for work",
            font_size="0.875rem",
            color="var(--text-secondary)",
        ),
        spacing="2",
        align="center",
        padding="0.5rem 1rem",
        border_radius="full",
        background="rgba(16, 185, 129, 0.1)",
        border="1px solid rgba(16, 185, 129, 0.2)",
    )


def header(data: Data) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Avatar
            rx.avatar(
                src=data.avatar,
                size="9",
                radius="full",
                style=avatar_style,
            ),

            # Status badge
            status_badge(),

            # Nombre con gradiente
            heading(data.name, h1=True, gradient=True),

            # Skill/profesión
            subtitle(data.skill),

            # Ubicación
            rx.hstack(
                rx.icon("map-pin", size=16, color="var(--text-tertiary)"),
                rx.text(
                    data.location,
                    color="var(--text-tertiary)",
                    font_size="0.9rem",
                ),
                spacing="2",
                align="center",
            ),

            # Botones de acción
            hero_media_buttons(data.media),

            # Social links
            hero_social_links(data.media),

            spacing="4",
            align="center",
            width="100%",
            padding_top="5rem",  # Espacio para navbar fixed
            padding_bottom="2rem",
        ),
        width="100%",
        id="hero",
    )
