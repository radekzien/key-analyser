from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QFileDialog, QProgressBar, QHBoxLayout, QTextEdit, QStackedWidget
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
import markdown
from Pipeline.AnalyseKey import AnalyseKey

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    #--- Window ---
        self.setWindowTitle("Key Analyser")
        self.setFixedSize(QSize(750,600))

    #--- Central Widget ---
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

    #-- Main Page --
        mainPage = QWidget()
        layout = QVBoxLayout(mainPage)
        layout.setAlignment(Qt.AlignVCenter)

        self.stack.addWidget(mainPage)
    #--- LAYOUT COMPONENTS --- 

        #--- Key Label ---
        keyLabelWidget = QWidget()
        keyLabelLayout = QVBoxLayout()
        keyLabelLayout.setAlignment(Qt.AlignCenter)
        self.keyLabel = QLabel("Upload a File.")
        keyFont = self.keyLabel.font()
        keyFont.setPointSize(30)
        self.keyLabel.setFont(keyFont)
        self.keyLabel.setAlignment(Qt.AlignCenter)
        self.keyLabel.setStyleSheet("""
            QLabel {
                border: 3px solid black;
                padding: 20px
            }
        """)
        keyLabelLayout.addWidget(self.keyLabel)
        keyLabelLayout.addStretch()
        keyLabelWidget.setLayout(keyLabelLayout)

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
        self.FindOutMoreButton.setFixedSize(30,30)
        self.FindOutMoreButton.setStyleSheet("border : 0; background: transparent;")
        self.FindOutMoreButton.setIcon(QIcon('gui/question-mark.png'))
        self.FindOutMoreButton.setIconSize(self.FindOutMoreButton.size())
        self.FindOutMoreButton.setCursor(Qt.PointingHandCursor)

        self.FindOutMoreButton.clicked.connect(self.OnFOMClicked)

        self.FindOutMore = QWidget()
        fomLayout = QVBoxLayout(self.FindOutMore)

        FOMText = QTextEdit(readOnly=True)
        with open("gui/help.md") as f:
            html = markdown.markdown(f.read())
        FOMText.setHtml(html)

        backBtn = QPushButton("Back")
        backBtn.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        fomLayout.addWidget(backBtn, alignment=Qt.AlignLeft)
        fomLayout.addWidget(FOMText)

        self.stack.addWidget(self.FindOutMore)

    #--- ADDING COMPONENTS TO LAYOUT ---
        layout.addWidget(self.FindOutMoreButton, alignment=Qt.AlignRight)
        layout.addWidget(self.fileDial)
        layout.addWidget(keyButton, alignment=Qt.AlignCenter)
        layout.addWidget(keyLabelWidget)
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

    def OnFOMClicked(self):
        self.stack.setCurrentIndex(1)

#--- Dialogue Window ---
class FileDialogue(QWidget):
    def __init__(self):
        super().__init__()
        self.fileName = ""
        self.fileSelected = False

        layout = QVBoxLayout(self)

        instructionLabel = QLabel("Upload your file (.wav .mp3)")
        instructionFont = instructionLabel.font()
        instructionFont.setBold(True)
        instructionLabel.setFont(instructionFont)
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

        layout.addWidget(instructionLabel)
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