# src/light_code/editor/editor.py

from PyQt6.Qsci import QsciScintilla
from PyQt6.QtGui import QColor, QFont


class BaseEditor(QsciScintilla):
    def __init__(self, parent=None, file_path=None):
        super().__init__()
        self.setObjectName("base_editor")
        self.file_path = file_path
        self._config()

    def _config(self):
        self.setCaretWidth(2)  # Cursor Width
        self.setUtf8(True)
        self.setTabWidth(4)
        self.setMarginWidth(0, "00000000")
        self.setFont(QFont("Jetbrains Mono", 15))
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)

        # Auto-completion
        self.setAutoCompletionThreshold(2)
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)

        # Editor Paper And Text Color:
        self.setPaper(QColor("#0d1117"))  # editor background (matches QMainWindow)
        self.setColor(QColor("#c9d1d9"))  # default text color

        # Selection Colors
        self.setSelectionBackgroundColor(QColor("#1f6feb"))  # accent blue
        self.setSelectionForegroundColor(QColor("#f0f6fc"))

        # Line Number Foreground And Background Color:
        self.setMarginsForegroundColor(
            QColor("#7d858e")
        )  # line Number Foreground Color (muted text)
        self.setMarginsBackgroundColor(
            QColor("#0d1117")
        )  # line Number Background Color (panel bg)

        # Caret Line Back and Foreground:
        self.setCaretLineBackgroundColor(QColor("#161b22"))
        self.setCaretForegroundColor(QColor("#58a6ff"))  # accent blue
        self.setCaretLineVisible(True)

        # Indentation Guide
        self.setAutoIndent(True)
        self.setIndentationGuides(True)
        self.setIndentationsUseTabs(False)
        self.setIndentationGuidesBackgroundColor(
            QColor("#21262d")
        )  # Indentation line background Color
        self.setIndentationGuidesForegroundColor(
            QColor("#21262d")
        )  # Indentation line Foregorund Color
