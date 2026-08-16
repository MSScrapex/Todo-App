# 📅 Weekly Todo App (PyWebView & Python)

A clean, modern desktop weekly planner application built with Python and PyWebView. Organize your tasks day-by-day from Monday to Sunday, navigate through weeks, and keep your data saved locally.

---

## 🚀 Features

* **2 Main Screens & Modal Interface:**
  * Welcome / Home Screen
  * Weekly Planner View (Monday – Sunday)
  * Pop-up Modal for adding new tasks
* **Weekly Navigation:** Automatically calculates date ranges and allows navigating forward/backward between weeks.
* **Local Database:** All tasks are saved locally in a `data.json` file managed by `db.py`.
* **Desktop Application:** Powered by `pywebview`, running as a standalone native desktop app without requiring a browser.

---

## 🛠️ Project Structure

```text
todo_app/
├── data.json     # Local database (created automatically)
├── db.py         # JSON database logic & date handling
├── main.py       # PyWebView app launcher & Python-JS bridge
├── index.html    # UI (HTML, CSS, and JS)
└── README.md     # Project documentation
