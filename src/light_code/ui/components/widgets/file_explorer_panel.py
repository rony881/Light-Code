# ui/components/widgets/file_explorer.py

from pathlib import Path

from PyQt6.QtCore import QModelIndex, QSize, pyqtSignal
from PyQt6.QtGui import QFileSystemModel, QIcon
from PyQt6.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QPushButton, QTreeView

from light_code.config import FILE_PLUS_ICON, FOLDER_PLUS_ICON
from light_code.ui.base_widgets.base_widget import BaseWidget
from light_code.utils.logger import logger


class FileExplorer(BaseWidget):
    file_selected = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("file_explorer_panel")
        logger.info("Initializing FileExplorer")

        self.header = FileExplorerHeader(self)
        self.add(self.header)

        self.file_tree_view = FileTreeView(self)
        self.file_tree_view.file_selected.connect(self.file_selected)

        self.home_path = str(Path.home())
        self.setFolderPath(self.home_path)
        self.add(self.file_tree_view)

    def browse_folder(self) -> None:
        """Open a native dialog and switch root folder if the user picks one."""

        logger.info("Opening folder dialog")
        current = self.file_tree_view.file_model.rootPath()

        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", current)
        if folder_path:
            self.setFolderPath(folder_path)
            logger.info(f"Folder selected: {folder_path}")
        else:
            logger.warning("Folder selection cancelled")

    def new_file(
        self, file_name: str = "untitled.py", folder_path: str | None = None
    ) -> bool:
        """Create a new file in the specified folder or the current selection."""
        logger.info(f"Creating new file: {file_name}")
        if folder_path is None:
            index = self.file_tree_view.currentIndex()

            if not index.isValid():
                folder_path = self.file_tree_view.file_model.rootPath()
            elif self.file_tree_view.file_model.isDir(index):
                folder_path = self.file_tree_view.file_model.filePath(index)
            else:
                folder_path = self.file_tree_view.file_model.filePath(index.parent())

        file_path = Path(folder_path) / file_name

        if file_path.exists():
            logger.warning(f"File already exists: {file_path}")
            return False

        file_path.touch()
        logger.info(f"File created: {file_path}")
        return True

    def set_folder_lbl_text(self, text: str) -> None:
        self.header.folder_lbl.setText(text)

    def set_new_file_btn_conn(self, conn) -> None:
        self.header.new_file_btn.clicked.connect(conn)

    def setFolderPath(self, folder_path: str) -> None:
        """Point the explorer at a new root folder."""

        logger.info(f"Setting folder path: {folder_path}")
        self.file_tree_view.file_model.setRootPath(folder_path)
        self.file_tree_view.setRootIndex(
            self.file_tree_view.file_model.index(folder_path)
        )
        self.file_tree_view.folder_changed.emit(folder_path)
        self.set_folder_lbl_text(self.get_folder_name(folder_path))

    def get_folder_name(self, folder_path: str) -> str:
        return Path(folder_path).name


class FileExplorerHeader(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing FileExplorerHeader")
        self.setFixedHeight(35)
        self.setObjectName("file_explorer_header")
        self.h_layout = QHBoxLayout()
        self.add(self.h_layout)

        self.folder_lbl = QLabel(parent=self)
        self.h_layout.addWidget(self.folder_lbl)
        self.h_layout.addStretch()

        self.new_file_btn = QPushButton(parent=self)
        self.new_file_btn.setObjectName("new_file_btn")
        self.new_file_btn.setIcon(QIcon(FILE_PLUS_ICON))
        self.new_file_btn.setIconSize(QSize(16, 16))
        self.new_file_btn.setFixedSize(24, 24)
        self.h_layout.addWidget(self.new_file_btn)

        self.new_folder_btn = QPushButton(parent=self)
        self.new_folder_btn.setObjectName("new_folder_btn")
        self.new_folder_btn.setIcon(QIcon(FOLDER_PLUS_ICON))
        self.new_folder_btn.setIconSize(QSize(16, 16))
        self.new_folder_btn.setFixedSize(24, 24)
        self.h_layout.addWidget(self.new_folder_btn)


class FileTreeView(QTreeView):
    file_selected = pyqtSignal(str)
    folder_changed = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing FileTreeView")
        self.setObjectName("file_tree_view")
        self.file_model = QFileSystemModel()
        self.clicked.connect(self.on_file_click)
        self._setup_config()

    def _setup_config(self):
        # tree configuration
        self.setModel(self.file_model)
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
        self.setAnimated(True)
        self.setIndentation(10)
        self.setMinimumWidth(170)
        self.setItemsExpandable(True)
        self.setRootIsDecorated(False)
        self.setHeaderHidden(True)

    def on_file_click(self, index: QModelIndex) -> None:
        path = self.file_model.filePath(index)
        if not self.file_model.isDir(index):
            self.file_selected.emit(path)
