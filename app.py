import flask
from flask import Flask

app = Flask(__name__)


@app.route('/likes')
def get_likes():
    list_names = ["Андрей","Жена","Степан", "Dima"]
    dict_answer ={
        "error": False,
        "data": '',
        "error_message": None
    }

    if any(char.isdigit() or not char.isalpha() for char in list_names) or len(list_names) > 10:
        return {
            "error": True,
            "data": None,
            "error_message": "Ошибки в имени пользователя"
        }

    if len(list_names) == 0:
        dict_answer['data'] = 'Это никому не нравится'
    elif len(list_names) == 1:
        dict_answer['data'] = f'{list_names[0]} лайкнул это'
    elif len(list_names) == 2:
        dict_answer['data'] = f'{list_names[0]} и {list_names[1]} лайкнули это'
    elif len(list_names) == 3:
        dict_answer['data'] = f'{", ".join(str(item) for item in list_names[0:2])} и {list_names[2]} лайкнули это'
    else:
        dict_answer['data'] = f'{", ".join(str(item) for item in list_names[0:2])} и еще {len(list_names[2:])} лайкнули это'
    return dict_answer
if __name__ == '__main__':
    app.run()
