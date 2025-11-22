import reflex as rx

from portfolio.data import Extra
from portfolio.styles.styles import IMAGE_HEIGHT, Size, EmSize, project_card_style, link_style
from portfolio.styles.color import TextColor, Color


def card_detail(extra: Extra) -> rx.Component:
    return rx.link(
        rx.box(
            # Imagen con overlay gradient
            rx.box(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover",
                    transition="transform 0.4s ease",
                ),
                # Gradient overlay
                rx.box(
                    position="absolute",
                    bottom="0",
                    left="0",
                    right="0",
                    height="50%",
                    background="linear-gradient(to top, rgba(10, 10, 15, 0.9), transparent)",
                    pointer_events="none",
                ),
                position="relative",
                overflow="hidden",
                _hover={
                    "& img": {
                        "transform": "scale(1.05)",
                    }
                },
            ),

            # Contenido de texto
            rx.vstack(
                rx.text(
                    extra.title,
                    font_weight="600",
                    font_size="1.1rem",
                    color=TextColor.PRIMARY.value,
                ),
                rx.text(
                    extra.description,
                    font_size="0.875rem",
                    color=TextColor.SECONDARY.value,
                    line_height="1.5",
                ),
                rx.hstack(
                    rx.text(
                        "Read more",
                        font_size="0.8rem",
                        color=Color.ACCENT_PRIMARY.value,
                        font_weight="500",
                    ),
                    rx.icon("arrow-right", size=14, color=Color.ACCENT_PRIMARY.value),
                    spacing="1",
                    align="center",
                    transition="transform 0.2s ease",
                    _group_hover={
                        "transform": "translateX(4px)",
                    },
                ),
                spacing="2",
                align="start",
                padding="1.25rem",
            ),
            style=project_card_style,
            role="group",
        ),
        href=extra.url,
        style=link_style,
        is_external=True,
    )
