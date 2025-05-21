from PyQt6.QtWidgets  import QColorDialog,QMainWindow, QWidget, QApplication,QSlider, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QAction,QColor
from PyQt6.QtCore import Qt

import sys

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):  
        
 
        self.setGeometry(0,0,700,500)
        self.red_slider = QSlider(Qt.Orientation.Horizontal)
        self.green_slider = QSlider(Qt.Orientation.Horizontal)
        self.blue_slider = QSlider(Qt.Orientation.Horizontal)

        for slider in [self.red_slider,self.green_slider,self.blue_slider]:
             slider.setRange(0,255)
             slider.setValue(255)
             slider.setTickPosition(QSlider.TickPosition.TicksBelow)
             slider.setTickInterval(25)


        self.red_label = QLabel("Red: ")

        self.green_label = QLabel("Green: ")

        self.blue_label = QLabel("Blue: ")

        self.red_value_label = QLabel("255")
        
        self.green_value_label = QLabel("255") 
        
        self.blue_value_label = QLabel("255")
        
        
        

        #creating a layout for main window
        layout = QVBoxLayout(self)
        
        sliders_layout = QVBoxLayout() 
        for label, slider, value_label in zip([self.red_label,self.green_label,self.blue_label],
                 [self.red_slider,self.green_slider,self.blue_slider],
                 [self.red_value_label,self.green_value_label,self.blue_value_label]
                       ):
                slider_layout = QHBoxLayout()
                slider_layout.addWidget(label)
                slider_layout.addWidget(slider)
                slider_layout.addWidget(value_label)
                sliders_layout.addLayout(slider_layout)
        
        
        layout.addLayout(sliders_layout)
        # creating a label to preview colors
        self.color_preview = QLabel()
        color_layout = QVBoxLayout()
        color_layout.addWidget(self.color_preview)
        color_layout.addStretch()
        layout.addLayout(color_layout)

        # connecting sliders to the methods
        self.red_slider.valueChanged.connect(self.update_color)
        self.green_slider.valueChanged.connect(self.update_color)
        self.blue_slider.valueChanged.connect(self.update_color)
        
        #Setting the initial value of Color
        self.color="#ffffff"
        self.color_preview.setStyleSheet(f"background-color:{self.color}")
        
        
        
        self.final_color_label= QLabel("Final Color: #ffffff")
        final_color_layout = QHBoxLayout()
        final_color_layout.addWidget(self.final_color_label)
        layout.addLayout(final_color_layout)
        
    def update_color(self):
        red = self.red_slider.value()
        self.red_value_label.setText(str(red))
        green = self.green_slider.value()
        self.green_value_label.setText(str(green))
        blue = self.blue_slider.value()
        self.blue_value_label.setText(str(blue))
        self.color = QColor(red,green,blue)
        self.color_preview.setStyleSheet(f"background-color:{self.color.name()}")
        self.final_color_label.setText(str(self.color.name()))
                 
    def show_color_dialog(self,event):
        print("Method triggered")
        if event.button() == Qt.MouseButton.LeftButton:
            color_dialog =QColorDialog(self.color,self)
            color_dialog.colorSelected.connect(self.set_color)
            color_dialog.exec()
    def set_color(self,color):
        self.color = color
        self.red_slider.value(color.red)
        self.green_slider.value(color.green)
        self.blue_slider.value(color.blue)
        self.update_color()


app = QApplication(sys.argv)

window = Window()
window.show()
app.exec()