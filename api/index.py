from flask import Flask, render_template, request
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} ราคา {self.price} บาท"

class ThaiFood(Food):
    def category(self):
        return "อาหารไทย"

class WesternFood(Food):
    def category(self):
        return "อาหารตะวันตก"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        selected_food = request.form.get("food")

        food_data = {
            "ข้าวผัด": 50,
            "ก๋วยเตี๋ยว": 45,
            "ส้มตำ": 40,
            "แฮมเบอร์เกอร์": 99
        }

        price = food_data.get(selected_food, 0)

        if selected_food in ["ข้าวผัด", "ก๋วยเตี๋ยว", "ส้มตำ"]:
            food = ThaiFood(selected_food, price)
        else:
            food = WesternFood(selected_food, price)

        result = f"{food.show()} ({food.category()})"

    return render_template("index.html", result=result)

app = app