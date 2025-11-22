from enum import Enum
import reflex as rx

from portfolio.styles.color import TextColor, Color, ButtonColor


# ============================================================================
# CONSTANTES GLOBALES
# ============================================================================

MAX_WIDTH = "1100px"  # Un poco más ancho para mejor lectura
IMAGE_HEIGHT = "220px"


# ============================================================================
# TAMAÑOS
# ============================================================================

class EmSize(Enum):
    TINY = "0.25em"
    SMALL = "0.5em"
    DEFAULT = "1em"
    HALF = "1.5em"
    MEDIUM = "2em"
    LARGE = "3em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    TINY = "1"
    SMALL = "2"
    DEFAULT = "4"
    MEDIUM = "6"
    LARGE = "8"
    BIG = "9"


# ============================================================================
# ANIMACIONES CSS (para inyectar en stylesheets)
# ============================================================================

CUSTOM_CSS = """
/* ============================================================================
   CSS VARIABLES (Dark mode only)
   ============================================================================ */

:root {
    --bg-primary: #0a0a0f;
    --bg-secondary: #12121a;
    --bg-glass: rgba(18, 18, 26, 0.7);
    --bg-navbar: rgba(10, 10, 15, 0.8);

    --text-primary: #ffffff;
    --text-secondary: #a1a1aa;
    --text-tertiary: #71717a;
    --text-muted: #52525b;

    --border: rgba(255, 255, 255, 0.08);
    --border-light: rgba(255, 255, 255, 0.15);

    --card-bg: rgba(18, 18, 26, 0.7);
    --card-hover-shadow: rgba(139, 92, 246, 0.15);

    --badge-bg: rgba(139, 92, 246, 0.1);
    --icon-badge-bg: rgba(255, 255, 255, 0.05);
}

/* ============================================================================
   ANIMATED GRID BACKGROUND
   ============================================================================ */

.animate-grid {
    animation: grid-move 25s linear infinite;
}

.animate-glow {
    animation: glow-move 20s ease-in-out infinite;
}

@keyframes grid-move {
    0% {
        transform: translate(0, 0);
    }
    100% {
        transform: translate(60px, 60px);
    }
}

@keyframes glow-move {
    0%, 100% {
        transform: translate(0%, 0%) scale(1);
        opacity: 0.6;
    }
    33% {
        transform: translate(15%, 10%) scale(1.1);
        opacity: 0.8;
    }
    66% {
        transform: translate(-10%, 15%) scale(1.05);
        opacity: 0.7;
    }
}

/* ============================================================================
   ANIMATIONS
   ============================================================================ */

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(139, 92, 246, 0.3); }
    50% { box-shadow: 0 0 40px rgba(139, 92, 246, 0.6); }
}

@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes fade-in-up {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

@keyframes pulse-dot {
    0%, 100% {
        transform: scale(1);
        box-shadow: 0 0 8px #10b981, 0 0 16px #10b981;
    }
    50% {
        transform: scale(1.4);
        box-shadow: 0 0 16px #10b981, 0 0 32px #10b981, 0 0 48px #10b981;
    }
}

.animate-pulse-dot {
    animation: pulse-dot 1.5s ease-in-out infinite;
}

@keyframes rotate-gradient {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

@keyframes glow-pulse {
    0%, 100% {
        box-shadow: 0 0 20px rgba(139, 92, 246, 0.4), 0 0 40px rgba(139, 92, 246, 0.2);
    }
    50% {
        box-shadow: 0 0 30px rgba(139, 92, 246, 0.6), 0 0 60px rgba(139, 92, 246, 0.3);
    }
}

.animate-ring {
    animation: glow-pulse 3s ease-in-out infinite;
}

.animate-float {
    animation: float 6s ease-in-out infinite;
}

.animate-pulse-glow {
    animation: pulse-glow 3s ease-in-out infinite;
}

.animate-gradient {
    background-size: 200% 200%;
    animation: gradient-shift 8s ease infinite;
}

.animate-fade-in {
    animation: fade-in-up 0.6s ease-out forwards;
}

.animate-shimmer {
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    background-size: 200% 100%;
    animation: shimmer 2s infinite;
}

/* Ocultar scrollbar pero mantener scroll funcional */
::-webkit-scrollbar {
    display: none;
}

html {
    -ms-overflow-style: none;
    scrollbar-width: none;
}

/* Selection styling */
::selection {
    background: rgba(139, 92, 246, 0.3);
    color: #ffffff;
}

/* Responsive tech stack */
@media (max-width: 768px) {
    .tech-stack-grid {
        gap: 0.75rem !important;
    }
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

/* Glow effects for text */
.text-glow {
    text-shadow: 0 0 20px rgba(139, 92, 246, 0.5);
}

/* Gradient text */
.gradient-text {
    background: linear-gradient(135deg, #8b5cf6, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
"""


