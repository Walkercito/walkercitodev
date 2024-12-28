import reflex as rx

from portfolio.data import Info
from portfolio.components.icon_badge import icon_badge
from portfolio.components.icon_button import icon_button
from portfolio.styles.styles import IMAGE_HEIGHT, EmSize, Size
from portfolio.styles.color import TextColor, Color

from portfolio.styles.styles import description_style, tech_badge_style



def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(
                    info.title,
                    color = TextColor.PRIMARY.value,
                ),
                rx.text(
                    info.subtitle,
                    color = TextColor.SECONDARY.value,
                ),
                rx.text(
                    info.description,
                    style = description_style,
                ),
                rx.cond(
                    info.technologies,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.hstack(
                                    rx.box(
                                        class_name = tech.icon,
                                        font_size = "1.2em",
                                        align_self = "center",
                                    ),
                                    rx.text(
                                        tech.name,
                                        align_self = "center",
                                    ),
                                    spacing = "2",
                                ),
                                style = tech_badge_style,
                            )
                            for tech in info.technologies
                        ],
                        wrap = "wrap",
                        gap = Size.SMALL.value,
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github
                        )
                    ),
                    spacing = Size.SMALL.value,
                ),
                spacing = Size.SMALL.value,
                width = "100%"
            ),
            spacing = Size.DEFAULT.value,
            width = "100%"
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src = info.image,
                height = IMAGE_HEIGHT,
                width = "auto",
                border_radius = EmSize.DEFAULT.value,
                object_fit = "cover",
                style = {
                    "border": f"1px solid {Color.BORDER.value}",
                }
            )
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(
                    info.date,
                    style = tech_badge_style,
                )
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid = True
                )
            ),
            spacing = Size.SMALL.value,
            align = "end"
        ),
        flex_direction = ["column-reverse", "row"],
        spacing = Size.DEFAULT.value,
        width = "100%"
    )