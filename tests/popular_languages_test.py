import pytest


@pytest.mark.parametrize("expected_values", [
    (10 ** 7),
    (1.5 * 10 ** 7),
    (5 * 10 ** 7),
    (10 ** 8),
    (5 * 10 ** 8),
    (10 ** 9),
    (1.5 * 10 ** 9),
])
def test_check_websites_popularity_languages(get_parsed_websites_list, expected_values):
    errors_log = []
    for website in get_parsed_websites_list:
        if website.popularity < int(expected_values):
            errors_log.append(f"{website.website} has {website.popularity} unique visitors per month. (Expected more "
                              f"than {int(expected_values)})")
    assert not errors_log, "\n".join(errors_log)
