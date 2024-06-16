from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QStackedWidget, QGridLayout, QScrollArea, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QFrame, QLineEdit
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize, QDateTime
from PyQt5 import uic
import sys
from Grocery import images
import os

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the UI file
        uic.loadUi("Grocery\groceryfeature.ui", self)
        self.list_count = 1  # Initialize the list count
        # Defining all the widgets
        
        # Buttons Widgets
        self.addnewlist = self.findChild(QPushButton, "addNewList")
        self.addnewitem = self.findChild(QPushButton, "addNewItem")
        self.backbutton = self.findChild(QPushButton, "grocerybackbutton")
        self.deleteButton = self.findChild(QPushButton, "deleteButton")
        self.deleteItem = self.findChild(QPushButton, "DeleteButton")
        
        # Label Widgets
        self.bgimg = self.findChild(QLabel, "grocerybg")
        self.bgimg2 = self.findChild(QLabel, "grocerybg2")
        self.totalprice = self.findChild(QLabel, "total_price")
        self.labellistname = self.findChild(QPlainTextEdit, "grocery_list_name")
        
        # ScrollPane and its content area
        self.scroll = self.findChild(QScrollArea, "scrollArea")
        self.scroll_2 = self.findChild(QScrollArea, "scrollArea_2")
        self.scrollWidgetContents = self.findChild(QWidget, "scrollAreaWidgetContents")
        self.scrollWidgetContents2 = self.findChild(QWidget, "scrollAreaWidgetContents2")
        
        # Stacked Widgets
        self.stackedWidget = self.findChild(QStackedWidget, "groceryft")
        self.groceryList = self.findChild(QWidget, "grocerylist")
        self.grocerymain = self.findChild(QWidget, "grocerymain")
        self.item_widget = self.findChild(QWidget, "item_widget")
        
        # Configure the scroll area
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Apply a modern and thin style to the vertical scrollbar
        self.scroll_2.setStyleSheet("""
            QScrollArea {
                background: transparent;
            }""")
        self.scroll.setStyleSheet("""
            QScrollArea {
                background: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 8px;
                margin: 10px 0 10px 0;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #a0a0a0;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
        """)

        # Ensure scrollWidgetContents has a layout
        if self.scrollWidgetContents.layout() is None:
            layout = QGridLayout(self.scrollWidgetContents)
            layout.setVerticalSpacing(25)
            layout.setHorizontalSpacing(25)
            self.scrollWidgetContents.setLayout(layout)
        self.scrollWidgetContents.layout().setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Ensure alignment to top-left
        
          # Define a dictionary to store the prices of items
        self.item_prices = {}  
        
        
        # Connect signals and slots
        self.addnewlist.clicked.connect(self.addNewListWidget)
        self.backbutton.clicked.connect(self.backmainpage)
        self.labellistname.textChanged.connect(self.update_selected_widget)
        self.addnewitem.clicked.connect(self.addNewItemWidget)  # Connect addnewitem button
        self.deleteItem.clicked.connect(self.deleteCheckedItems)
        self.deleteButton.clicked.connect(self.deleteCheckedWidgets)

    def deleteCheckedItems(self):
        # Create a message box for confirmation
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this item?', 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            layout = self.item_widget.layout()
            if layout is None:
                return
            
            total_price = 0.0
            for i in reversed(range(layout.count())):
                item_widget = layout.itemAt(i).widget()
                if item_widget is not None:
                    checkbox = item_widget.findChild(QCheckBox)
                    if checkbox is not None and checkbox.isChecked():
                        checkbox.setChecked(False)  # Uncheck the checkbox
                        quantity_product = item_widget.findChild(QLineEdit, "quantity_product")
                        orginal_price = item_widget.findChild(QLineEdit, "orginal_price")
                        item_name_list = item_widget.findChild(QLineEdit, "item_name_list")
                        if quantity_product is not None and orginal_price is not None and item_name_list is not None:
                            quantity = int(quantity_product.text())
                            price_per_unit = float(orginal_price.text())
                            total_price -= quantity * price_per_unit
                            # Remove the item from the dictionary
                            item_name = item_name_list.text()
                            self.item_prices.pop(item_name, None)
                            # Remove item from layout
                        layout.removeWidget(item_widget)
                        item_widget.deleteLater()
            
            
            self.totalprice.setText(f" {total_price:.2f}")
                
    def addNewItemWidget(self):
        
                # Create the popup widget
        popup_widget = QWidget()
        popup_widget.setFixedSize(350, 385)
        popup_widget.setStyleSheet("background-color: #F0F0F0; border-radius: 20px;")
        # Remove the window title
        popup_widget.setWindowTitle(" ")
        
        # Create the layout for the popup widget
        layout = QVBoxLayout(popup_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Create the text fields
        item_name_label = QLabel("Item Name:")
        item_name_label.setStyleSheet("color: #5E5E5E; font-family: Verdana; font-size: 16px;")
        layout.addWidget(item_name_label)

        item_name_text = QLineEdit()
        item_name_text.setStyleSheet("background-color: white; color: #5E5E5E; font-family: Verdana; font-size: 14px; border-radius: 10px; height: 40px")
        layout.addWidget(item_name_text)

        quantity_label = QLabel("Quantity:")
        quantity_label.setStyleSheet("color: #5E5E5E; font-family: Verdana; font-size: 16px;")
        layout.addWidget(quantity_label)

        quantity_text = QLineEdit()
        quantity_text.setStyleSheet("background-color: white; color: #5E5E5E; font-family: Verdana; font-size: 14px; border-radius: 10px; height: 40px")
        layout.addWidget(quantity_text)

        price_label = QLabel("Price:")
        price_label.setStyleSheet("color: #5E5E5E; font-family: Verdana; font-size: 16px;")
        layout.addWidget(price_label)

        price_text = QLineEdit()
        price_text.setStyleSheet("background-color: white; color: #5E5E5E; font-family: Verdana; font-size: 14px;border-radius: 10px; height: 40px")
        layout.addWidget(price_text)

        # Create the "Add Item" button
        add_item_button = QPushButton("Add Item")
        add_item_button.setFixedSize(251, 57)
        add_item_button.setStyleSheet("background-color: #76BA99; color: white; border-radius: 20px; font-family: Verdana; font-size: 16px;")
        layout.addWidget(add_item_button, alignment=Qt.AlignCenter)


        

        def add_item():
            itemname = item_name_text.text()
            quantity = quantity_text.text()
            price = price_text.text()

            item_name_list.setText(itemname)
            quantity_product.setText(quantity)
            orginal_price.setText(price)

            checkbox.stateChanged.connect(lambda state, item_name_list=item_name_list, quantity_product=quantity_product, orginal_price=orginal_price: checkbox_state_changed(state, item_name_list, quantity_product, orginal_price))


            popup_widget.close()

        add_item_button.clicked.connect(add_item)

        # Show the popup widget
        popup_widget.show()



            
        
        if self.item_widget.layout() is None:
            layout = QVBoxLayout(self.item_widget)
            layout.setContentsMargins(10, 2, 10, 2)
            layout.setAlignment(Qt.AlignTop)
            self.item_widget.setLayout(layout)

        # Create the container widget for the new item
        new_item_widget = QWidget()
        new_item_widget.setFixedSize(QSize(368, 53))
        new_item_widget.setStyleSheet("background: rgba(0, 0, 0, 0); border-radius: 15px;")

        # Create a horizontal layout for the new item widget
        new_item_layout = QHBoxLayout(new_item_widget)
        new_item_layout.setContentsMargins(0, 0, 0, 0)
        new_item_layout.setSpacing(0)

        # Create the checkbox widget
        checkbox_widget = QWidget()
        checkbox_widget.setFixedSize(QSize(20, 53))
        checkbox_widget.setStyleSheet("background: rgba(0, 0, 0, 0); border-radius: 15px;")

        # Create the checkbox inside the checkbox widget
        checkbox = QCheckBox(checkbox_widget)
        checkbox.setFixedSize(QSize(20, 20))
        checkbox.move(1, 16)  # Adjust the position of the checkbox if needed

        # Customize the checkbox stylesheet
        checkbox_style = """
        QCheckBox::indicator:checked {
            background-color: #78C112;
            border: none;
            border-radius: 4px;
        }

        QCheckBox::indicator:unchecked {
            background-color: rgba(0, 0, 0, 0);
            border: 1px solid #C0C0C0;
            border-radius: 4px;
        }

        QCheckBox::indicator:checked:disabled {
            background-color: #78C112;
            border: none;
            border-radius: 4px;
        }

        QCheckBox::indicator:unchecked:disabled {
            background-color: rgba(0, 0, 0, 0);
            border: 1px solid #C0C0C0;
            border-radius: 4px;
        }
        """
        checkbox.setStyleSheet(checkbox_style)
        

        # Create the plain text area widget
        item_name_list = QLineEdit()
        item_name_list.setFixedSize(QSize(150, 53))
        item_name_list.setStyleSheet("background: rgba(0, 0, 0, 0); border-radius: 15px;")
        item_name_list.setFont(QFont("Verdana", 16))  # Set font to Verdana, size 16

        # Create the red minus button widget
        red_minus_button = QPushButton("-")
        red_minus_button.setFixedSize(QSize(25, 25))
        red_minus_button.setStyleSheet("color: red; background-color: transparent; border: none; font: bold 36px 'Arial';")
        red_minus_button.clicked.connect(lambda: decrease_number())

        # Create the plain text area widget for 3 digit numbers
        quantity_product = QLineEdit()
        quantity_product.setFixedSize(QSize(40, 53))
        quantity_product.setStyleSheet("background: rgba(0, 0, 0, 0); border-radius: 5px;")
        quantity_product.setFont(QFont("Verdana", 16))  # Set font to Verdana, size 16
        quantity_product.setPlaceholderText("0")  # Set the initial placeholder text to "0"
        quantity_product.setAlignment(Qt.AlignCenter)
   

        # Create the green plus button widget
        green_plus_button = QPushButton("+")
        green_plus_button.setFixedSize(QSize(25, 25))
        green_plus_button.setStyleSheet("color: green; background-color: transparent; border: none; font: bold 36px 'Arial';")
        green_plus_button.clicked.connect(lambda: increase_number())
        
        # Create a vertical layout for the red minus button
        red_minus_layout = QVBoxLayout()
        red_minus_layout.setContentsMargins(0, -10, 0, 0)  # Adjust the top margin to move the button up
        red_minus_layout.addWidget(red_minus_button, alignment=Qt.AlignVCenter)

        # Create a vertical layout for the green plus button
        green_plus_layout = QVBoxLayout()
        green_plus_layout.setContentsMargins(0, -10, 0, 0)  # Adjust the top margin to move the button up
        green_plus_layout.addWidget(green_plus_button, alignment=Qt.AlignVCenter)
                
        def decrease_number():
            current_number = int(quantity_product.text())
            if current_number > 0:
                new_quantity = current_number - 1
                quantity_product.setText(str(new_quantity))
                if checkbox == Qt.Checked:
                    update_item_price(new_quantity)

        def increase_number():
            current_number = int(quantity_product.text())
            new_quantity = current_number + 1
            quantity_product.setText(str(new_quantity))
            if checkbox == Qt.Checked:
                update_item_price(new_quantity)

        def update_item_price(quantity):
            if orginal_price.text().isdigit():
                price_per_unit = float(orginal_price.text())
            else:
                price_per_unit = 0.0  # Default or error handling scenario
            item_name = item_name_list.text()
            self.item_prices[item_name] = {"quantity": quantity, "price_per_unit": price_per_unit}
            update_total_price()

        def checkbox_state_changed(state, item_name_list, quantity_product, orginal_price):
            if state == Qt.Checked:
                quantity = int(quantity_product.text())
                price = float(orginal_price.text())
                total_price = quantity * price
                item_name = item_name_list.text()
                self.item_prices[item_name] = {"quantity": quantity, "price_per_unit": price}
                update_total_price()
            else:
                item_name = item_name_list.text()
                if item_name_list.text() in self.item_prices:
                    del self.item_prices[item_name_list.text()]
                    update_total_price()

            update_total_price()

        def update_total_price():
            total_price = sum(item["quantity"] * item["price_per_unit"] for item in self.item_prices.values())
            self.totalprice.setText(f" {total_price:.2f}")




        
        # Create the last plain text area widget
        orginal_price = QLineEdit()
        orginal_price.setFixedSize(QSize(80, 53))
        orginal_price.setStyleSheet("background: rgba(0, 0, 0, 0); border-radius: 15px;")    
        orginal_price.setFont(QFont("Verdana", 16))  # Set font to Verdana, size 16
        orginal_price.setAlignment(Qt.AlignCenter)



        # Create a container widget
        container_widget = QWidget()
        container_widget.setFixedSize(347, 53)
        container_widget.setStyleSheet("background-color: #F0F0F0; border-radius: 20px;")

        # Create a horizontal layout for the container widget
        container_layout = QHBoxLayout(container_widget)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        # Move the existing widgets to the new container layout
        container_layout.addWidget(item_name_list)
        container_layout.addWidget(red_minus_button)
        container_layout.addWidget(quantity_product)
        container_layout.addWidget(green_plus_button)
        container_layout.addWidget(orginal_price)
        # Add widgets to the new item layout
    
        
        new_item_layout.addWidget(checkbox_widget)
        new_item_layout.addWidget(container_widget)
         

        # Add the new item widget to the item_widget's layout
        self.item_widget.layout().addWidget(new_item_widget)
        self.item_widget.setStyleSheet("background: white;")
        # Add a vertical spacer item at the bottom of the layout
        spacer_item = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.item_widget.layout().addItem(spacer_item)

        # Configure the scroll area for the item_widget
        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.item_widget)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("background: rgba(0, 0, 0, 0);")

        # Update the scroll area for item_widget
        self.scroll_2.setWidget(scroll_area)
        self.scroll_2.setStyleSheet("background: rgba(0, 0, 0, 0);")
        self.scroll_2.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 8px;
                margin: 0px 0px 0px 0px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #a0a0a0;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
        """)
    
    def addNewListWidget(self):
        layout = self.scrollWidgetContents.layout()
        row, col = divmod(layout.count(), 2)

        new_widget = QWidget()
        new_widget.setFixedSize(QSize(162, 136))
        new_widget.setStyleSheet("background-color: #FDFFAB; border-radius: 30px;")
        new_widget.mousePressEvent = self.onWidgetClicked

        grocery_label = QLabel(f"Grocery\nList {self.list_count}", new_widget)
        grocery_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        grocery_label.setGeometry(10, 10, 142, 74)
        grocery_label.setStyleSheet("font-family: Verdana; font-size: 32px; color: black;")

        # Create checkbox
        checkbox = QCheckBox(new_widget)
        checkbox.setGeometry(125, 100, 70, 30)
        checkbox.setStyleSheet("background-color: none;")


        self.labellistname.setPlainText(f"Grocery List {self.list_count}")

        # Create and add label with formatted text for date
        current_date = QDateTime.currentDateTime().toString("MM/dd/yyyy")
        date_label = QLabel(new_widget)
        date_label.setText(current_date)
        date_label.setStyleSheet("font-family: Verdana; font-size: 16px; color: #5E5E5E;")
        date_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        date_label.setGeometry(10, 100, 112, 24)

        self.list_count += 1
        layout.addWidget(new_widget, row, col)

    def confirmDelete(self):
        reply = QMessageBox.question(self, 'Confirm Delete', 'Are you sure you want to delete the checked items?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.deleteCheckedWidgets()

    def deleteCheckedWidgets(self):
        layout = self.scrollWidgetContents.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                checkbox = widget.findChild(QCheckBox)
                if checkbox and checkbox.isChecked():
                    layout.removeWidget(widget)
                    widget.deleteLater()

    def deleteCheckedWidgets(self):
        layout = self.scrollWidgetContents.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                checkbox = widget.findChild(QCheckBox)
                if checkbox and checkbox.isChecked():
                    layout.removeWidget(widget)
                    widget.deleteLater()
                    # Shift the widgets up to fill the gap
                    for j in range(i, layout.count()):
                        item_widget = layout.itemAt(j).widget()
                        if item_widget:
                            new_pos = item_widget.pos()
                            new_pos.setY(new_pos.y() - widget.height())
                            item_widget.move(new_pos)


    def onWidgetClicked(self, event):
        widget = self.sender()
        if widget:
            grocery_label = widget.findChild(QLabel)
            if grocery_label:
                self.labellistname.setText(grocery_label.text())
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QWidget, "grocerylist"))



    def backmainpage(self):
        self.update_selected_widget()
        self.stackedWidget.setCurrentWidget(self.stackedWidget.findChild(QWidget, "grocerymain"))

    def update_selected_widget(self):
        selected_widget = self.scrollWidgetContents.focusWidget()
        if selected_widget:
            grocery_label = selected_widget.findChild(QLabel)
            if grocery_label:
                grocery_label.setText(self.labellistname.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())