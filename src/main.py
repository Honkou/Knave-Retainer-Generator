# ruff: noqa: T201
"""Program entrance."""

from characters import KnaveCharacter
from web_generators import ChartopiaTables, get_random_names


def main() -> None:
    """Run the main program."""
    names = get_random_names(ChartopiaTables.DND_NPC_NAMES.value, 5)
    npcs = []
    for name in names:
        npcs.append(KnaveCharacter(level=5, name=name))
    print(npcs)


if __name__ == "__main__":
    main()
