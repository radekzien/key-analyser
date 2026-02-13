from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QFileDialog, QProgressBar, QHBoxLayout
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from AnalyseKey import AnalyseKey

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
        layout.setAlignment(Qt.AlignVCenter)
        centralWidget.setLayout(layout)
    
    #--- LAYOUT COMPONENTS --- 

        #--- Key Label ---
        self.keyLabel = QLabel("Upload a File.")
        keyFont = self.keyLabel.font()
        keyFont.setPointSize(30)
        self.keyLabel.setFont(keyFont)
        self.keyLabel.setAlignment(Qt.AlignCenter)

        #--- File Dialogue ---
        self.fileDial = FileDialogue()

        #--- Alt Keys Title Label ---
        altKeysTitleLabel = QLabel("Closely Related Keys:")
        akTFont = altKeysTitleLabel.font()
        akTFont.setPointSize(15)
        altKeysTitleLabel.setFont(akTFont)

        #--- Alternative keys ---
        alternativeKeys = QWidget()
        altKeysLayout = QVBoxLayout()
        self.subdomLabel = QLabel("Subdominant: ")
        self.domLabel = QLabel("Dominant: ")
        self.relativeLabel = QLabel("Relative: ")
        self.subdom = QLabel("IV")
        self.dom = QLabel("V")
        self.relative = QLabel("III/vi")

        subdomLayout = QHBoxLayout()
        subdomLayout.addWidget(self.subdomLabel)
        subdomLayout.addWidget(self.subdom)

        domLayout = QHBoxLayout()
        domLayout.addWidget(self.domLabel)
        domLayout.addWidget(self.dom)

        relativeLayout = QHBoxLayout()
        relativeLayout.addWidget(self.relativeLabel)
        relativeLayout.addWidget(self.relative)

        altKeysLayout.addLayout(subdomLayout)
        altKeysLayout.addLayout(domLayout)
        altKeysLayout.addLayout(relativeLayout)

        altKeysLayout.setAlignment(Qt.AlignCenter)
        altKeysLayout.setSpacing(20)
        alternativeKeys.setLayout(altKeysLayout)
        
        #--- Analyse Button ---
        keyButton = QPushButton("Analyse Key")
        keyButton.setFixedSize(100,50)
        keyButton.clicked.connect(self.onButtonClick)

        #--- Progress Bar ---
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.hide()
        self.progress.setAlignment(Qt.AlignCenter)

        #--- Find Out More---
        #Button
        self.FindOutMoreButton = QPushButton()
        self.FindOutMoreButton.setFixedSize(50,50)
        self.FindOutMoreButton.setStyleSheet("border : 0; background: transparent;")
        self.FindOutMoreButton.setIcon(QIcon('question-mark.png'))
        self.FindOutMoreButton.setIconSize(self.FindOutMoreButton.size())

    #--- ADDING COMPONENTS TO LAYOUT ---
        layout.addWidget(self.FindOutMoreButton, alignment=Qt.AlignRight)
        layout.addWidget(self.fileDial)
        layout.addWidget(keyButton, alignment=Qt.AlignCenter)
        layout.addWidget(self.keyLabel)
        layout.addWidget(self.progress)
        layout.addWidget(altKeysTitleLabel)
        layout.addWidget(alternativeKeys)
    
    def onButtonClick(self):
        if not self.fileDial.fileSelected:
           self.keyLabel.setText("Upload a File.")
        else:
            self.keyLabel.setText("Analysing...")
            self.subdom.setText("IV")
            self.dom.setText("V")
            self.relative.setText("III/vi")
            self.progress.show()
            self.worker = AnalyseWorker(self.fileDial.fileName)
            self.worker.finished.connect(self.onAnalysisFinished)
            self.worker.start()

    def onAnalysisFinished(self, key_data):
        self.keyLabel.setText(key_data[0])
        self.subdom.setText(key_data[1])
        self.dom.setText(key_data[2])
        self.relative.setText(key_data[3])
        
        self.progress.hide()

#--- Dialogue Window ---
class FileDialogue(QWidget):
    def __init__(self):
        super().__init__()
        self.fileName = ""
        self.fileSelected = False

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
            self.fileName = selected_files[0]
            self.fileSelected = True

#--- Worker Thread ---
class AnalyseWorker(QThread):
    finished = pyqtSignal(list)

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        key_data = AnalyseKey(self.file_name)
        self.finished.emit(key_data)

#--- App ---
app = QApplication([])
window = mainWindow()
window.show()

app.exec()