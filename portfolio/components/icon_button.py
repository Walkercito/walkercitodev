import reflex as rx

from portfolio.styles.styles import (
    button_solid_style,
    button_surface_style,
    button_ghost_style,
    kofi_button_style,
    link_style
)
from portfolio.styles.color import Color, TextColor


def icon_button(
    icon: str,
    url: str,
    text: str = "",
    solid: bool = False,
    is_kofi: bool = False,
    ghost: bool = False,
    size: str = "2"
) -> rx.Component:
    """Botón con icono estilizado."""
    if is_kofi:
        button_style = kofi_button_style
    elif ghost:
        button_style = button_ghost_style
    elif solid:
        button_style = button_solid_style
    else:
        button_style = button_surface_style

    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(icon, size=18),
                rx.text(text) if text else rx.fragment(),
                spacing="2",
                align="center",
            ),
            style=button_style,
            size=size,
        ),
        href=url,
        is_external=True,
        style=link_style,
    )


SOCIAL_COLORS = {
    "github": "#ffffff",
    "linkedin": "#0A66C2",
    "twitter": "#1DA1F2",
    "message-circle": "#5865F2",  # Discord
    "send": "#0088cc",  # Telegram
    "coffee": "#FF5E5B",  # Ko-fi
    "file-text": "#8b5cf6",  # Resume/CV
}


def social_icon(icon: str, url: str, label: str = "") -> rx.Component:
    """Icono de red social con efecto hover del color de la red."""
    hover_color = SOCIAL_COLORS.get(icon, Color.ACCENT_PRIMARY.value)

    return rx.link(
        rx.box(
            rx.icon(icon, size=20, color="var(--text-secondary)"),
            width="44px",
            height="44px",
            display="flex",
            align_items="center",
            justify_content="center",
            border_radius="12px",
            background="var(--icon-badge-bg)",
            border="1px solid var(--border)",
            transition="all 0.2s ease",
            _hover={
                "background": f"rgba({int(hover_color[1:3], 16)}, {int(hover_color[3:5], 16)}, {int(hover_color[5:7], 16)}, 0.15)" if hover_color.startswith("#") else "rgba(139, 92, 246, 0.1)",
                "border_color": hover_color,
                "transform": "translateY(-2px)",
                "box_shadow": f"0 4px 15px {hover_color}40",
                "& svg": {
                    "color": hover_color,
                }
            },
        ),
        href=url,
        is_external=True,
        title=label,
    )
