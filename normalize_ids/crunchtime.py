"""
Normalizes Smart Fantasy Baseball's registry
"""

import datetime
import logging

from .models import Row


def normalize_crunchtime(row):
    """Normalizes a single row of Crunchtime Baseball data

    Args:
        row: `dict`-ified row from Crunchtime Baseball spreadsheet

    Returns:
        Formatted model (`Model`)
    """

    log = logging.getLogger(__name__)

    model = Row()
    model.src = 'ct'
    model.name_full = row['mlb_name']

    model.bats = row['bats']
    model.throws = row['throws']
    model.team = row['mlb_team']

    try:
        mlb_played_first = datetime.datetime.strptime(row['debut'],
                                                      r'%Y%m%d')
        model.mlb_played_first = datetime.date(mlb_played_first.year,
                                               mlb_played_first.month,
                                               mlb_played_first.day)
    except ValueError:
        log.exception('Invalid debut date for Crunchtime %s: %s',
                      model.name_full,
                      row['debut'])

    # combine positions from each source, remove empty
    positions = (row['espn_pos'], row['cbs_pos'], row['mlb_pos'],
                 row['nfbc_pos'], row['yahoo_pos'], row['ottoneu_pos'])
    model.pos = ','.join(set(filter(lambda p: p.strip(), positions)))

    model.key_mlbam = row['mlb_id']
    model.key_bpro = row['bp_id']
    model.key_bbref = row['bref_id']
    model.key_cbs = row['cbs_id']
    model.key_espn = row['espn_id']
    model.key_nfbc = row['nfbc_id']
    model.key_retro = row['retro_id']
    model.key_yahoo = row['yahoo_id']
    model.key_ottoneu = row['ottoneu_id']

    fg_id = row['fg_id']

    if fg_id.startswith('sa'):
        model.key_fangraphs_minors = fg_id
    else:
        model.key_fangraphs = fg_id

    return model
