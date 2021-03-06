import time
from talon import Context, Module, actions, clip, ui

ctx = Context()
mod = Module()


@ctx.action_class("edit")
class edit_actions:
    def selected_text() -> str:
        # try:
        #     text = ui.focused_element().AXSelectedText
        #     if text:
        #         return text
        # except Exception:
        #     pass

        try:
            with clip.capture() as s:
                actions.edit.copy()
            return s.get()
        except clip.NoChange:
            return clip.get()


@mod.action_class
class Actions:
    def paste(text: str):
        """Pastes text and preserves clipboard"""

        with clip.revert():
            clip.set(text)
            actions.edit.paste()
            # sleep here so that clip.revert doesn't revert the clipboard too soon
            actions.sleep("100ms")
