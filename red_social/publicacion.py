from abc import ABC, abstractmethod

LIMITE_CARACTERES = 280


class Publicacion(ABC):
    def __init__(self, autor, texto):
        if not texto or len(texto.strip()) == 0:
            raise ValueError("El texto no puede ser vacio")
        elif len(texto) > LIMITE_CARACTERES:
            raise ValueError("El texto no puede exceder el maximo de caracteres")
        self.autor = autor
        self.texto = texto
        self.me_gusta = 0

    @abstractmethod
    def __str__(self) -> str:
        """Mostrar publicacion por pantalla"""

    @staticmethod
    def extraer_hashtags(texto) -> list[str]:
        hashtags = []
        vistos = set()

        for palabra in texto.split():
            palabra_limpia = palabra.rstrip(",.;:!?¡¿").lower()
            if (
                palabra_limpia.startswith("#")
                and len(palabra_limpia) > 1
                and palabra_limpia not in vistos
            ):
                vistos.add(palabra_limpia)
                hashtags.append(palabra_limpia)

        return hashtags

    @property
    def hashtags(self) -> list[str]:
        return Publicacion.extraer_hashtags(self.texto)

    def dar_me_gusta(self):
        self.me_gusta += 1


class Tweet(Publicacion):
    def __str__(self) -> str:
        return f"{self.autor.alias}: {self.texto}"


class Respuesta(Publicacion):
    def __init__(self, autor, texto, original):
        super().__init__(autor, texto)
        self.original = original

    def __str__(self) -> str:
        return f"{self.autor.alias} ↩ {self.original.autor.alias}: {self.texto}"


class Retweet(Publicacion):
    def __init__(self, autor, original):
        super().__init__(autor, original.texto)
        self.original = original

    def __str__(self) -> str:
        return f"{self.autor.alias} 🔁 {self.original}"
