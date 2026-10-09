import pytest

from red_social.publicacion import Tweet
from red_social.red import RedSocial
from red_social.usuario import Usuario


@pytest.fixture
def ana():
    return Usuario("Ana", "@ana")


@pytest.fixture
def luis():
    return Usuario("Luis", "@luis")


@pytest.fixture
def tweet(ana):
    return Tweet(ana, "Hola a todos #python #pytest")


@pytest.fixture
def red():
    red = RedSocial()

    ana = red.registrar("Ana", "@ana")
    luis = red.registrar("Luis", "@luis")
    red.registrar("Marta", "@marta")

    luis.seguir(ana)

    return red
