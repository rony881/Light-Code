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
    QsciLexerSQL,
    QsciLexerCPP,
    QsciLexerCSharp,
    QsciLexerJava,
    QsciLexerLua,
    QsciLexerRuby,
    QsciLexerPerl,
    QsciLexerBash,
    QsciLexerBatch,
    QsciLexerProperties,
    QsciLexerMakefile,
    QsciLexerCMake,
    QsciLexerDiff,
    QsciLexerTeX,
)


LEXER_CLASS = {
    "Python": QsciLexerPython,
    "JavaScript": QsciLexerJavaScript,
    "TypeScript": QsciLexerJavaScript,
    "HTML": QsciLexerHTML,
    "CSS": QsciLexerCSS,
    "JSON": QsciLexerJSON,
    "XML": QsciLexerXML,
    "YAML": QsciLexerYAML,
    "Markdown": QsciLexerMarkdown,
    "SQL": QsciLexerSQL,
    "C/C++": QsciLexerCPP,
    "C#": QsciLexerCSharp,
    "Java": QsciLexerJava,
    "Lua": QsciLexerLua,
    "Ruby": QsciLexerRuby,
    "Perl": QsciLexerPerl,
    "Shell": QsciLexerBash,
    "Batch": QsciLexerBatch,
    "TOML": QsciLexerProperties,
    "Makefile": QsciLexerMakefile,
    "CMake": QsciLexerCMake,
    "Diff": QsciLexerDiff,
    "TeX": QsciLexerTeX,
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
    ".sql": "SQL",
    ".c": "C/C++", ".h": "C/C++", ".cpp": "C/C++", ".cc": "C/C++",
    ".hpp": "C/C++", ".cxx": "C/C++",
    ".cs": "C#",
    ".java": "Java",
    ".lua": "Lua",
    ".rb": "Ruby",
    ".pl": "Perl",
    ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell",
    ".bat": "Batch", ".cmd": "Batch",
    ".toml": "TOML",
    ".mk": "Makefile",
    ".cmake": "CMake",
    ".diff": "Diff", ".patch": "Diff",
    ".tex": "TeX",
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
