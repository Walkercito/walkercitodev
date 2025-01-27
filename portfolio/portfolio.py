import reflex as rx

from portfolio import data
from portfolio.views.navbar import navbar
from portfolio.views.header import header
from portfolio.views.about import about
from portfolio.views.tech_stack import tech_stack
from portfolio.views.info import info
from portfolio.views.extra import blogs
from portfolio.views.footer import footer

from portfolio.styles.styles import MAX_WIDTH, BASE_STYLE, STYLESHEETS
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.color import TextColor, Color

from portfolio.pages.blogs.arcadianet_blog import ArcadiaBlog


DATA = data.data

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(

            rx.vstack(
                header(DATA),
                about(DATA.about),
                rx.divider(),
                tech_stack(DATA.technologies),
                info("Experience", DATA.experience),
                info("Projects", DATA.projects),
                info("Studies", DATA.training),
                blogs(DATA.extras),
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


app = rx.App(
    stylesheets = STYLESHEETS,
    style = BASE_STYLE,
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title = title,
    description = description,
    image = image,
    meta = [
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
app.add_page(
    ArcadiaBlog,
    title = "Blog: ArcadiaNET",
    description = "Blog about ArcadiaNET's project",
    route = "/blogs/arcadianet_blog"
)
