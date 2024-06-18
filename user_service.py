import user_repository as repository
from flask import jsonify

def get_all():
    return repository.get_all()

def get_user(id):
    user = repository.get_by_id(id)
    if user == None:
        return jsonify(
            {
                "status": 404,
                "message": "Usuário não encontrado"
            }
        ), 404
    return user, 200

def create_user(dto):
    valid, log = _validate_args(dto)

    if not valid:
        return jsonify(
            {
                "status": 400,
                "message": log
            }
        ), 400
    user = repository.save(dto)
    return user, 201

def _validate_args(dto):
    logs = []
    if not isinstance(dto['nome'], str) or len(dto['nome']) > 500:
        logs.append("O parâmetro 'nome' deve ser do tipo string e ter o tamanho menor que 500.")
    if not isinstance(dto['idade'], int):
        logs.append("O parâmetro 'idade' deve ser do tipo inteiro.")
    if not isinstance(dto['profissao'], str) or len(dto['profissao']) > 255:
        logs.append("O parâmetro 'profissao' deve ser do tipo string e ter o tamanho menor que 255.")
    if not isinstance(dto['estado_civil'], str):
        logs.append("O parâmetro 'estado_civil' deve ser do tipo string.")

    return not logs, logs

def update_user(id, dto):
    valid, log = _validate_args(dto)

    if not valid:
        return jsonify(
            {
                "status": 400,
                "message": log
            }
        ), 400
    user = repository.get_by_id(id)
    if user == None:
        return jsonify(
            {
                "status": 404,
                "message": "Usuário não encontrado"
            }
        ), 404

    repository.update(user, dto)

    return user, 200

