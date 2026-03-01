from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

class Menu:
    def __init__(self, name):
        self.name = name

    def detail(self):
        return f"เมนู: {self.name}"

class Drink(Menu):
    def detail(self):
        return f"เครื่องดื่ม: {self.name} 🧋"

class Dessert(Menu):
    def detail(self):
        return f"ของหวาน: {self.name} 🍰"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        choice = request.form.get("menu")

        if choice == "drink":
            item = Drink("ชาไทย")
        else:
            item = Dessert("เค้กช็อกโกแลต")

        result = item.detail()

    return render_template("index.html", result=result)