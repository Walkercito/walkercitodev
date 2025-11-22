import reflex as rx


class ContactState(rx.State):
    """State para el modal de contacto."""
    is_open: bool = False

    def open_modal(self):
        self.is_open = True

    def close_modal(self):
        self.is_open = False

    def toggle_modal(self):
        self.is_open = not self.is_open
