"""
Normalizes Smart Fantasy Baseball's registry
"""

import datetime
import logging

from .models import Row


def normalize_sfbb(row):
    """Normalizes a single row of SFBB data

    Args:
        row: `dict`-ified row from SFBB spreadsheet

    Returns:
        Formatted model (`Model`)
    """

    log = logging.getLogger(__name__)

    model = Row()
    model.src = 'sfbb'
    model.name_last = row['LASTNAME']
    model.name_first = row['FIRSTNAME']
    model.name_full = row['PLAYERNAME']
    model.name_lfc = row['LASTCOMMAFIRST']

    if row['BIRTHDATE']:
        try:
            birth_date = datetime.datetime.strptime(row['BIRTHDATE'],
                                                    '%m/%d/%Y')
            model.birth_date = datetime.date(
                birth_date.year,
                birth_date.month,
                birth_date.day)
        except ValueError:
            log.exception('Invalid birth date for SFBB: %s %s',
                          row['IDPLAYER'],
                          row['BIRTHDATE'])

    model.bats = row['BATS']
    model.throws = row['THROWS']
    model.team = row['TEAM']
    model.lg = row['LG']
    model.pos = row['POS']

    fg_id = row['IDFANGRAPHS']

    if fg_id.startswith('sa'):
        model.key_fangraphs_minors = fg_id
    else:
        model.key_fangraphs = fg_id

    model.key_mlbam = row['MLBID']
    model.key_cbs = row['CBSID']
    model.key_retro = row['RETROID']
    model.key_bbref = row['BREFID']
    model.key_nfbc = row['NFBCID']
    model.key_espn = row['ESPNID']
    model.key_kffl = row['KFFLNAME']
    model.key_davenport = row['DAVENPORTID']
    model.key_bpro = row['BPID']
    model.key_yahoo = row['YAHOOID']
    model.key_rotowire = row['ROTOWIREID']
    model.key_fanduel = row['FANDUELID']
    model.key_ottoneu = row['OTTONEUID']

    return model
