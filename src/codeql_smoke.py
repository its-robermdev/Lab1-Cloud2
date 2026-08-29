"""Módulo mínimo para validar el análisis de Python con CodeQL."""


def codeql_smoke_check() -> str:
    """Devuelve un estado estable para mantener un punto analizable."""
    return "ok"


if __name__ == "__main__":
    print(codeql_smoke_check())
