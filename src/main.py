# ruff: noqa: T201
"""Program entrance."""

from characters import KnaveCharacter

if __name__ == "__main__":
    John = KnaveCharacter(level=5)
    print(John)
