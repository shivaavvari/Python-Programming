from PyQt6.QtWidgets  import QCheckBox,QRadioButton,QTabWidget,QHBoxLayout,QGroupBox, QPushButton,QWidget,QMainWindow,QApplication, QStyleFactory, QLabel,QVBoxLayout
import sys

 
class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):  
        
        self.setGeometry(100,100,700,500)
    # creating the tab widget
        tab_widget = QTabWidget()
        tea_tab= QWidget()
        coffee_tab =QWidget()

        tab_widget.addTab(tea_tab,"Tea")
        tab_widget.addTab(coffee_tab,"Coffee")

        


        # create the layout Tea
        tea_layout = QVBoxLayout()

        # create a label 

        liquid_label = QLabel("Select Milk /Water")
        spice_label = QLabel("Select Spices to add ")

        milk_button = QRadioButton("Milk ")
        water_button = QRadioButton("Water ")
        #sugar_button = QCheckBox("Sugar")
        #clove_button = QCheckBox("Clove ")
        #bpepper_button = QCheckBox("Black Pepper")
        #cinammon_button = QCheckBox("Cinnamon ")
        #turmeric_button = QCheckBox("Turmeric ")


        # create a container for milk/water
        liquid_group  = QGroupBox()
        spice_group = QGroupBox()
        # create a layout for liquid

        liquid_group_layout = QVBoxLayout()
        spice_group_layout = QVBoxLayout()    
        liquid_group_layout.addWidget(milk_button)
        liquid_group_layout.addWidget(water_button)
        
        spices = ['sugar','clove','blackpeppwe','cinnamon','turmeric']
        
        for spice in spices:
            spice_check_box = QCheckBox(spice)
            spice_group_layout.addWidget(spice_check_box)
        #spice_group_layout.addWidget(sugar_button)
        #spice_group_layout.addWidget(clove_button)
        #spice_group_layout.addWidget(bpepper_button)
        #spice_group_layout.addWidget(cinammon_button)
        #spice_group_layout.addWidget(turmeric_button)
        
            
        liquid_group.setLayout(liquid_group_layout)
        spice_group.setLayout(spice_group_layout)
        
        tea_layout.addWidget(liquid_label)
        tea_layout.addWidget(liquid_group)
        tea_layout.addWidget(spice_label)
        tea_layout.addWidget(spice_group)
        tea_tab.setLayout(tea_layout)
        
        mainlayout = QVBoxLayout(self)
        mainlayout.addWidget(tab_widget)


        




app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())
