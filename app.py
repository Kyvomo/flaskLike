import flask
from flask import Flask

app = Flask(__name__)


@app.route('/likes')
def get_likes():
    list_names = ["Андрей", "Жанна", "Катя", "Настя", "Алекс", "Миша"]
    if any(char.isdigit() or not char.isalpha() for char in list_names) or len(list_names) > 10:
        return {
            "error": True,
            "data": None,
            "error_message": "Ошибки в имени пользователя"
        }

    return {
        "error": False,
        "data": f"{list_names[0]}, {list_names[1]} и ещё {len(list_names[1:])} человека лайкнули это",
        "error_message": None
    }


if __name__ == '__main__':
    app.run()
