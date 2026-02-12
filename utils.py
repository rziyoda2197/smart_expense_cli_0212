import json
import os

FILE = "data/expenses.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(data, title, amount, category):
    data.append({
        "title": title,
        "amount": amount,
        "category": category
    })
    save_data(data)
