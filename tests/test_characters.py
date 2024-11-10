"""Tests suite for characters."""

from characters import KnaveAttributes, KnaveCharacter


def test_default_character_creation():
    """Assert that a default new character has all attributes set to 0."""
    character = KnaveCharacter()
    for value in character.attributes.base_attributes.values():
        assert value == 0


def test_1st_level_statistics_creation():
    """Assert that a 1st level character has a total of 3 points in stats."""
    attributes = KnaveAttributes()
    attributes.add_first_level_attributes()
    assert attributes.statistics_sum == 3
