from re import sub

import pytest

from classes.website_row import Website
from constants.constants import CUT_SQUARE_BRACKETS_PATTERN
from constants.constants import ONLY_DIGIT_PATTERN
from utils.util_functions import get_table


@pytest.fixture
def get_parsed_websites_list():
    rows = get_table().find_all('tr')
    websites_list = []
    for row in rows[1:]:
        box = row.find_all('td')
        popularity_cut_str = sub(CUT_SQUARE_BRACKETS_PATTERN, '',  box[1].text.strip())
        website = sub(CUT_SQUARE_BRACKETS_PATTERN, '',  box[0].text.strip())
        popularity = int(sub(ONLY_DIGIT_PATTERN, '', popularity_cut_str))
        frontend = sub(CUT_SQUARE_BRACKETS_PATTERN, '',  box[2].text.strip())
        backend = sub(CUT_SQUARE_BRACKETS_PATTERN, '',  box[3].text.strip())
        websites_list.append(Website(website, popularity, frontend, backend))

    return websites_list
