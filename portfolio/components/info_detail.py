import reflex as rx

from portfolio.data import Info
from portfolio.components.icon_badge import icon_badge
from portfolio.components.icon_button import icon_button
from portfolio.styles.styles import (
    IMAGE_HEIGHT, EmSize, Size,
    description_style, tech_badge_style, date_badge_style,
    glass_card_style, project_card_style, card_image_style
)
from portfolio.styles.color import TextColor, Color


def tech_mini_badge(icon: str, name: str) -> rx.Component:
    """Badge pequeño para tecnologías en cards."""
    return rx.box(
        rx.hstack(
            rx.box(
                class_name=icon,
                font_size="0.9rem",
            ),
            rx.text(
                name,
                font_size="0.75rem",
                font_weight="500",
            ),
            spacing="1",
            align="center",
        ),
        padding="0.375rem 0.75rem",
        border_radius="9999px",
        background="rgba(139, 92, 246, 0.1)",
        border=f"1px solid {Color.BORDER_ACCENT.value}",
        color=TextColor.ACCENT.value,
    )


def info_detail(info: Info) -> rx.Component:
    """Card de información con diseño responsive."""
    return rx.box(
        rx.vstack(
            # Header con icono, título y fecha
            rx.flex(
                rx.hstack(
                    # Icon badge
                    icon_badge(info.icon),
                    # Título y subtítulo
                    rx.vstack(
                        rx.text(
                            info.title,
                            font_weight="600",
                            font_size="1.125rem",
                            color="var(--text-primary)",
                        ),
                        rx.text(
                            info.subtitle,
                            font_size="0.9rem",
                            color=TextColor.ACCENT.value,
                        ),
                        spacing="1",
                        align="start",
                    ),
                    spacing="3",
                    align="center",
                ),
                # Fecha badge - estilo como icon_badge
                rx.cond(
                    info.date != "",
                    rx.box(
                        rx.hstack(
                            rx.icon("calendar", size=16, color=Color.ACCENT_SECONDARY.value),
                            rx.text(
                                info.date,
                                font_size="0.8rem",
                                font_weight="600",
                                color="var(--text-secondary)",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        padding="0.5rem 0.875rem",
                        border_radius="10px",
                        background="var(--icon-badge-bg)",
                        border="1px solid var(--border-light)",
                        flex_shrink="0",
                    ),
                ),
                justify="between",
                align="center",
                width="100%",
                flex_wrap="wrap",
                gap="3",
            ),

            # Descripción
            rx.text(
                info.description,
                style={
                    **description_style,
                    "font_size": "0.9rem",
                    "line_height": "1.7",
                },
            ),

            # Imagen (si existe) - ahora responsive
            rx.cond(
                info.image != "",
                rx.box(
                    rx.image(
                        src=info.image,
                        width="100%",
                        max_height="200px",
                        object_fit="cover",
                        border_radius="12px",
                        style={
                            "border": f"1px solid {Color.BORDER.value}",
                        },
                    ),
                    width="100%",
                ),
            ),

            # Tecnologías
            rx.cond(
                len(info.technologies) > 0,
                rx.flex(
                    *[tech_mini_badge(tech.icon, tech.name) for tech in info.technologies],
                    wrap="wrap",
                    gap="2",
                    width="100%",
                ),
            ),

            # Botones de acción
            rx.hstack(
                rx.cond(
                    info.url != "",
                    icon_button("external-link", info.url, "View"),
                ),
                rx.cond(
                    info.github != "",
                    icon_button("github", info.github, "Code"),
                ),
                rx.cond(
                    info.certificate != "",
                    icon_button("award", info.certificate, "Certificate", solid=True),
                ),
                spacing="2",
                flex_wrap="wrap",
            ),

            spacing="4",
            width="100%",
            align="start",
        ),
        style=glass_card_style,
        width="100%",
    )
