import reflex as rx

from portfolio.data import Extra

from portfolio.styles.styles import IMAGE_HEIGHT, Size, EmSize
from portfolio.styles.color import TextColor, Color
from portfolio.styles.styles import card_style, description_style, text_content_style


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.vstack(
                rx.image(
                    src = extra.image,
                    height = IMAGE_HEIGHT,
                    width = "100%",
                    object_fit = "cover",
                    border_radius = f"{EmSize.SMALL.value} {EmSize.SMALL.value} {EmSize.SMALL.value} {EmSize.SMALL.value}",  # Redondear solo las esquinas superiores
                ),
                rx.vstack(
                    rx.text.strong(
                        extra.title,
                        color = TextColor.PRIMARY.value,
                    ),
                    rx.text(
                        extra.description,
                        color = TextColor.SECONDARY.value,
                        size = Size.SMALL.value,
                    ),
                    style = text_content_style,
                    align_items = "start",
                    width = "100%",
                    spacing = Size.SMALL.value,
                ),
                spacing = "0",
                align_items = "start",
                width = "100%",
            ),
            _hover = {
                "text_decoration": "none",
            }
        ),
        style = card_style,
        width = "100%",
        href = extra.url,
        is_external = False,
    )