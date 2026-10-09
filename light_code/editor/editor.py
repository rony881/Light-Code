# src/light_code/editor/editor.py

from PyQt6.Qsci import QsciScintilla
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QFrame

from light_code.config import (
    EDITOR_SELECTION_BACKGROUND,
    EDITOR_SELECTION_FOREGROUND,
    WINDOW_BACKGROUND
)
from light_code.editor.syntax_highlighter import detect_language, get_lexer


class BaseEditor(QsciScintilla):
    def __init__(self, parent=None, file_path=None):
        super().__init__(parent=parent)
        self.setObjectName("base_editor")
        self.file_path = file_path
        self.language = detect_language(file_path)
        self._config()
        self.apply_syntax_highlighter()

    def apply_syntax_highlighter(self):
        lexer = get_lexer(self.language, self)
        if lexer:
            lexer.setDefaultPaper(self.paper())
            lexer.setDefaultColor(self.color())
            lexer.setPaper(self.paper())
            self.setLexer(lexer)

    def _config(self):
        self.setFrameShape(QFrame.Shape.NoFrame)

        self.setCaretWidth(3)
        self.setUtf8(True)
        self.setTabWidth(4)
        self.setMarginWidth(0, "00000000")
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)

        # Auto-completion
        self.setAutoCompletionThreshold(2)
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)

        # Editor Paper And Text Color:
        self.setPaper(QColor(WINDOW_BACKGROUND))  # editor background (matches QMainWindow)

        # Selection Colors
        self.setSelectionBackgroundColor(QColor(EDITOR_SELECTION_BACKGROUND))
        self.setSelectionForegroundColor(QColor(EDITOR_SELECTION_FOREGROUND))

        # Line Number Foreground And Background Color:
        self.setMarginsBackgroundColor(QColor("#0d1117"))
        self.setMarginsForegroundColor(QColor("#3D424D"))

        # Caret Line Back and Foreground:
        self.setCaretLineBackgroundColor(QColor("#131721"))
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
        