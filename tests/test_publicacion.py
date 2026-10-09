import pytest

from red_social.publicacion import Publicacion, Retweet, Tweet


@pytest.mark.parametrize(
    "mensaje",
    [
        (""),  # Mensaje vacio
        (" "),  # Espacio sin nada
        ("a" * 281),  # 281 caracteres
    ],
)
def test_texto_invalido_lanza_error(ana, mensaje):
    with pytest.raises(ValueError):
        Tweet(ana, mensaje)


@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("", []),  # Sin hashtags
        ("Hola #Python #PYTEST", ["#python", "#pytest"]),  # Pasa a minuscula
        ("#python y otra vez #python", ["#python"]),  # Sin repetidos
        (
            "Me gusta #python, y mucho #pytest!",
            ["#python", "#pytest"],
        ),  # Quita la puntuacion
    ],
)
def test_extraer_hashtags(texto, esperado):
    assert Publicacion.extraer_hashtags(texto) == esperado


def test_retweet_comparte_el_texto_del_original(tweet, luis):
    retweet = Retweet(luis, tweet)

    assert retweet.original is tweet
    assert retweet.texto == tweet.texto
    assert retweet.hashtags == tweet.hashtags
    assert retweet.autor is luis
