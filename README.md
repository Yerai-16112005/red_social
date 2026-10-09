# Red Social - Entrega Final

Implementación en Python 3.12 de una red social simplificada tipo Twitter orientada a objetos, gestionada con `uv`.

## aracterísticas

* **Gestión de usuarios:** Registro, perfiles, búsqueda y relaciones de seguimiento entre usuarios.
* **Tipos de publicaciones:** Soporte para `Tweet`, `Respuesta` y `Retweet`.
* **Hashtags y Tendencias:** Extracción automática de hashtags limpios y cálculo de las tendencias.
* **Timeline dinámico:** Generación del hilo de publicaciones de usuarios seguidos en orden cronológico inverso.
* **Persistencia:** Carga inicial de usuarios y relaciones desde archivos JSON (`datos/usuarios.json`).

## Estructura del proyecto

```text
red_social/
├── datos/
│   └── usuarios.json
├── red_social/
│   ├── publicacion.py
│   ├── red.py
│   └── usuario.py
├── tests/
│   ├── conftest.py
│   ├── test_publicacion.py
│   ├── test_red.py
│   └── test_usuario.py
├── .gitignore
├── main.py
├── pyproject.toml
└── README.md
```

## Requisitos

- Python 3.12
- uv (gestor de paquetes y entornos)

## Instalación

1. Clonar el repositorio:
```bash
  git clone [https://github.com/Yerai-16112005/red_social.git](https://github.com/Yerai-16112005/red_social.git)
  cd red_social
```

2. Instalar y sincronizar el entorno virtual:
```bash
  uv sync
```

3. Ejecutar la suite de pruebas con pytest:
```bash
  uv run pytest -v
```

4. Ejecutar el programa principal:
```bash
  uv run main.py
```