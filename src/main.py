import webview
from db import Database

class Api:
    def __init__(self):
        self.db = Database()

    def get_week_todos(self, offset_weeks):
        return self.db.get_week_todos(offset_weeks)

    def add_todo(self, title, date_str):
        return self.db.add_todo(title, date_str)

    def delete_todo(self, todo_id):
        return self.db.delete_todo(todo_id)

    def toggle_todo(self, todo_id):
        return self.db.toggle_todo(todo_id)

    def exit_app(self):
        """Closes the application safely."""
        window.destroy()

if __name__ == '__main__':
    api = Api()
    window = webview.create_window(
        'Weekly To-Do App', 
        'index.html', 
        js_api=api,
        width=1100, 
        height=750,
        resizable=True
    )
    webview.start()