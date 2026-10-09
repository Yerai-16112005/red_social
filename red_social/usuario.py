class Usuario:
    def __init__(self, nombre, alias):
        self.nombre = nombre
        if not alias.startswith("@"):
            alias = "@" + alias
        self.alias = alias
        self.seguidos = []

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["nombre"], datos["alias"])

    @property
    def numero_seguidos(self) -> int:
        return len(self.seguidos)

    def __eq__(self, otro) -> bool:
        return self.alias == otro.alias

    def __str__(self) -> str:
        return f"{self.nombre} ({self.alias})"

    def a_dict(self) -> dict:
        return {"nombre": self.nombre, "alias": self.alias}

    def seguir(self, otro) -> None:
        if self == otro:
            raise ValueError(f"{self.alias} no puede seguirse a si mismo")
        elif otro in self.seguidos:
            raise ValueError(f"Usted ya sigue a {otro.alias}")

        self.seguidos.append(otro)

    def sigue_a(self, otro) -> bool:
        return otro in self.seguidos
