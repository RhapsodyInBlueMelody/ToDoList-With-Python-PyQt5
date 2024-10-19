import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QHBoxLayout

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDoloo")
        self.setGeometry(100, 100, 400, 300)

        self.tasks = []

        self.layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Remove Task")
        self.task_list = QListWidget()

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.remove_button)

        self.layout.addWidget(self.input_field)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.task_list)

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)

        self.input_field.setStyleSheet("background-color: #3A6D8C; border-radius: 10px; border: 1px solid #ccc; padding: 10px; margin: 20px; color: white;")
        self.add_button.setStyleSheet("background-color: #EAD8B1; border-radius: 10px; border: 1px solid #ccc; padding: 10px;")
        self.remove_button.setStyleSheet("background-color: #EAD8B1;border-radius: 10px; border: 1px solid #ccc; padding: 10px;")
        self.task_list.setStyleSheet("background-color: #3A6D8C; border-radius: 10px; border: 1px solid #ccc; padding: 10px; color: white;")
        self.setStyleSheet("background-color: #001F3F")
        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()
            
    def remove_task(self):
        selected_task = self.task_list.currentRow()
        if selected_task >= 0:
            self.tasks.pop(selected_task)
            self.task_list.takeItem(selected_task)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
