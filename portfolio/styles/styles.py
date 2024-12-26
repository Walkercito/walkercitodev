from enum import Enum
import reflex as rx

from portfolio.styles.color import TextColor, Color

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"


class EmSize(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"  # 16px
    HALF = "1.5em"
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px



button_base_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "0.5rem",
    "padding": "0.5rem 1rem",
    "border_radius": "0.375rem",
    "transition": "all 0.2s",
    "cursor": "pointer",
    "_hover": {"transform": "scale(1.02)"},
}

button_surface_style = {
    **button_base_style,
    "background": "transparent",
    "border": f"1px solid {Color.BORDER.value}",
    "color": TextColor.PRIMARY.value,
    "_hover": {
        **button_base_style["_hover"],
        "background": "rgba(255, 255, 255, 0.1)",
    }
}

button_solid_style = {
    **button_base_style,
    "background": TextColor.PRIMARY.value,
    "color": Color.BACKGROUND.value,
    "border": f"1px solid {TextColor.PRIMARY.value}",
    "_hover": {
        **button_base_style["_hover"],
        "background": "rgba(255, 255, 255, 0.9)",
    }
}