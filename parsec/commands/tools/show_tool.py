import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('show_tool')
@click.argument("tool_id", type=str)

@click.option(
    "--io_details",
    help="if True, get also input and output details",
    is_flag=True
)
@click.option(
    "--link_details",
    help="if True, get also link details",
    is_flag=True
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, tool_id, io_details=False, link_details=False):
    """Get details of a given tool.

Output:

    
    """
    return ctx.gi.tools.show_tool(tool_id, io_details=io_details, link_details=link_details)
