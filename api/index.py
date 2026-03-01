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

drink_list = ["ชาไทย", "กาแฟเย็น", "โกโก้"]
dessert_list = ["เค้กช็อกโกแลต", "บราวนี่", "ไอศกรีม"]


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        category = request.form.get("category")
        item_name = request.form.get("item")

        if category == "drink":
            item = Drink(item_name)
        else:
            item = Dessert(item_name)

        result = item.detail()

    return render_template(
        "index.html",
        drinks=drink_list,
        desserts=dessert_list,
        result=result
    )
