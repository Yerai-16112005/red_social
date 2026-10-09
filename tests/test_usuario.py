
import pytest


def test_seguir_anade_al_otro_usuario(ana, luis):
    ana.seguir(luis)
    assert ana.sigue_a(luis) and ana.numero_seguidos == 1 and not luis.sigue_a(ana) 

def test_seguirse_a_si_mismo_lanza_error(ana):
    with pytest.raises(ValueError):
        ana.seguir(ana) 