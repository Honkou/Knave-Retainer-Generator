"""Module containing NPC classes."""

import random
from dataclasses import dataclass

_MAX_KNAVE_LEVEL = 10


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

    def increase_random_attributes(self, amount_of_attributes: int = 3) -> None:
        """Increase multiple random attributes by 1, with no duplicates."""
        attrs_to_increase = random.sample(list(self.base_attributes.keys()), amount_of_attributes)
        for attribute in attrs_to_increase:
            self._increase_attribute(attribute)

    @property
    def statistics_sum(self) -> int:
        """Return the sum of all 6 statistics. Mostly used as a sanity check."""
        total = 0
        for stat in self.base_attributes.values():
            total += stat
        return total


class KnaveCharacter:
    """Representation of a Knave 2ed character sheet."""

    def __init__(self, level: int = 0, name: str = "John") -> None:
        """Initialize the character with a level and attributes."""
        self._level = 0
        self._name = name
        self._attributes = KnaveAttributes()

        self._validate_level(level)
        if level > 0:
            self._level = 1
            self._attributes.add_first_level_attributes()
        if level > 1:
            self.level_up(level - 1)

    def __repr__(self) -> str:
        """Return the character's representation."""
        return f"{self._name} - Level {self.level}. Attributes:\n{self.attributes.base_attributes}\n"

    @property
    def level(self) -> int:
        """Return the character's level."""
        return self._level

    def _validate_level(self, level: int) -> None:
        """Validate the level-up is legal before increasing it."""
        if self._level + level > _MAX_KNAVE_LEVEL:
            raise ValueError(f"Character level cannot exceed {_MAX_KNAVE_LEVEL}.")
        if self._level + level < 0:
            raise ValueError("Character level cannot be negative.")

    @property
    def name(self) -> str:
        """Return the character's name."""
        return self._name

    @property
    def attributes(self) -> KnaveAttributes:
        """Return the character's attributes class."""
        return self._attributes

    def level_up(self, amount: int = 1) -> None:
        """Increase the character's level by the amount specified."""
        self._validate_level(amount)
        self._level += amount
        for _ in range(amount):
            self._attributes.increase_random_attributes(3)
