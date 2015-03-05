import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('datasets_download_dataset')
@click.argument("dataset_id", type=str)

@click.option(
    "--file_path",
    help="If the file_path argument is provided, the dataset will be streamed to disk at that path (Should not contain filename if use_default_name=True). If the file_path argument is not provided, the dataset content is loaded into memory and returned by the method (Memory consumption may be heavy as the entire file will be in memory).",
    type=str
)
@click.option(
    "--use_default_filename",
    help="If the use_default_name parameter is True, the exported file will be saved as file_path/%s, where %s is the dataset name. If use_default_name is False, file_path is assumed to contain the full file path including filename.",
    is_flag=True
)
@click.option(
    "--wait_for_completion",
    help="If wait_for_completion is True, this call will block until the dataset is ready. If the dataset state becomes invalid, a DatasetStateException will be thrown.",
    is_flag=True
)
@click.option(
    "--maxwait",
    help="Time (in seconds) to wait for dataset to complete. If the dataset state is not complete within this time, a DatasetTimeoutException will be thrown.",
    type=float
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, dataset_id, file_path="", use_default_filename=True, wait_for_completion=False, maxwait=12000):
    """Downloads the dataset identified by 'id'.
    """
    return ctx.gi.datasets.download_dataset(dataset_id, file_path=file_path, use_default_filename=use_default_filename, wait_for_completion=wait_for_completion, maxwait=maxwait)