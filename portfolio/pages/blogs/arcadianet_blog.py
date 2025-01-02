import reflex as rx

from portfolio import data
from portfolio.views.navbar import navbar
from portfolio.views.footer import footer

from portfolio.styles.styles import MAX_WIDTH, BASE_STYLE, STYLESHEETS
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.color import TextColor, Color


DATA = data.data

def ArcadiaBlog() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.divider(),
                footer(DATA.media),
                spacing = Size.MEDIUM.value,
                padding_x = EmSize.MEDIUM.value,
                padding_y = EmSize.BIG.value,
                max_width = MAX_WIDTH,
                width = "100%"
            )
        )
    )