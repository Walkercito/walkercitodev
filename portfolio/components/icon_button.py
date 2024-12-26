import reflex as rx

from portfolio.styles.styles import button_solid_style, button_surface_style, button_base_style


def icon_button1(icon: str, url: str, text = "", solid = False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface"
        ),
        href = url,
        is_external = True
    )


def icon_button(icon: str, url: str, text: str = "", solid: bool = False) -> rx.Component:
    """Create an icon button component.
    
    Args:
        icon: The icon name from react-icons
        url: The URL to navigate to
        text: Optional text to display next to the icon
        solid: Whether to use the solid style variant
    
    Returns:
        rx.Component: The icon button component
    """
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    icon,
                    width = "1em",
                    height = "1em",
                ),
                rx.text(text) if text else None,
                spacing = "2",
            ),
            style = button_solid_style if solid else button_surface_style,
        ),
        href = url,
        is_external = True,
    )