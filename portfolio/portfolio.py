import reflex as rx

from portfolio import data
from portfolio.views.navbar import navbar
from portfolio.views.header import header

from portfolio.styles.styles import MAX_WIDTH
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.color import TextColor, Color


DATA = data.data

def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.box(
                rx.center(
                    header(DATA),
                ),
                width = "100%",
                height = "100vh",
                max_width = MAX_WIDTH,
                padding_x = EmSize.HALF.value,
                padding_y = EmSize.HALF.value,
            )
        ),
        spacing = "0",
        width = "100%",
        height = "100vh",
    )


app = rx.App()
app.add_page(index, route = "/")