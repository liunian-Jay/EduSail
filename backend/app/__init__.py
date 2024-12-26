from flask import Flask
from .config import Config
from .api import api_blueprints

def create_app():
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object(Config)
    
    # 注册API蓝图
    for blueprint in api_blueprints:
        app.register_blueprint(blueprint)
    
    return app
