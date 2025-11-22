import reflex as rx

from portfolio.data import Extra
from portfolio.components.heading import section_heading
from portfolio.components.card_detail import card_detail
from portfolio.styles.styles import Size
from portfolio.styles.color import Color


# CSS for carousel with dynamic center highlight
CAROUSEL_CSS = """
/* Container */
.blogs-carousel-viewport {
    overflow: hidden;
    position: relative;
}

/* Track that moves */
.blogs-carousel-track {
    display: flex;
    gap: 1.5rem;
    animation: blogs-slide 12s ease-in-out infinite;
}

.blogs-carousel-track:hover {
    animation-play-state: paused;
}

@keyframes blogs-slide {
    0%, 12% {
        transform: translateX(0);
    }
    33%, 45% {
        transform: translateX(calc(-33.333% - 0.5rem));
    }
    66%, 78% {
        transform: translateX(calc(-66.666% - 1rem));
    }
    100% {
        transform: translateX(0);
    }
}

/* Card styling - default dimmed */
.blog-carousel-card {
    flex: 0 0 calc(33.333% - 1rem);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    opacity: 0.5;
    transform: scale(0.92);
    filter: brightness(0.7);
}

/* Center card gets highlight - applied via JS */
.blog-carousel-card.is-center {
    opacity: 1 !important;
    transform: scale(1) !important;
    filter: brightness(1) !important;
    z-index: 10;
}

/* Hover still works */
.blog-carousel-card:hover {
    opacity: 1 !important;
    transform: scale(1.02) !important;
    filter: brightness(1.1) !important;
    z-index: 20 !important;
}

/* Mobile carousel */
@media (max-width: 768px) {
    .blogs-carousel-track {
        animation: blogs-slide-mobile 12s ease-in-out infinite;
    }

    .blog-carousel-card {
        flex: 0 0 280px;
        min-width: 280px;
    }

    @keyframes blogs-slide-mobile {
        0%, 12% {
            transform: translateX(calc(50% - 140px));
        }
        33%, 45% {
            transform: translateX(calc(50% - 140px - 280px - 1.5rem));
        }
        66%, 78% {
            transform: translateX(calc(50% - 140px - 560px - 3rem));
        }
        100% {
            transform: translateX(calc(50% - 140px));
        }
    }
}
"""


def blogs(extras: list[Extra]) -> rx.Component:
    # Triple items for seamless infinite loop
    carousel_items = extras + extras + extras

    return rx.vstack(
        # Inject CSS
        rx.el.style(CAROUSEL_CSS),

        section_heading("Blogs & More", "bookmark"),

        # Same carousel for both mobile and desktop
        rx.box(
            rx.box(
                *[
                    rx.box(
                        card_detail(extra),
                        class_name="blog-carousel-card",
                    )
                    for extra in carousel_items
                ],
                class_name="blogs-carousel-track",
            ),
            class_name="blogs-carousel-viewport",
            width="100%",
            padding_y="0.5rem",
        ),

        spacing="4",
        width="100%",
        align="stretch",
        id="blogs",
    )
