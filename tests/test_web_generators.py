from src.web_generators import ChartopiaTables, get_random_names


def test_get_random_name():
    """Assert that the API call returns a dictionary with a name."""
    name = get_random_names(ChartopiaTables.DND_NPC_NAMES.value)[0]
    assert isinstance(name, str)
    assert name != ""


def test_get_random_names_over_limit():
    """Assert that exceeding the API limit of 5 still returns 5 names."""
    too_many_names = 15
    name = get_random_names(ChartopiaTables.DND_NPC_NAMES.value, too_many_names)
    assert len(name) == 5
