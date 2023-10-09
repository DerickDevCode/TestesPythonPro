import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github.
    :param usuario: str com o nome do usuário no Github.
    :return: str com o link do avatar do usuário.
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    if 'avatar_url' not in resp.json():
        return 'Usuário não encontrado.'
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('Derick23begindev'))
