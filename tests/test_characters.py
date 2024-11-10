"""Tests suite for characters."""

import pytest

from characters import KnaveAttributes, KnaveCharacter


class TestKnaveCharacter:

    def test_default_character_creation(self):
        """Assert that a default new character has all attributes set to 0."""
        character = KnaveCharacter()
        for value in character.attributes.base_attributes.values():
            assert value == 0

    def test_1st_level_character_creation(self):
        """Assert that a 1st level character has a level of 1."""
        character = KnaveCharacter(level=1)
        assert character.level == 1
        assert character.attributes.statistics_sum == 3

    def test_2nd_level_character_creation(self):
        """Assert that a 2nd level character has a level of 2."""
        character = KnaveCharacter(level=2)
        assert character.level == 2
        assert character.attributes.statistics_sum == 6

    def test_character_creation_below_zero(self):
        """Assert that a character with a level below 0 is not allowed."""
        with pytest.raises(ValueError, match="Character level cannot be negative."):
            _ = KnaveCharacter(level=-1)

    def test_character_creation_above_max_level(self):
        """Assert that a character with a level above the maximum is not allowed."""
        with pytest.raises(ValueError, match="Character level cannot exceed 10."):
            _ = KnaveCharacter(level=11)

    def test_character_leveling_above_max_level(self):
        """Assert that a character cannot level up above the maximum level."""
        character = KnaveCharacter(10)
        with pytest.raises(ValueError, match="Character level cannot exceed 10."):
            character.level_up(1)


class TestKnaveAttributes:

    def test_1st_level_statistics_creation(self):
        """Assert that a 1st level character has a total of 3 points in stats."""
        attributes = KnaveAttributes()
        attributes.add_first_level_attributes()
        assert attributes.statistics_sum == 3

    def test_increase_random_attributes(self):
        """Assert that the sum of the stats increased is 3 and no stat is higher than 1."""
        attributes = KnaveAttributes()
        attributes.increase_random_attributes(3)
        assert attributes.statistics_sum == 3
        for value in attributes.base_attributes.values():
            assert value <= 1
