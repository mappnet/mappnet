import os
import json
from flask import Flask, request, jsonify, send_from_directory

# Настройка Flask: указываем корень для статики и отключаем префикс /static
app = Flask(__name__, static_folder='.', static_url_path='')

# Путь к JSON-файлу с серверами
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(PROJECT_ROOT, 'servers/servers.json')

# Загрузка серверов из файла
def load_servers():
    try:
        if not os.path.exists(DATA_FILE):
            save_servers([])
            return []
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

# Сохранение серверов в файл
def save_servers(data):
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

# Главная страница
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Обработка статики (html, css, js, картинки и т.д.)
@app.route('/<path:folder>/<path:filename>')
def serve_folder(folder, filename):
    return send_from_directory(folder, filename)

# Получение серверов (GET)
@app.route('/get_servers')
def get_servers():
    return jsonify(load_servers())

# Сохранение серверов (POST)
@app.route('/save_servers', methods=['POST'])
def save_servers_api():
    try:
        data = request.get_json()
        if save_servers(data):
            return jsonify({"success": True})
        return jsonify({"success": False, "error": "Ошибка сохранения"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Запуск сервера
if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        save_servers([])
    app.run(debug=True, port=5000, use_reloader=False)
