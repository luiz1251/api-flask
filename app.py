from flask import Flask, request
import user_service as service

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_all():
    return service.get_all(), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    response, code = service.get_user(id)

    return response, code

@app.route('/users', methods=['POST'])
def create_user():
    dto = request.get_json()
    response, code = service.create_user(dto)
    return response, code

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    dto = request.get_json()
    response, code = service.update_user(id, dto)
    return response, code

if __name__ == '__main__':
    app.run()