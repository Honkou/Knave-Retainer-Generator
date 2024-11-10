"""Module containing functions that call REST APIs to generate RPG content, such as NPC names."""

from enum import Enum

import requests


class ChartopiaTables(Enum):
    """Enum containing the Chartopia tables' IDs used in the API calls."""

    DND_NPC_NAMES = 19


def get_random_names(chart_id: int, amount: int = 1) -> list[str]:
    """Return a list of random names from the Chartopia API."""
    if amount > 5:
        amount = 5
    data = {"mult": amount}
    response = requests.post(f"https://chartopia.d12dev.com/api/charts/{chart_id}/roll/", data=data)
    return response.json()["results"]
