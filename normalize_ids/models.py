"""
Defines post-normalization model for baseball registry schemas
"""

# pylint: disable=too-many-instance-attributes

import collections

from schematics.models import Model
from schematics.types import DateType, IntType, StringType


__all__ = ('Row', 'MODEL_FIELDNAMES', )

class Row(Model):
    """Defines the normalized state of a transitioned baseball registry
    """

    src = StringType()

    name_last = StringType()
    name_first = StringType()
    name_given = StringType()
    name_full = StringType()
    name_lfc = StringType()

    birth_date = DateType()
    team = StringType()
    lg = StringType()
    pos = StringType()
    bats = StringType()
    throws = StringType()
    pro_played_first = IntType()
    pro_played_last = IntType()
    mlb_played_first = IntType()
    mlb_played_last = IntType()

    key_bbref = StringType()
    key_bbref_minors = StringType()
    key_bpro = StringType()
    key_cbs = StringType()
    key_davenport = StringType()
    key_espn = StringType()
    key_fanduel = StringType()
    key_fangraphs = StringType()
    key_fangraphs_minors = StringType()
    key_kbo = StringType()
    key_kffl = StringType()
    key_nfbc = StringType()
    key_npb = StringType()
    key_mlbam = StringType()
    key_retro = StringType()
    key_rotowire = StringType()
    key_yahoo = StringType()


MODEL_FIELDNAMES = list(filter(lambda k: not k.startswith('_'),
                               collections.OrderedDict(Row())))
