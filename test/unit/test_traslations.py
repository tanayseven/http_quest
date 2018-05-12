from rest_test.translations import strings as base_string
from rest_test.user.translations import strings as user_string


def assert_keys_for_all_translations(strings: dict):
    keys = list(strings.keys())
    master_key = keys.pop()
    for key in keys:
        assert set(strings[master_key].keys()) == set(strings[key].keys())


def test_that_all_keys_have_translations():
    assert_keys_for_all_translations(base_string)
    assert_keys_for_all_translations(user_string)
