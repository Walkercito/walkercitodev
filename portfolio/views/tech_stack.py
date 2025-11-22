import reflex as rx

from portfolio.styles.styles import EmSize, Size, tech_badge_style
from portfolio.styles.color import TextColor, Color
from portfolio.data import Tech
from portfolio.components.heading import section_heading


def tech_badge(tech: Tech) -> rx.Component:
    """Badge individual de tecnología con hover effects."""
    return rx.box(
        rx.hstack(
            rx.box(
                class_name=tech.icon,
                font_size="1.25rem",
            ),
            rx.text(
                tech.name,
                font_size="0.875rem",
                font_weight="500",
            ),
            spacing="2",
            align="center",
        ),
        style=tech_badge_style,
    )


def tech_stack(technologies: list[Tech]) -> rx.Component:
    return rx.vstack(
        section_heading("Tech Stack", "layers"),
        rx.flex(
            *[tech_badge(tech) for tech in technologies],
            wrap="wrap",
            column_gap="1.25rem",
            row_gap="0.875rem",
            justify="center",
            width="100%",
            padding_y="1rem",
            class_name="tech-stack-grid",
        ),
        spacing="4",
        width="100%",
        align="stretch",
        id="tech",
    )
