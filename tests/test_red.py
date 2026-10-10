import json

from red_social.publicacion import Tweet
from red_social.red import RedSocial


def test_timeline_solo_tiene_publicaciones_de_los_seguidos(red):
    ana = red["@ana"]
    luis = red["@luis"]
    marta = red["@marta"]

    tweet_ana_1 = red.publicar(Tweet(ana, "Primer tweet de Ana #python"))
    red.publicar(Tweet(marta, "Tweet de Marta #pytest"))
    tweet_ana_2 = red.publicar(Tweet(ana, "Segundo tweet de Ana #python"))

    timeline_luis = red.timeline(luis)
    assert timeline_luis == [tweet_ana_2, tweet_ana_1]

    timeline_ana = red.timeline(ana)
    assert timeline_ana == []


def test_desde_json_construye_usuarios_y_seguimientos(mocker):
    datos_mock = {
        "usuarios": [
            {"nombre": "Ana", "alias": "@ana"},
            {"nombre": "Luis", "alias": "@luis"},
        ],
        "seguimientos": [["@luis", "@ana"]],
    }
    json_contenido = json.dumps(datos_mock)

    mock_file = mocker.mock_open(read_data=json_contenido)
    mocker.patch("builtins.open", mock_file)

    ruta = "datos/usuarios.json"
    red = RedSocial.desde_json(ruta)

    mock_file.assert_called_once_with(ruta, encoding="utf-8")

    assert len(red) == 2
    assert "@ana" in red
    assert "@luis" in red
    assert red["@luis"].sigue_a(red["@ana"]) is True
    assert red["@ana"].sigue_a(red["@luis"]) is False
