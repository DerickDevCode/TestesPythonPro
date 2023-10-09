from libpythonpro.github_api import buscar_avatar


def test_buscar_avatar():
    url = buscar_avatar('Derick23begindev')
    assert url == 'https://avatars.githubusercontent.com/u/137959472?v=4'


def test_buscar_avatar_invalido():
    url = buscar_avatar('')
    assert url == 'Usuário não encontrado.'
