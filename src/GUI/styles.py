import os

def apply_stylesheet(app):

    css_path = os.path.join(os.path.dirname(__file__), 'css', 'style.css')
    
    with open(css_path, "r") as file:
        stylesheet = file.read()
        app.setStyleSheet(stylesheet)