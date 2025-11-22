import reflex as rx

from portfolio import data
from portfolio.views.navbar import navbar
from portfolio.views.header import header
from portfolio.views.about import about
from portfolio.views.tech_stack import tech_stack
from portfolio.views.info import info
from portfolio.views.extra import blogs
from portfolio.views.footer import footer

from portfolio.styles.styles import MAX_WIDTH, BASE_STYLE, STYLESHEETS, CUSTOM_CSS
from portfolio.styles.styles import Size, EmSize
from portfolio.styles.color import TextColor, Color

from portfolio.pages.blogs.arcadianet_blog import ArcadiaBlog
from portfolio.pages.links.donations import Donations

DATA = data.data


def custom_divider() -> rx.Component:
    """Divider personalizado con gradiente."""
    return rx.box(
        height="1px",
        width="100%",
        background=f"linear-gradient(90deg, transparent 0%, {Color.BORDER_LIGHT.value} 50%, transparent 100%)",
        margin_y="2rem",
    )


def index() -> rx.Component:
    return rx.box(
        # Navbar flotante
        navbar(),

        # Contenido principal centrado
        rx.box(
            rx.vstack(
                header(DATA),
                custom_divider(),
                about(DATA.about),
                custom_divider(),
                tech_stack(DATA.technologies),
                custom_divider(),
                info("Experience", DATA.experience, icon="briefcase", section_id="experience"),
                custom_divider(),
                info("Projects", DATA.projects, icon="code", section_id="projects"),
                custom_divider(),
                info("Studies", DATA.training, icon="graduation-cap", section_id="studies"),
                custom_divider(),
                blogs(DATA.extras),
                custom_divider(),
                footer(DATA.media),
                spacing="0",
                width="100%",
                max_width=MAX_WIDTH,
                margin_x="auto",
                padding_x="1.5rem",
                padding_bottom="2rem",
            ),
            width="100%",
        ),
        min_height="100vh",
        background_color=Color.BACKGROUND.value,
    )


# Stylesheets
CUSTOM_STYLESHEETS = [
    *STYLESHEETS,
]

app = rx.App(
    stylesheets=CUSTOM_STYLESHEETS,
    style=BASE_STYLE,
    head_components=[
        # Google Fonts - Inter
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="anonymous",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
        # CSS personalizado inline
        rx.el.style(CUSTOM_CSS),
    ],
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image},
        {"name": "theme-color", "content": "#0a0a0f"},
    ]
)

app.add_page(
    ArcadiaBlog,
    title="Blog: ArcadiaNET",
    description="Blog about ArcadiaNET's project",
    route="/blogs/arcadianet_blog"
)

app.add_page(
    Donations,
    title="Donations",
    description="Donations links",
    route="/donations/links"
)
