_arr = [
    {
        'id': 1,
        'nome': 'Luiz Fernando',
        'idade': 27,
        'profissao': "programador",
        'estado_civil': 'solteiro'
    },
    {
        'id': 2,
        'nome': 'Caio',
        'idade': 21,
        'profissao': "programador",
        'estado_civil': 'solteiro'
    },
    {
        'id': 3,
        'nome': 'Alessandro',
        'idade': 39,
        'profissao': "programador",
        'estado_civil': 'solteiro'
    }
]

def _new_id():
    return _arr[-1]['id'] + 1
    

def get_all():
    return _arr

def get_by_id(id):
    for user in _arr:
        if user['id'] == id:
            return user
    return None

def save(dto):
    dto['id'] = _new_id()
    _arr.append(dto)
    return _arr[-1]

def update(user, dto):
    user['idade'] = dto['idade']
    user['nome'] = dto['nome']
    user['profissao'] = dto['profissao']
    user['estado_civil'] = dto['estado_civil']

def update_user(dto):
    dto['nome']