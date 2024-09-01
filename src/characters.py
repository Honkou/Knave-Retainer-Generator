"""Module containing NPC classes."""

import random
from dataclasses import dataclass, field


@dataclass
class KnaveAttributes:
    """Representation of a Knave 2ed attributes. Contrary to 5e, all 6 attributes start at 0."""

    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0

    def add_first_level_attributes(self) -> None:
        """Randomly choose one attribute and increase it by one. Do it 3 times."""
        attributes = list(self.__dict__)
        for _ in range(3):
            random_stat = random.choice(attributes)
            setattr(self, random_stat, getattr(self, random_stat) + 1)

    @property
    def statistics_sum(self) -> int:
        """Return the sum of all 6 statistics. Mostly used as a sanity check."""
        total = 0
        for stat in self.__dict__:
            total += getattr(self, stat)
        return total


@dataclass
class KnaveCharacter:
    """Representation of a Knave 2ed character sheet."""

    attributes: KnaveAttributes = field(default_factory=KnaveAttributes)
