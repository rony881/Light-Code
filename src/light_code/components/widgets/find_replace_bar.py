from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QCheckBox,
    QPushButton
)


class FindReplaceBar(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("findBar")
        self.setFixedHeight(46)
        self.setVisible(False)

        self._editor = None

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 6, 12, 6)
        layout.setSpacing(6)

        lbl = QLabel("🔍")
        lbl.setStyleSheet("font-size: 16px;")
        layout.addWidget(lbl)

        self.find_input = QLineEdit()
        self.find_input.setPlaceholderText("Find...")
        self.find_input.setMinimumWidth(200)
        layout.addWidget(self.find_input)

        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Replace...")
        self.replace_input.setMinimumWidth(200)
        layout.addWidget(self.replace_input)

        self.case_check = QCheckBox("Aa")
        self.case_check.setToolTip("Match Case")
        self.case_check.setStyleSheet("color: #8b949e; font-size: 12px;")
        layout.addWidget(self.case_check)

        self.btn_prev = QPushButton("<-")
        self.btn_prev.setToolTip("Previous Match")
        self.btn_prev.setFixedWidth(32)
        layout.addWidget(self.btn_prev)

        self.btn_next = QPushButton("->")
        self.btn_next.setToolTip("Next Match")
        self.btn_next.setFixedWidth(32)
        layout.addWidget(self.btn_next)

        self.btn_replace = QPushButton("Replace")
        layout.addWidget(self.btn_replace)

        self.btn_replace_all = QPushButton("Replace All")
        layout.addWidget(self.btn_replace_all)

        self.btn_close = QPushButton("✕")
        self.btn_close.setFixedWidth(32)
        self.btn_close.clicked.connect(self.hide)
        layout.addWidget(self.btn_close)

        self.match_label = QLabel("")
        self.match_label.setStyleSheet("color: #fff; font-size: 11px; min-width: 70px;")
        layout.addWidget(self.match_label)

        self.btn_next.clicked.connect(self.find_next)
        self.btn_prev.clicked.connect(self.find_prev)
        self.btn_replace.clicked.connect(self.replace_one)
        self.btn_replace_all.clicked.connect(self.replace_all)
        self.find_input.returnPressed.connect(self.find_next)
        self.replace_input.returnPressed.connect(self.replace_one)

    def set_editor(self, editor):
        self._editor = editor

    def toggle(self, replace_mode=False):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.find_input.setFocus()
            self.find_input.selectAll()
        self.replace_input.setVisible(replace_mode)
        self.btn_replace.setVisible(replace_mode)
        self.btn_replace_all.setVisible(replace_mode)

    def find_next(self):
        if not self._editor:
            return
        text = self.find_input.text()
        if not text:
            return
        cs = self.case_check.isChecked()
        found = self._editor.findFirst(text, False, cs, False, True)
        self.match_label.setText("Found" if found else "No match")
        return found

    def find_prev(self):
        if not self._editor:
            return
        text = self.find_input.text()
        if not text:
            return
        cs = self.case_check.isChecked()
        line, col = self._editor.getCursorPosition()
        found = self._editor.findFirst(text, False, cs, False, True, False, line, col - 1)
        self.match_label.setText("Found" if found else "No match")
        return found

    def replace_one(self):
        if not self._editor:
            return
        if self._editor.hasSelectedText():
            self._editor.replace(self.replace_input.text())
        self.find_next()

    def replace_all(self):
        if not self._editor:
            return
        text = self.find_input.text()
        repl = self.replace_input.text()
        if not text:
            return
        count = 0
        cs = self.case_check.isChecked()
        self._editor.beginUndoAction()
        if self._editor.findFirst(text, False, cs, False, True, True, 0, 0):
            self._editor.replace(repl)
            count += 1
            while self._editor.findNext():
                self._editor.replace(repl)
                count += 1
        self._editor.endUndoAction()
        self.match_label.setText(f"{count} replaced")
        return count