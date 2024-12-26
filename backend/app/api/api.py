from flask import Blueprint, request, jsonify

test = Blueprint('test', __name__)

@test.route('/test', methods=['POST'])
def test():
    try:
        # 从请求中获取数据
        data = request.get_json()
        test = data.get('test')

        # 调用推理服务
        result = {"res": test, "prediction": '你好'}
        return jsonify(result), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
