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

    @property
    def base_attributes(self) -> dict:
        """Return the base attributes as a dictionary."""
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
        }

    def _increase_attribute(self, attribute: str) -> None:
        """Increase the value of the attribute by one."""
        setattr(self, attribute, getattr(self, attribute) + 1)

    def add_first_level_attributes(self) -> None:
        """Randomly choose one attribute and increase it by one. Do it 3 times."""
        for _ in range(3):
            random_stat = random.choice(list(self.base_attributes.keys()))
            self._increase_attribute(random_stat)

    @property
    def statistics_sum(self) -> int:
        """Return the sum of all 6 statistics. Mostly used as a sanity check."""
        total = 0
        for stat in self.base_attributes.values():
            total += stat
        return total


@dataclass
class KnaveCharacter:
    """Representation of a Knave 2ed character sheet."""

    attributes: KnaveAttributes = field(default_factory=KnaveAttributes)
