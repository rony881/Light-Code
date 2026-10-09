# src/light_code/editor/syntax_highlighter.py

from pathlib import Path

from PyQt6.Qsci import (
    QsciLexer,
    QsciLexerPython,
    QsciLexerJavaScript,
    QsciLexerHTML,
    QsciLexerCSS,
    QsciLexerJSON,
    QsciLexerXML,
    QsciLexerYAML,
    QsciLexerMarkdown,
    QsciLexerCPP,
    QsciLexerCSharp,
    QsciLexerJava,
    QsciLexerLua,
    QsciLexerRuby,
    QsciLexerBash,
    QsciLexerBatch,
    QsciLexerProperties,
    QsciLexerMakefile,
    QsciLexerCMake,
    QsciScintilla,
)
from PyQt6.QtGui import QColor

from light_code.config import EDITOR_FONT


SYNTAX_COLORS = {
    "text": "#E0E0E0",
    "keyword": "#4FC1FF",
    "number": "#B5CEA8",
    "string": "#FC9867",
    "function": "#ffb454",
    "class": "#FFC66D",
    "operator": "#ff8f40",
    "decorator": "#C586C0",
    "comment": "#5a6673",
}



class PythonLexer(QsciLexerPython):
    def __init__(self, parent: QsciScintilla):
        super().__init__(parent)

        self.PYTHON_COLOR_CONFIG = [
            (SYNTAX_COLORS["text"], QsciLexerPython.Default),
            (SYNTAX_COLORS["keyword"], QsciLexerPython.Keyword),
            (SYNTAX_COLORS["number"], QsciLexerPython.Number),
            (SYNTAX_COLORS["function"], QsciLexerPython.FunctionMethodName),
            (SYNTAX_COLORS["class"], QsciLexerPython.ClassName),
            (SYNTAX_COLORS["operator"], QsciLexerPython.Operator),
            (SYNTAX_COLORS["text"], QsciLexerPython.Identifier),
            (SYNTAX_COLORS["decorator"], QsciLexerPython.Decorator),
            (SYNTAX_COLORS["comment"], QsciLexerPython.Comment),
            (SYNTAX_COLORS["comment"], QsciLexerPython.CommentBlock),
            (SYNTAX_COLORS["string"], QsciLexerPython.SingleQuotedString),
            (SYNTAX_COLORS["string"], QsciLexerPython.SingleQuotedFString),
            (SYNTAX_COLORS["string"], QsciLexerPython.DoubleQuotedString),
            (SYNTAX_COLORS["string"], QsciLexerPython.DoubleQuotedFString),
            (SYNTAX_COLORS["string"], QsciLexerPython.TripleSingleQuotedFString),
            (SYNTAX_COLORS["string"], QsciLexerPython.TripleDoubleQuotedString),
        ]
        self.setDefaultFont(EDITOR_FONT)
        self.setup_lexer()

    def setup_lexer(self):
        for color, syntax in self.PYTHON_COLOR_CONFIG:
            self.setColor(QColor(color), syntax)

LEXER_CLASS = {
    "Python": PythonLexer,
    "JavaScript": QsciLexerJavaScript,
    "TypeScript": QsciLexerJavaScript,
    "HTML": QsciLexerHTML,
    "CSS": QsciLexerCSS,
    "JSON": QsciLexerJSON,
    "XML": QsciLexerXML,
    "YAML": QsciLexerYAML,
    "Markdown": QsciLexerMarkdown,
    "C/C++": QsciLexerCPP,
    "C#": QsciLexerCSharp,
    "Java": QsciLexerJava,
    "Lua": QsciLexerLua,
    "Ruby": QsciLexerRuby,
    "Shell": QsciLexerBash,
    "Batch": QsciLexerBatch,
    "TOML": QsciLexerProperties,
    "Makefile": QsciLexerMakefile,
    "CMake": QsciLexerCMake,
}

EXTENSIONS = {
    ".py": "Python", ".pyw": "Python", ".pyi": "Python",
    ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript", ".jsx": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript",
    ".html": "HTML", ".htm": "HTML",
    ".css": "CSS", ".qss": "CSS",  # your theme file style.qss gets CSS colours
    ".json": "JSON",
    ".xml": "XML", ".svg": "XML", ".ui": "XML", ".qrc": "XML",
    ".yaml": "YAML", ".yml": "YAML",
    ".md": "Markdown", ".markdown": "Markdown",
    ".c": "C/C++", ".h": "C/C++", ".cpp": "C/C++", ".cc": "C/C++",
    ".hpp": "C/C++", ".cxx": "C/C++",
    ".cs": "C#",
    ".java": "Java",
    ".lua": "Lua",
    ".rb": "Ruby",
    ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell",
    ".bat": "Batch", ".cmd": "Batch",
    ".toml": "TOML",
    ".mk": "Makefile",
    ".cmake": "CMake",
}

def detect_language(file_path: str | None) -> str:
    """Return the language name for a path, or PLAIN_TEXT."""
    if not file_path:
        return "Plain Text"
    path = Path(file_path)
    extension = path.suffix.lower()
    return EXTENSIONS.get(extension, "Plain Text")
    
def get_lexer(language: str, parent=None) -> QsciLexer | None:
    """Return a lexer instance for a given language, or None if not found."""
    lexer_class = LEXER_CLASS.get(language)
    if lexer_class is None:
        return None
    return lexer_class(parent)
