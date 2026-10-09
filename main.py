from red_social.publicacion import Respuesta, Retweet, Tweet
from red_social.red import RedSocial


def main():
    # 1. La red se carga desde un fichero: usuarios y quién sigue a quién
    red = RedSocial.desde_json("datos/usuarios.json")
    print(f"Usuarios registrados: {len(red)}")
    for usuario in red:
        print(f"  {usuario} sigue a {usuario.numero_seguidos}")

    # 2. Un usuario nuevo que empieza a seguir a otro
    pablo = red.registrar("Pablo", "pablo")
    print(f"\nNuevo usuario: {pablo}")
    print(f"¿Está @pablo en la red? {'@pablo' in red}")
    pablo.seguir(red["@ana"])
    print(f"¿Sigue @pablo a @ana? {pablo.sigue_a(red['@ana'])}")
    print(f"¿Sigue @ana a @pablo? {red['@ana'].sigue_a(pablo)}")

    # 3. Publicaciones de tres tipos distintos
    ana, luis, marta = red["@ana"], red["@luis"], red["@marta"]
    hola = red.publicar(Tweet(ana, "Hola a todos #python #pytest"))
    red.publicar(Respuesta(luis, "¡Bienvenida! #Python", hola))
    red.publicar(Retweet(marta, hola))
    red.publicar(Tweet(pablo, "Mi primer tweet #hola"))

    # 4. Me gusta, y cada publicación se muestra a su manera
    hola.dar_me_gusta()
    hola.dar_me_gusta()
    print("\nPublicaciones:")
    for publicacion in red.publicaciones:
        print(f"  {publicacion}  ♥ {publicacion.me_gusta}")
    print(f"\nHashtags del tweet de {ana}: {hola.hashtags}")

    # 5. Timeline y tendencias
    red.mostrar_timeline("@marta")
    print("\nTendencias:")
    for hashtag, veces in red.tendencias(2):
        print(f"  {hashtag} ({veces})")


if __name__ == "__main__":
    main()
