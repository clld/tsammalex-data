# coding: utf8
from __future__ import unicode_literals, print_function, division

import pytest
from mock import Mock

from pytsammalex.models import regex_validator, convert_date, \
    valid_coordinates, Images


def test_validators():
    with pytest.raises(ValueError):
        regex_validator('[a-z]+', None, Mock(), '')

    regex_validator('[a-z]+', None, Mock(), '', allow_empty=True)

    with pytest.raises(ValueError):
        convert_date('2008Jan21')

    with pytest.raises(ValueError):
        valid_coordinates(None, Mock(), (91.0, 45.0))


def test_images():
    row = "47a4a90a6fb76d027e7db2d383973e1d,motacillaflava,general;thumbnail1," \
          "image/jpeg,,,2008-12-28,,50.567634 30.301384," \
          "https://creativecommons.org/," \
          "http://commons.wikimedia.org/wiki/File:Motacilla_flava_Horenka2.jpg," \
        .split(',')
    assert (Images(*row).csv_row() == row)
