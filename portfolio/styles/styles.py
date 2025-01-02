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

kofi_button_style = {
    **button_base_style,
    "background": "#ff5f5f",  
    "color": "#ffffff", 
    "border": "1px solid #ff5f5f", 
    "box-shadow": "0 4px 8px rgba(255, 95, 95, 0.6)",  
    "transition": "transform 0.2s, box-shadow 0.2s", 
    "_hover": {
        "background": "#ff8989",  
        "color": "#ffffff", 
        "box-shadow": "0 6px 12px rgba(255, 95, 95, 0.8)", 
        "transform": "scale(1.05)",  
    },
    "_active": {
        "background": "#ff4b4b",  
        "box-shadow": "0 2px 4px rgba(255, 95, 95, 0.4)",  
        "transform": "scale(0.95)", 
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

tech_badge_style = {
    "display": "flex",
    "align_items": "center",
    "gap": "0.5rem",
    "padding": "0.5rem 1rem",
    "border_radius": "0.375rem",
    "transition": "all 0.2s",
    "cursor": "pointer",
    "background": "rgba(255, 255, 255, 0.05)",
    "border": f"1px solid {Color.BORDER.value}",
    "color": TextColor.PRIMARY.value,
    "_hover": {
        "transform": "scale(1.02)",
        "background": "rgba(255, 255, 255, 0.1)",
    }
}

icon_badge_style = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "background": "rgba(255, 255, 255, 0.05)",
    "border": f"1px solid {Color.BORDER.value}",
    "color": TextColor.PRIMARY.value,
    "transition": "all 0.2s",
    "_hover": {
        "transform": "scale(1.02)",
        "background": "rgba(255, 255, 255, 0.1)",
    }
}

card_style = {
    "background": "rgba(255, 255, 255, 0.05)",
    "border": f"1px solid {Color.BORDER.value}",
    "transition": "all 0.2s",
    "_hover": {
        "transform": "scale(1.02)",
        "background": "rgba(255, 255, 255, 0.08)",
    }
}

# Estilo para el enlace que elimina todas las decoraciones por defecto
link_style = {
    "text_decoration": "none",
    "_hover": {
        "text_decoration": "none",
    },
    "color": "inherit",  # Hereda el color del padre
}

text_content_style = {
    "padding": EmSize.DEFAULT.value,
}

# Estilo para los badges de tecnología
tech_badge_style = {
    "background": "rgba(255, 255, 255, 0.05)",
    "border": f"1px solid {Color.BORDER.value}",
    "color": TextColor.PRIMARY.value,
    "transition": "all 0.2s",
    "_hover": {
        "transform": "scale(1.02)",
        "background": "rgba(255, 255, 255, 0.1)",
    }
}

# Estilo para el texto de descripción
description_style = {
    "color": TextColor.SECONDARY.value,
    "font_size": EmSize.DEFAULT.value,
}


STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}