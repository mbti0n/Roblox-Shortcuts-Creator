from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from robloxGameInfo import robloxFind
from PIL import Image
import os, subprocess, win32com.client

# PyQt5 app, window, and layout definitions
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# Window elements
# App name header
appNameHeader = QLabel("Roblox Shortcut")
appNameHeader.setStyleSheet("QLabel { font-size: 21pt; font-weight: 500 }")

# Input prompt (3 lines)
inputPrompt = QLabel("Type the Roblox game URL")
inputPrompt.setAlignment(Qt.AlignTop)
inputPrompt.setWordWrap(True)
inputPrompt2 = QLabel("Must follow this format:\nhttps://www.roblox.com/games/0000000000/Game-Name")
inputPrompt2.setWordWrap(True)

# Text input
textInput = QLineEdit()
textInput.setAlignment(Qt.AlignTop)

# "Add" button
addButton = QPushButton("Add")

# Status prompt
statusPrompt = QLabel()
statusPrompt.setStyleSheet("QLabel { font-weight: 500 }")
statusPrompt.setWordWrap(True)
statusPrompt.hide()

# Game name info (game icon + game name)
gameNameLayout = QHBoxLayout()
pixLabel = QLabel()
pixLabel.hide()
nameLabel = QLabel()
nameLabel.setWordWrap(True)
nameLabel.hide()
gameNameLayout.addWidget(pixLabel)
gameNameLayout.addWidget(nameLabel)
addButton = QPushButton("Add")

# Define on-click function
def clicked():
    try:
        # Required definitions (game info, desktop path, icon path, and shortcut path)
        uriScheme, thumbnail, name, placeId = robloxFind(textInput.text())
        desktopPath = os.path.join(os.environ["USERPROFILE"], "Desktop")
        iconStoragePath = os.path.join(os.environ["USERPROFILE"], ".robloxicons")
        shortcutPath = os.path.join(desktopPath, f"{name}.lnk")
        
        # Make the .robloxicons directory if not exists
        if not os.path.exists(iconStoragePath):
            os.makedirs(iconStoragePath)
            
        # Download the game icon using curl
        subprocess.run(f"curl --output {iconStoragePath}/{placeId}.png {thumbnail}", shell=True)
        
        # Convert to .ico
        img = Image.open(f"{iconStoragePath}/{placeId}.png")
        img.save(f"{iconStoragePath}/{placeId}.ico", format="ICO", sizes=[(256, 256)])
        
        # Create a new desktop shortcut
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(shortcutPath)
        shortcut.TargetPath = uriScheme
        shortcut.WorkingDirectory = os.path.dirname(uriScheme)
        shortcut.IconLocation = os.path.abspath(f"{iconStoragePath}/{placeId}.ico")
        shortcut.save()
        
        # Adjust the window size
        window.adjustSize()
        window.setMinimumHeight(window.sizeHint().height())
        
        # Successful status
        statusPrompt.show()
        statusPrompt.setText("Added to Desktop!")
        
        # Show game info
        nameLabel.show()
        nameLabel.setText(name)
        pixLabel.show()
        pixLabel.setPixmap(QPixmap(f"{iconStoragePath}/{placeId}.png").scaled(100, 100))
        
        # Remove the original .png icon file
        os.remove(f"{iconStoragePath}/{placeId}.png")
        
    # If no game data is found
    except ValueError:
        # Clear the game info label if possible
        nameLabel.clear()
        nameLabel.hide()
        pixLabel.clear()
        pixLabel.hide()
        
        # Adjust the window size
        window.adjustSize()
        window.setMinimumHeight(window.sizeHint().height())
        
        # Unsuccessful status
        statusPrompt.show()
        statusPrompt.setText("Could not get the Roblox game.")
        
    # Adjust the window (again)
    window.adjustSize()
    window.setMinimumHeight(window.sizeHint().height())

# Button on-click / Text input Enter behavior
addButton.clicked.connect(clicked)
textInput.returnPressed.connect(clicked)

# Adding elements to the main window
layout.addWidget(appNameHeader)
layout.addWidget(inputPrompt)
layout.addWidget(inputPrompt2)
layout.addSpacing(3)
layout.addWidget(textInput)
layout.addSpacing(15)
layout.addWidget(addButton)
layout.addWidget(statusPrompt)
layout.addLayout(gameNameLayout)
layout.addStretch()

# Window behaviors
window.setFixedWidth(400)
window.setWindowTitle("Roblox Shortcut Creator")
window.setLayout(layout)

# Display the window
window.show()

# Execute the app
app.exec()