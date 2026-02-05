from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtCore import QSize, Qt

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    #--- Window ---
        self.setWindowTitle("Key Analyser")
        self.setFixedSize(QSize(750,550))

    #--- Central Widget ---
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
    #--- Layout ---
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
    
    #--- LAYOUT COMPONENTS --- 

        #--- Key Label ---
        keyLabel = QLabel("C major")
        keyFont = keyLabel.font()
        keyFont.setPointSize(30)
        keyLabel.setFont(keyFont)
        keyLabel.setAlignment(Qt.AlignCenter)

        #--- File Dialogue ---
        fileDial = FileDialogue()

        #--- Alt Keys Title Label ---
        altKeysTitleLabel = QLabel("Closely Related Keys:")
        akTFont = altKeysTitleLabel.font()
        akTFont.setPointSize(15)
        altKeysTitleLabel.setFont(akTFont)

        #--- Alternative keys ---
        alternativeKeys = QWidget()
        altKeysLayout = QVBoxLayout()
        subdom = "F Major"
        dom = "G Major"
        relative_minor = "A Minor"

        altKeys = QLabel(subdom +"  "+ dom +"   "+ relative_minor)

        akFont = altKeys.font()

        akFont.setPointSize(10)

        altKeys.setFont(akFont)

        altKeysLayout.addWidget(altKeys)
        altKeysLayout.setAlignment(Qt.AlignCenter)

        alternativeKeys.setLayout(altKeysLayout)
        
        #--- Analyse Button ---
        keyButton = QPushButton("Analyse Key")
        keyButton.setFixedSize(100,50)

    #--- ADDING COMPONENTS TO LAYOUT ---
        layout.addWidget(fileDial)
        layout.addWidget(keyButton, alignment=Qt.AlignCenter)
        layout.addWidget(keyLabel)
        layout.addWidget(altKeysTitleLabel)
        layout.addWidget(alternativeKeys)



#--- Dialogue Window ---
class FileDialogue(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.fileLabel = QLabel("No File Selected")
        self.fileLabel.setStyleSheet("""
            QLabel {
                border: 1px solid black;
            }
        """)
        self.fileLabel.setFixedHeight(30)
        self.button = QPushButton("Open File")
        self.button.clicked.connect(self.openFileDialog)
        self.button.setFixedSize(100,50)

        layout.addWidget(self.fileLabel)
        layout.addWidget(self.button)


    def openFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        file_dialog.setNameFilter(
             "Audio Files (*.wav *.mp3)"
            )

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.fileLabel.setText(selected_files[0])
#--- App ---
app = QApplication([])
window = mainWindow()
window.show()

app.exec()