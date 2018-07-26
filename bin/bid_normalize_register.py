"""
CLI for normalization
"""

import csv

import click

from normalize_ids import (MODEL_FIELDNAMES,
                           normalize_bpro,
                           normalize_chadwick,
                           normalize_crunchtime,
                           normalize_sfbb)


TRANSLATORS = {
    'bpro': normalize_bpro,
    'chadwick': normalize_chadwick,
    'crunchtime': normalize_crunchtime,
    'sfbb': normalize_sfbb,
}

@click.command('normalize')
@click.option('-s', 'system', required=True,
              type=click.Choice(TRANSLATORS.keys()))
@click.option('-i', 'input_path', required=True,
              type=click.Path(exists=True, dir_okay=False))
@click.option('-o', 'output_fp', type=click.File('w'), required=True)
def normalize_id_registry(system, input_path, output_fp):
    """Normalizes a given ID registry
    """

    # watch encoding from crunchtime :/
    encoding = 'latin-1' if system in ('crunchtime', 'bpro') else 'utf-8'

    reader = csv.DictReader(open(input_path, encoding=encoding))
    writer = csv.DictWriter(output_fp, MODEL_FIELDNAMES)
    writer.writeheader()

    translator_fn = TRANSLATORS[system]

    for row in reader:
        model = translator_fn(row)
        writer.writerow(dict(model))

    click.echo(f'Wrote to {output_fp.name}')


if __name__ == '__main__':
    normalize_id_registry() # pylint: disable=no-value-for-parameter
