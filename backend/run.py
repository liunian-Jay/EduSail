from app import create_app

app = create_app()


from flask_cors import CORS

# 启用 CORS 支持，允许来自特定 origin（如 http://localhost:8080）的请求
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8080"}})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=15000)