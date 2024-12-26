from flask import Blueprint, request, jsonify
from app.services.inference_service import InferenceService

model_routes = Blueprint('model_routes', __name__)

@model_routes.route('/predict', methods=['POST'])
def predict():
    try:
        # 从请求中获取数据
        data = request.get_json()
        model_name = data.get('model_name')
        inputs = data.get('inputs')

        # 调用推理服务
        result = {"model_name": model_name, "prediction": result}
        return jsonify(result), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
