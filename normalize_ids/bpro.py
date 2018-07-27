"""
Normalizes Baseball Prospectus's registry
"""

import datetime
import logging

from .models import Row


def normalize_bpro(row):
    """Normalizes a single row of BP data

    Args:
        row: `dict`-ified row from BP spreadsheet

    Returns:
        Formatted model (`Model`)
    """

    log = logging.getLogger(__name__)

    model = Row()
    model.src = 'bp'
    model.name_last = row['LASTNAME']
    model.name_first = row['FIRSTNAME']
    model.name_full = row['FIRSTNAME'] + ' ' + row['LASTNAME']
    model.name_lfc = row['LASTNAME'] + ', ' + row['FIRSTNAME']

    model.key_mlbam = row['MLBCODE']
    model.key_davenport = row['DAVENPORTCODE']
    model.key_bpro = row['PLAYERID']

    return model
