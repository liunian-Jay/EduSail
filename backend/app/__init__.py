from flask import Flask
from .config import Config
from .api.api import test as api_test

def create_app():
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object(Config)
    
    # 注册API蓝图
    app.register_blueprint(api_test, url_prefix='/test')
    
    return app