# ============================================================================
# ESTILOS GLASSMORPHISM
# ============================================================================

glass_base = {
    "background": "var(--bg-glass)",
    "backdrop_filter": "blur(12px)",
    "-webkit-backdrop-filter": "blur(12px)",
    "border": "1px solid var(--border-light)",
    "border_radius": "16px",
    "transition": "background 0.3s ease, border-color 0.3s ease",
}

glass_card_style = {
    **glass_base,
    "padding": "1.5rem",
    "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
    "_hover": {
        "transform": "translateY(-4px)",
        "border_color": Color.BORDER_ACCENT.value,
        "box_shadow": "0 20px 40px var(--card-hover-shadow)",
    }
}

glass_navbar_style = {
    "background": "var(--bg-navbar)",
    "backdrop_filter": "blur(20px)",
    "-webkit-backdrop-filter": "blur(20px)",
    "border_bottom": "1px solid var(--border)",
    "transition": "background 0.3s ease, border-color 0.3s ease",
}


# ============================================================================
# ESTILOS DE BOTONES
# ============================================================================

button_base_style = {
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "gap": "0.5rem",
    "padding": "0.625rem 1.25rem",
    "border_radius": "12px",
    "font_weight": "500",
    "font_size": "0.875rem",
    "transition": "all 0.2s cubic-bezier(0.4, 0, 0.2, 1)",
    "cursor": "pointer",
    "white_space": "nowrap",
}

button_surface_style = {
    **button_base_style,
    "background": "var(--icon-badge-bg)",
    "border": "1px solid var(--border-light)",
    "color": "var(--text-primary)",
    "_hover": {
        "background": "var(--badge-bg)",
        "border_color": Color.ACCENT_PRIMARY.value,
        "transform": "translateY(-2px)",
        "box_shadow": "0 4px 12px rgba(139, 92, 246, 0.2)",
    },
    "_active": {
        "transform": "translateY(0)",
    }
}

button_solid_style = {
    **button_base_style,
    "background": Color.GRADIENT_PRIMARY.value,
    "border": "none",
    "color": TextColor.PRIMARY.value,
    "_hover": {
        "transform": "translateY(-2px)",
        "box_shadow": "0 8px 20px rgba(139, 92, 246, 0.4)",
        "filter": "brightness(1.1)",
    },
    "_active": {
        "transform": "translateY(0)",
    }
}

button_ghost_style = {
    **button_base_style,
    "background": "transparent",
    "border": "none",
    "color": "var(--text-secondary)",
    "_hover": {
        "color": "var(--text-primary)",
        "background": "var(--icon-badge-bg)",
    }
}

kofi_button_style = {
    **button_base_style,
    "background": f"linear-gradient(135deg, {ButtonColor.KOFI.value}, {ButtonColor.KOFI_HOVER.value})",
    "border": "none",
    "color": "#ffffff",
    "box_shadow": "0 4px 15px rgba(255, 95, 95, 0.4)",
    "_hover": {
        "transform": "translateY(-2px)",
        "box_shadow": "0 8px 25px rgba(255, 95, 95, 0.5)",
        "filter": "brightness(1.1)",
    },
    "_active": {
        "transform": "translateY(0)",
    }
}


# ============================================================================
# ESTILOS DE BADGES Y TAGS
# ============================================================================

tech_badge_style = {
    "display": "inline-flex",
    "align_items": "center",
    "gap": "0.5rem",
    "padding": "0.5rem 1rem",
    "border_radius": "9999px",  # Pill shape
    "background": "rgba(139, 92, 246, 0.1)",
    "border": f"1px solid {Color.BORDER_ACCENT.value}",
    "color": TextColor.ACCENT.value,
    "font_size": "0.875rem",
    "font_weight": "500",
    "transition": "all 0.2s ease",
    "_hover": {
        "background": "rgba(139, 92, 246, 0.2)",
        "transform": "scale(1.05)",
        "box_shadow": "0 0 20px rgba(139, 92, 246, 0.3)",
    }
}

