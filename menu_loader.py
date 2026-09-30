import json

def load_menu():
    with open("menu.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    menu_text = ""

    for item in data["menu"]:
        menu_text += (
            f"- **{item['name']}**: "
            f"{item['description']} - AED {item['price']}\n"
        )

    return menu_text