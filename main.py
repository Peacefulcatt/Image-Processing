import sys
from PySide6 import QtCore, QtGui, QtWidgets
from processing import ImageProcessor

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_processor = ImageProcessor()

        self.setStyleSheet("background-color: cyan; color : black ;")
        
        self.file_list_widget = QtWidgets.QListWidget()
        self.file_list_widget.itemSelectionChanged.connect(self.on_file_selected)

        self.image_label = QtWidgets.QLabel("Choose an image from the list on the left")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        self.coordinates_label = QtWidgets.QLabel()
        self.coordinates_label.setAlignment(QtCore.Qt.AlignCenter)

        self.image_viewer_layout = QtWidgets.QVBoxLayout()
        self.image_viewer_layout.addWidget(self.image_label)
        self.image_viewer_layout.addWidget(self.coordinates_label)

        self.proceed_button = QtWidgets.QPushButton("Proceed")
        self.proceed_button.clicked.connect(self.on_proceed_clicked)
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.file_list_layout = QtWidgets.QVBoxLayout()
        self.file_list_layout.addWidget(QtWidgets.QLabel("Image Folder"))
        self.file_list_layout.addWidget(self.create_folder_input())
        self.file_list_layout.addWidget(self.create_folder_browse_button())
        self.file_list_layout.addWidget(self.file_list_widget)

        self.main_layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.main_layout.addLayout(self.file_list_layout)
        self.main_layout.addLayout(self.image_viewer_layout)
        self.main_layout.addWidget(self.proceed_button)

        self.resize(1920,1080)

    def create_folder_input(self):
        self.folder_input = QtWidgets.QLineEdit()
        self.folder_input.textChanged.connect(self.on_folder_input_changed)
        return self.folder_input

    def create_folder_browse_button(self):
        self.folder_browse_button = QtWidgets.QPushButton("Browse")
        self.folder_browse_button.clicked.connect(self.on_folder_browse_clicked)
        return self.folder_browse_button

    def update_file_list(self, folder):
        self.file_list_widget.clear()
        if folder and self.image_processor.is_folder_valid(folder):
            fnames = self.image_processor.get_valid_image_files(folder)
            self.file_list_widget.addItems(fnames)

    def on_folder_input_changed(self, folder):
        self.update_file_list(folder)

    def on_folder_browse_clicked(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_input.setText(folder)
            self.update_file_list(folder)

    def on_file_selected(self):
        selected_items = self.file_list_widget.selectedItems()
        if selected_items:
            filename = self.image_processor.get_absolute_file_path(self.folder_input.text(), selected_items[0].text())
            self.display_image(filename)

    def display_image(self, filename):
        pixmap = QtGui.QPixmap(filename)
        self.image_label.setPixmap(pixmap.scaledToWidth(800))

    def on_proceed_clicked(self):
        selected_items = self.file_list_widget.selectedItems()
        if selected_items:
            filename = self.image_processor.get_absolute_file_path(self.folder_input.text(), selected_items[0].text())
            self.image_processor.process_image(filename)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
