import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('quotas_get_quotas')
@options.galaxy_instance()


@click.option(
    "--deleted",
    help="Only return quota(s) that have been deleted",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, deleted=False):
    """Get a list of quotas
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.quotas.get_quotas(deleted=deleted)

