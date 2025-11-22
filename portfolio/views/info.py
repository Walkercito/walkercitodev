import reflex as rx

from portfolio.data import Info
from portfolio.styles.styles import Size
from portfolio.components.heading import section_heading
from portfolio.components.info_detail import info_detail


def info(title: str, items: list[Info], icon: str = "folder", section_id: str = "") -> rx.Component:
    """Sección genérica para mostrar Experience, Projects, Studies, etc."""
    return rx.vstack(
        section_heading(title, icon),
        rx.vstack(
            *[info_detail(item) for item in items],
            spacing="4",
            width="100%",
        ),
        spacing="4",
        width="100%",
        align="stretch",
        id=section_id if section_id else title.lower().replace(" ", "-"),
    )
