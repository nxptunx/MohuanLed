from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import subprocess
import sys

class LEDControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LED Control')
        self.setStyleSheet("background-color: grey;")
        layout = QVBoxLayout()

        # Turn ON button
        self.turn_on_button = QPushButton('ON', self)
        self.turn_on_button.setStyleSheet("background-color: black; color: white; border-radius: 15px;")
        self.turn_on_button.setFixedHeight(30)
        self.turn_on_button.setFixedWidth(70)  
        self.turn_on_button.clicked.connect(self.turn_on_led)
        layout.addWidget(self.turn_on_button)

        self.turn_off_button = QPushButton('OFF', self)
        self.turn_off_button.setStyleSheet("background-color: black; color: white; border-radius: 15px;")
        self.turn_off_button.setFixedHeight(30)
        self.turn_off_button.setFixedWidth(70) 
        self.turn_off_button.clicked.connect(self.turn_off_led)
        layout.addWidget(self.turn_off_button)
        
        self.disconnect_button = QPushButton('Disconnect', self)
        self.disconnect_button.setStyleSheet("background-color: black; color: white; border-radius: 15px;")
        self.disconnect_button.setFixedHeight(30)
        self.disconnect_button.setFixedWidth(70)  
        self.disconnect_button.clicked.connect(self.disconnect_led)
        layout.addWidget(self.disconnect_button)


        self.rainbow_button = QPushButton('RGB', self)
        self.rainbow_button.setStyleSheet("background-color: black; color: white; border-radius: 15px;")
        self.rainbow_button.setFixedHeight(30)
        self.rainbow_button.setFixedWidth(70)  
        self.rainbow_button.clicked.connect(self.rainbow_cycle)
        layout.addWidget(self.rainbow_button)

        self.red_button = QPushButton('Red', self)
        self.red_button.setStyleSheet("background-color: red; color: black; border-radius: 15px;")
        self.red_button.setFixedHeight(30)
        self.red_button.setFixedWidth(70)
        self.red_button.clicked.connect(self.red_color)
        layout.addWidget(self.red_button)
    
        self.green_button = QPushButton('Green', self)
        self.green_button.setStyleSheet("background-color: green; color: black; border-radius: 15px;")
        self.green_button.setFixedHeight(30)
        self.green_button.setFixedWidth(70)
        self.green_button.clicked.connect(self.green_color)
        layout.addWidget(self.green_button)
    
        self.blue_button = QPushButton('Blue', self)
        self.blue_button.setStyleSheet("background-color: blue; color: black; border-radius: 15px;")
        self.blue_button.setFixedHeight(30)
        self.blue_button.setFixedWidth(70)
        self.blue_button.clicked.connect(self.blue_color)
        layout.addWidget(self.blue_button)

        self.purple_button = QPushButton('Purple', self)
        self.purple_button.setStyleSheet("background-color: Purple; color: black; border-radius: 15px;")
        self.purple_button.setFixedHeight(30)
        self.purple_button.setFixedWidth(70)
        self.purple_button.clicked.connect(self.purple_color)
        layout.addWidget(self.purple_button) 

        self.white_button = QPushButton('White', self)
        self.white_button.setStyleSheet("background-color: White; color: black; border-radius: 15px;")
        self.white_button.setFixedHeight(30)
        self.white_button.setFixedWidth(70)
        self.white_button.clicked.connect(self.white_color)
        layout.addWidget(self.white_button)

        self.orange_button = QPushButton('Orange', self)
        self.orange_button.setStyleSheet("background-color: Orange; color: black; border-radius: 15px;")
        self.orange_button.setFixedHeight(30)
        self.orange_button.setFixedWidth(70)
        self.orange_button.clicked.connect(self.orange_color)
        layout.addWidget(self.orange_button)
        
        self.yellow_button = QPushButton('Yellow', self)
        self.yellow_button.setStyleSheet("background-color: YelloW; color: black; border-radius: 15px;")
        self.yellow_button.setFixedHeight(30)
        self.yellow_button.setFixedWidth(70)
        self.yellow_button.clicked.connect(self.yellow_color)
        layout.addWidget(self.yellow_button)

        self.setLayout(layout)

    def turn_on_led(self):
        subprocess.run(['python', 'TurnONLed.py'])

    def turn_off_led(self):
        subprocess.run(['python', 'TurnOFFLed.py'])

    def disconnect_led(self):
        subprocess.run(['python', 'Disconnect.py'])

    def rainbow_cycle(self):
        subprocess.run(['python', 'rainbow.py'])
    
    def red_color(self):
        subprocess.run(['python', 'red.py']) 

    def green_color(self):
        subprocess.run(['python', 'green.py'])    

    def blue_color(self):
        subprocess.run(['python', 'blue.py'])    

    def purple_color(self):
        subprocess.run(['python', 'purple.py'])  

    def white_color(self):
        subprocess.run(['python', 'white.py'])

    def orange_color(self):
        subprocess.run(['python', 'orange.py'])

    def yellow_color(self):
        subprocess.run(['python', 'yellow.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LEDControlApp()
    ex.show()
    sys.exit(app.exec_())