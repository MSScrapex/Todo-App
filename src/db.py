import json
import os
from datetime import datetime, timedelta

DATA_FILE = "data.json"

class Database:
    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def _read_data(self):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def _write_data(self, data):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_week_todos(self, offset_weeks=0):
        """Retrieves the days and to-dos for the specified week."""
        today = datetime.now() + timedelta(weeks=offset_weeks)
        start_of_week = today - timedelta(days=today.weekday())  # Monday
        
        week_days = []
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        for i in range(7):
            day_date = start_of_week + timedelta(days=i)
            week_days.append({
                "date_str": day_date.strftime("%Y-%m-%d"),
                "day_name": day_names[i],
                "display_date": day_date.strftime("%d.%m.%Y")
            })

        todos = self._read_data()
        
        # Group weekly todos by day.
        result = {}
        
        for day in week_days:
            date_key = day["date_str"]
            result[date_key] = {
                "info": day,
                "todos": [t for t in todos if t.get("date") == date_key]
            }

        start_format = week_days[0]["display_date"]
        end_format = week_days[-1]["display_date"]

        return {
            "week_range": f"{start_format} - {end_format}",
            "days": result
        }

    def add_todo(self, title, date_str):
        todos = self._read_data()
        new_todo = {
            "id": len(todos) + 1 if not todos else max(t["id"] for t in todos) + 1,
            "title": title,
            "date": date_str,
            "completed": False
        }
        
        todos.append(new_todo)
        self._write_data(todos)
        return True

    def delete_todo(self, todo_id):
        todos = self._read_data()
        todos = [t for t in todos if t["id"] != todo_id]
        self._write_data(todos)
        return True

    def toggle_todo(self, todo_id):
        todos = self._read_data()
        for t in todos:
            if t["id"] == todo_id:
                t["completed"] = not t["completed"]
                break
        self._write_data(todos)
        return True