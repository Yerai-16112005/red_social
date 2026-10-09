import json
from collections import Counter
from collections.abc import Iterator

from red_social.publicacion import Publicacion
from red_social.usuario import Usuario


class RedSocial:
    def __init__(self):
        self.usuarios = {}
        self.publicaciones = []

    @classmethod
    def desde_json(cls, ruta):
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)

        red = cls()
        for dic_user in datos["usuarios"]:
            red.anadir(Usuario.desde_dict(dic_user))

        for quien_sigue, a_quien in datos["seguimientos"]:
            red.usuarios[quien_sigue].seguir(red.usuarios[a_quien])

        return red

    def __len__(self) -> int:
        return len(self.usuarios)

    def __iter__(self) -> Iterator[Usuario]:
        return iter(sorted(self.usuarios.values(), key=lambda u: u.alias))

    def __contains__(self, alias) -> bool:
        return alias in self.usuarios

    def __getitem__(self, alias) -> Usuario:
        if alias not in self:
            raise KeyError(f"El alias {alias} no existe")
        return self.usuarios[alias]

    def anadir(self, usuario) -> Usuario:
        if usuario.alias in self:
            raise ValueError("El alias ya existe")
        self.usuarios[usuario.alias] = usuario
        return usuario

    def registrar(self, nombre, alias) -> Usuario:
        user = Usuario(nombre, alias)
        return self.anadir(user)

    def publicar(self, publicacion) -> Publicacion:
        self.publicaciones.append(publicacion)
        return publicacion

    def timeline(self, usuario) -> list[Publicacion]:
        return [p for p in reversed(self.publicaciones) if p.autor in usuario.seguidos]

    def tendencias(self, n: int = 3) -> list[tuple[str, int]]:
        todos_los_hashtags = []
        for p in self.publicaciones:
            todos_los_hashtags.extend(p.hashtags)

        contador = Counter(todos_los_hashtags)
        return contador.most_common(n)

    def mostrar_timeline(self, alias):
        print()
        print(f"Timeline de {self.usuarios[alias]}:")
        for p in self.timeline(self.usuarios[alias]):
            print(f"  {p}  ♥ {p.me_gusta}")
