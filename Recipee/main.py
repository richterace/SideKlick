import os
import json
import traceback
import sys
import mysql.connector
from mysql.connector import Error

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QSizePolicy, QPushButton, QLabel
from PyQt5.QtCore import QFile, QStringListModel, Qt
from PyQt5 import uic
from Recipee.assets import assets

ui_file_path = os.path.join(os.path.dirname(__file__), "softeng-ui.ui")

class RecipeMain(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize db_connection attribute
        self.db_connection = self.connect_to_mysql()  # Connect to MySQL database

        # Load the rest of the UI and connect buttons
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        uic.loadUi(ui_file, self)  # Load the UI file directly into the QMainWindow
        ui_file.close()

        # Connect the buttons to their respective functions
        #Buttons in page widget
        self.addButton.clicked.connect(self.go_to_add_widget)

        #Buttons in add widget
        self.backButton.clicked.connect(self.go_to_page_widget)
        self.addIngredient.clicked.connect(self.add_ingredient)
        self.deleteIngredient.clicked.connect(self.delete_ingredient)
        self.addPhoto.clicked.connect(self.add_photo)
        self.saveButton.clicked.connect(self.save_recipe)  # Connect the Save button
        self.deleteButton.clicked.connect(self.delete_recipe)

        #Buttons in recipe widget
        self.backButton_2.clicked.connect(self.go_to_page_widget)
        self.editButton.clicked.connect(self.edit_recipe)

        self.current_widget = self.page  # Initially set the current widget to the page widget

        self.recipes = self.load_recipes()  # Load existing recipes

        self.display_recipe_buttons()  # Display recipe buttons in the page widget

        self.selected_recipe = None  # Variable to store the selected recipe

        self.reset_add_widget()  # Reset the "Add" widget when the main window is initialized

        self.logged_in_user_id = None  # Initialize to None
        
    def connect_to_mysql(self):
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                database='health',
                user='root',
                password='123456'
            )
            if conn.is_connected():
                print('Connected to MySQL database')
                return conn
        except Error as e:
            print(e)
            return None

    def load_recipes(self):
        # Load recipes from JSON file
        filename = 'Recipee/recipes.json'
        recipes = []
        try:
            with open(filename, 'r') as file:
                recipes = json.load(file)
            print(f"Loaded {len(recipes)} recipes from {filename}")
        except Exception as e:
            print(f"Error loading recipes: {e}")
            traceback.print_exc()
        
        # Fetch additional recipes from the database and merge with existing recipes
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM recipes")
                db_recipes = cursor.fetchall()
                for recipe in db_recipes:
                    # Split ingredients string into a list
                    if 'ingredients' in recipe and isinstance(recipe['ingredients'], str):
                        recipe['ingredients'] = recipe['ingredients'].split('\n')
                recipes.extend(db_recipes)
                print(f"Loaded {len(db_recipes)} recipes from MySQL database")
            except mysql.connector.Error as e:
                print(f"Error loading recipes from MySQL: {e}")
                traceback.print_exc()
        return recipes

    
    def save_recipe_to_mysql(self, recipe, user_id):
        cursor = self.db_connection.cursor()
        try:
            # Concatenate ingredients into a single string separated by newline characters
            ingredients_string = '\n'.join(recipe['ingredients'])

            cursor.execute("INSERT INTO recipes (user_id, name, ingredients, procedures, photo_path) VALUES (%s, %s, %s, %s, %s)",
                        (user_id, recipe['name'], ingredients_string, recipe['procedure'], recipe['photo_path']))
            self.db_connection.commit()
            print("Recipe saved to MySQL database")
        except Error as e:
            print("Error saving recipe to MySQL database:", e)
            self.db_connection.rollback()




    def get_logged_in_user_id(self):
        # Implement logic to retrieve the user_id of the currently logged-in user
        # This could involve querying the database or accessing user session data
        # For demonstration purposes, let's assume you have a method to retrieve it
        return self.logged_in_user_id

    def add_ingredient(self):
        # Get the text from inputIngredient
        ingredient = self.inputIngredient.toPlainText().strip()  # Remove leading/trailing whitespace

        if ingredient:
            # Split the ingredient text into separate items based on newline characters
            ingredients_list = ingredient.split('\n')
            
            # Add each ingredient as a separate item to the listIngredient QListWidget
            for ing in ingredients_list:
                self.viewIngredients.addItem(ing)

            # Clear the inputIngredient QTextEdit
            self.inputIngredient.clear()

        print("Ingredients added:", ingredients_list)

    def clear_recipe_buttons(self):
        # Get the number of items in the layout
        count = self.gridLayout_5.count()

        # Remove all items from the layout
        for i in range(count):
            item = self.gridLayout_5.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

    def reset_add_widget(self):
        # Clear all input fields in the "Add" widget
        self.inputRecipeName.clear()
        self.listIngredient.clear()
        self.inputProcedure.clear()
        self.photoName.clear()

        self.selected_recipe = None  # Also clear the selected recipe

    def navigate_to_recipe(self, recipe):
        self.go_to_recipe()

        self.selected_recipe = recipe

        self.populate_recipe_details(recipe)

    def edit_recipe(self):
        # Navigate to the add widget
        self.go_to_add_widget()

        if self.selected_recipe:
            # Populate the add widget with the details of the selected recipe for editing
            self.populate_add_widget_with_recipe_details(self.selected_recipe)
        else:
            print("No recipe selected.")

    def populate_recipe_details(self, recipe):
        # Populate the recipe widget with the details of the selected recipe
        recipe_name = recipe.get("name")
        ingredients = recipe.get("ingredients")
        procedure = recipe.get("procedures")
        photo_path = recipe.get("photo_path")

        self.Recipes_2.setText(recipe_name)
        pixmap = QPixmap(photo_path)
        self.photoDisplay.setStyleSheet(f"border-image: url({photo_path}); background-repeat: no-repeat; background-position: center; border-radius: 15px;")

        self.viewIngredients.clear()
        if isinstance(ingredients, list):
            for ingredient in ingredients:
                self.viewIngredients.addItem(ingredient)
        else:
            # If ingredients is a string, split by newline to create list items
            ingredients_list = ingredients.split('\n')
            for ingredient in ingredients_list:
                self.viewIngredients.addItem(ingredient)

        self.viewProcedures.setPlainText(procedure)


    def populate_add_widget_with_recipe_details(self, recipe):
        # Populate the add widget with the details of the selected recipe for editing
        recipe_name = recipe.get("name")
        ingredients = recipe.get("ingredients")
        procedure = recipe.get("procedure")
        photo_path = recipe.get("photo_path")

        self.inputRecipeName.setPlainText(recipe_name)
        self.listIngredient.clear()
        for ingredient in ingredients:
            self.listIngredient.addItem(ingredient)
        self.inputProcedure.setPlainText(procedure)
        self.photoName.setPlainText(photo_path)

    def clear_recipe_buttons(self):
        while self.gridLayout_5.count():
            item = self.gridLayout_5.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def display_recipe_buttons(self):
        self.clear_recipe_buttons()
        num_columns = 2
        row = 0
        col = 0
        for index, recipe in enumerate(self.recipes):
            recipe_name = recipe.get("name")
            image_path = recipe.get("photo_path")  # Assuming the image path is specified in the recipe JSON
            if recipe_name and image_path:
                button = QPushButton()
                button.setObjectName(f"recipeButton_{index}")

                # Set the background image, dimensions, and remove the border
                button.setStyleSheet(
                    f"QPushButton {{ border-image: url({image_path}); border-radius: 15px;}}")
                button.setFixedSize(150, 190)

                button.clicked.connect(lambda _, recipe=recipe: self.navigate_to_recipe(recipe))

                # Add the button to the grid layout
                self.gridLayout_5.addWidget(button, row, col)

                # Add a label for the recipe name below the button
                label = QLabel(recipe_name)
                label.setAlignment(Qt.AlignLeft)  # Align text to the left
                label.setStyleSheet(
                    "QLabel { margin-bottom: 25px; }")
                self.gridLayout_5.addWidget(label, row + 1, col)  # Place the label in the row below the button

                # Increment column counter
                col += 1
                if col == num_columns:
                    col = 0
                    row += 2  # Increment by 2 to leave space for the button and label in the next row


    # def show_recipe_details(self, recipe):
    #     # Implement this method to show the details of the selected recipe
    #     pass

    def go_to_page_widget(self):
        self.selected_recipe = None  # Variable to store the selected recipe
        self.reset_add_widget()

        self.RecipeList.setCurrentWidget(self.page)
        self.current_widget = self.page
        self.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def go_to_add_widget(self):
        self.RecipeList.setCurrentWidget(self.add)
        self.current_widget = self.add

    def go_to_recipe(self):
        self.RecipeList.setCurrentWidget(self.recipe)
        self.current_widget = self.recipe

    def add_ingredient(self):
        # Get the text from inputIngredient
        ingredient = self.inputIngredient.toPlainText()
        if ingredient:
            # Add the ingredient to the listIngredient QListWidget
            self.listIngredient.addItem(ingredient)
            # Clear the inputIngredient QTextEdit
            self.inputIngredient.clear()
        print("Ingredient added: ", ingredient)

    def delete_ingredient(self):
        # Get the currently selected item(s) from listIngredient
        selected_items = self.listIngredient.selectedItems()
        # Iterate over the selected items and remove them from listIngredient
        for item in selected_items:
            self.listIngredient.takeItem(self.listIngredient.row(item))

    def add_photo(self):
        # Open a file dialog to select a photo
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            # Get the selected file(s)
            file_paths = file_dialog.selectedFiles()

            # Display the path of the selected file in the QPlainTextEdit
            if file_paths:
                file_path = file_paths[0]
                self.photoName.setPlainText(file_path)

    def save_recipe(self):
        # Retrieve the user ID of the currently logged-in user
        logged_in_user_id = self.get_logged_in_user_id()

        # Check if a user is logged in
        if logged_in_user_id is None:
            print("No user is logged in. Saving recipe to JSON file.")
            # Save recipe to JSON file
            # Existing code...
        else:
            print("Saving recipe to MySQL database...")
            # Save recipe to MySQL database
            recipe_name = self.inputRecipeName.toPlainText()
            ingredients = [self.listIngredient.item(i).text() for i in range(self.listIngredient.count())]
            procedure = self.inputProcedure.toPlainText()
            photo_path = self.photoName.toPlainText()

            # Define the recipe data
            recipe_data = {
                "name": recipe_name,
                "ingredients": ingredients,
                "procedure": procedure,
                "photo_path": photo_path
            }

            self.save_recipe_to_mysql(recipe_data, logged_in_user_id)

            # Clear the current recipes and re-fetch them to include the newly saved recipe
            self.recipes = self.load_recipes()

            # Clear the recipe buttons
            self.clear_recipe_buttons()

            # Display the updated recipe buttons
            self.display_recipe_buttons()

            # Reset the add widget
            self.reset_add_widget()
            self.selected_recipe = None  # Variable to store the selected recipe

            self.go_to_page_widget()
            
    def save_recipes_to_json(self):
        filename = 'Recipee/recipes.json'
        try:
            with open(filename, 'w') as file:
                json.dump(self.recipes, file, indent=4)
            print(f"Recipes saved to {filename}")
        except Exception as e:
            print(f"Error saving recipes to JSON: {e}")
            traceback.print_exc()

    def delete_recipe(self):
        if self.selected_recipe:
            # Find the index of the selected recipe in the list of recipes
            index = self.recipes.index(self.selected_recipe)

            # Remove the recipe at the index
            del self.recipes[index]

            # Save the updated list of recipes to the JSON file
            filename = 'Recipee/recipes.json'
            try:
                with open(filename, 'w') as file:
                    json.dump(self.recipes, file, indent=4)
                print(f'The recipe has been deleted from {filename}')
            except Exception as e:
                print(f"Error deleting recipe from JSON: {e}")
                traceback.print_exc()

            # Delete the recipe from the database
            if self.db_connection:
                try:
                    cursor = self.db_connection.cursor()
                    cursor.execute("DELETE FROM recipes WHERE id = %s", (self.selected_recipe['id'],))
                    self.db_connection.commit()
                    print("Recipe deleted from MySQL database")
                except mysql.connector.Error as e:
                    print(f"Error deleting recipe from MySQL: {e}")
                    traceback.print_exc()

            # Refresh the recipe buttons in the page widget
            self.display_recipe_buttons()
        else:
            print("No recipe selected.")

        self.clear_recipe_buttons()

        self.display_recipe_buttons()
        self.go_to_page_widget()


    def clear_recipe_buttons(self):
            # Get the number of items in the layout
        count = self.gridLayout_5.count()

            # Remove all items from the layout
        for i in range(count):
            item = self.gridLayout_5.itemAt(i)
            if item.widget():
                item.widget().deleteLater()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = RecipeMain()
    main_window.show()
    sys.exit(app.exec_())
