"""Tests suite for characters."""

from dataclasses import asdict

from characters import KnaveAttributes, KnaveCharacter


def test_default_character_creation():
    character = KnaveCharacter()
    for _, value in asdict(character.attributes).items():
        assert value == 0


def test_1st_level_statistics_creation():
    attributes = KnaveAttributes()
    attributes.add_first_level_attributes()
    assert attributes.statistics_sum == 3
