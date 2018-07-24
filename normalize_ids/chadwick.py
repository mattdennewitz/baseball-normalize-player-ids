"""
Normalizes Chadwick's registry
"""

import datetime
import logging

from .models import Row, MODEL_FIELDNAMES


def normalize_chadwick(row):
    """Normalizes a single row of Chadwick data

    Args:
        row: `dict`-ified row from Chadwickspreadsheet

    Returns:
        Formatted model (`Model`)
    """

    log = logging.getLogger(__name__)

    model = Row()
    model.src = 'cw'
    model.name_last = row['name_last']
    model.name_first = row['name_first']
    model.name_given = row['name_given']
    model.name_full = f'{model.name_first} {model.name_last}'
    model.name_lfc = f'{model.name_last}, {model.name_first}'

    if all((row['birth_year'], row['birth_month'], row['birth_day'])):
        try:
            model.birth_date = datetime.date(int(row['birth_year']),
                                             int(row['birth_month']),
                                             int(row['birth_day']))
        except ValueError:
            bad_date = f"{row['birth_year']}-{row['birth_month']}-{row['birth_day']}"
            log.exception('Invalid birth date for Chadwick %s: %s',
                          row['key_uuid'],
                          bad_date)

    model.pro_played_first = row.get('pro_played_first')
    model.pro_played_last = row.get('pro_played_last')
    model.mlb_played_first = row.get('mlb_played_first')
    model.mlb_played_last = row.get('mlb_played_last')

    model.bats = row.get('bats')
    model.throws = row.get('throws')

    key_fields = filter(lambda k: k.startswith('key_'), MODEL_FIELDNAMES)
    for key in key_fields:
        setattr(model, key, row.get(key))

    return model
