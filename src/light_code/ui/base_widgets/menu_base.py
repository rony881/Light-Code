# src/light_code/ui/components/base_widgets/menu_base.py

from dataclasses import dataclass

from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import QMenu, QMenuBar

# ============================================================================
# Menu Manager | File | Edit | View | Settings | About | Help |
# ============================================================================


@dataclass
class MenuItem:
    """One entry in a menu. Use `None` in a menu's item list for a separator."""

    name: str
    handler: str | None = None
    shortcut: str | None = None


# structure passed to Menumanager.build()
MenuStructure = dict[str, list[MenuItem | None]]


class MenuBaseWidget(QMenuBar):
    """Builds the menu bar from a declarative structure."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._menus: dict[str, QMenu] = {}
        self._actions: dict[str, QAction] = {}

    def build(self, structure: MenuStructure) -> None:
        for menu_name, items in structure.items():
            menu = self.add_menu(menu_name)
            if menu is None:
                return
            for item in items:
                if item is None:
                    menu.addSeparator()
                    continue
                self._add_action(menu_name, menu, item)

    def add_menu(self, name: str) -> QMenu | None:
        menu = self.addMenu(name)
        if menu is not None:
            self._menus[name] = menu
            return menu

    def add_action_to(self, menu_name: str, item: MenuItem) -> QAction:
        """Add one action to an already-created menu, e.g. after build()."""
        menu = self._menus[menu_name]
        return self._add_action(menu_name, menu, item)

    def _add_action(self, menu_name: str, menu: QMenu, item: MenuItem) -> QAction:
        # parent=self keeps the action alive and lets the shortcut fire
        # anywhere in this window, even before the user opens the menu.
        action = QAction(item.name, self)
        if item.shortcut:
            action.setShortcut(QKeySequence(item.shortcut))
        if item.handler:
            action.triggered.connect(item.handler)

        menu.addAction(action)
        self._actions[f"{menu_name}/{item.name}"] = action
        return action

    def action(self, key: str) -> QAction:
        """Look up a previously built action, e.g. action('File/Save')."""
        return self._actions[key]

    def menu(self, name: str) -> QMenu:
        return self._menus[name]
