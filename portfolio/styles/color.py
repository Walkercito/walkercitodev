from enum import Enum


class Color(Enum):
    # Fondos
    BACKGROUND = "#0a0a0f"  # Casi negro con tinte azulado
    BACKGROUND_SECONDARY = "#12121a"  # Para cards y secciones
    BACKGROUND_GLASS = "rgba(18, 18, 26, 0.7)"  # Glassmorphism

    # Bordes
    BORDER = "rgba(255, 255, 255, 0.08)"
    BORDER_LIGHT = "rgba(255, 255, 255, 0.15)"
    BORDER_ACCENT = "rgba(139, 92, 246, 0.3)"  # Borde con acento

    # Acentos - Gradiente púrpura/azul/cyan
    ACCENT_PRIMARY = "#8b5cf6"  # Violeta vibrante
    ACCENT_SECONDARY = "#06b6d4"  # Cyan
    ACCENT_TERTIARY = "#3b82f6"  # Azul
    ACCENT_PINK = "#ec4899"  # Rosa para hover

    # Gradientes (como strings para usar en CSS)
    GRADIENT_PRIMARY = "linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%)"
    GRADIENT_SECONDARY = "linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)"
    GRADIENT_GLOW = "linear-gradient(135deg, rgba(139, 92, 246, 0.4) 0%, rgba(6, 182, 212, 0.4) 100%)"

    # Estados
    SUCCESS = "#10b981"  # Verde esmeralda
    WARNING = "#f59e0b"  # Ámbar
    ERROR = "#ef4444"  # Rojo


class TextColor(Enum):
    PRIMARY = "#ffffff"  # Blanco puro
    SECONDARY = "#a1a1aa"  # Gris zinc
    TERTIARY = "#71717a"  # Gris más oscuro
    ACCENT = "#c4b5fd"  # Violeta claro para links
    MUTED = "#52525b"  # Texto muy tenue


# Colores específicos para botones
class ButtonColor(Enum):
    KOFI = "#ff5f5f"
    KOFI_HOVER = "#ff8989"
    GITHUB = "#333333"
    LINKEDIN = "#0077b5"
    TWITTER = "#1da1f2"
