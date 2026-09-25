"""Точка входа приложения."""

from utils import add


def main() -> None:
    """Запускает приложение."""
    result = add(2, 3)
    print(f"Hello, project-structure-lab! 2 + 3 = {result}")


if __name__ == "__main__":
    main()