icon_badge_style = {
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "width": "48px",
    "height": "48px",
    "border_radius": "12px",
    "background": "var(--icon-badge-bg)",
    "border": "1px solid var(--border-light)",
    "color": Color.ACCENT_SECONDARY.value,
    "font_size": "1.25rem",
    "flex_shrink": "0",
}

date_badge_style = {
    "display": "inline-flex",
    "align_items": "center",
    "padding": "0.375rem 0.75rem",
    "border_radius": "8px",
    "background": "rgba(6, 182, 212, 0.1)",
    "border": "1px solid rgba(6, 182, 212, 0.3)",
    "color": Color.ACCENT_SECONDARY.value,
    "font_size": "0.75rem",
    "font_weight": "600",
}


# ============================================================================
# ESTILOS DE CARDS
# ============================================================================

card_style = {
    **glass_card_style,
    "overflow": "hidden",
}

project_card_style = {
    "background": "var(--bg-secondary)",
    "border": "1px solid var(--border)",
    "border_radius": "20px",
    "overflow": "hidden",
    "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
    "_hover": {
        "transform": "translateY(-8px)",
        "border_color": Color.BORDER_ACCENT.value,
        "box_shadow": "0 25px 50px var(--card-hover-shadow)",
    }
}

card_image_style = {
    "width": "100%",
    "height": IMAGE_HEIGHT,
    "object_fit": "cover",
    "transition": "transform 0.3s ease",
}


# ============================================================================
# ESTILOS DE LINKS
# ============================================================================

link_style = {
    "text_decoration": "none",
    "color": "inherit",
    "_hover": {
        "text_decoration": "none",
    }
}

nav_link_style = {
    "color": "var(--text-secondary)",
    "font_size": "0.875rem",
    "font_weight": "500",
    "padding": "0.5rem 1rem",
    "border_radius": "8px",
    "transition": "all 0.2s ease",
    "_hover": {
        "color": "var(--text-primary)",
        "background": "var(--icon-badge-bg)",
    }
}


# ============================================================================
# ESTILOS DE TEXTO
# ============================================================================

heading_style = {
    "color": "var(--text-primary)",
    "font_weight": "700",
    "letter_spacing": "-0.02em",
    "line_height": "1.2",
}

subheading_style = {
    "color": "var(--text-secondary)",
    "font_weight": "500",
    "letter_spacing": "-0.01em",
}

description_style = {
    "color": "var(--text-secondary)",
    "font_size": "1rem",
    "line_height": "1.7",
}

text_content_style = {
    "padding": EmSize.DEFAULT.value,
}


# ============================================================================
# ESTILOS DE SECCIONES
# ============================================================================

section_style = {
    "width": "100%",
    "padding_y": "4rem",
}

section_title_style = {
    "display": "inline-flex",
    "align_items": "center",
    "gap": "0.75rem",
    "margin_bottom": "2rem",
}

divider_style = {
    "background": f"linear-gradient(90deg, transparent, {Color.BORDER_LIGHT.value}, transparent)",
    "height": "1px",
    "border": "none",
    "margin_y": "3rem",
}


# ============================================================================
# ESTILOS ESPECIALES
# ============================================================================

avatar_style = {
    "border": f"4px solid {Color.ACCENT_PRIMARY.value}",
    "box_shadow": "0 0 30px rgba(139, 92, 246, 0.4)",
    "transition": "all 0.3s ease",
}

glow_effect = {
    "position": "absolute",
    "width": "300px",
    "height": "300px",
    "border_radius": "50%",
    "background": Color.GRADIENT_GLOW.value,
    "filter": "blur(80px)",
    "opacity": "0.5",
    "pointer_events": "none",
}


# ============================================================================
# STYLESHEETS Y BASE STYLE
# ============================================================================

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
]

BASE_STYLE = {
    "background_color": "var(--bg-primary)",
    "color": "var(--text-primary)",
    "font_family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    "transition": "background-color 0.3s ease, color 0.3s ease",
    rx.button: {
        "--cursor-button": "pointer",
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "text_decoration": "none",
        }
    },
    rx.heading: heading_style,
}
