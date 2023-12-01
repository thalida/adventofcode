from helpers.rich import RichArgumentParser, RichRawTextHelpFormatter
from helpers.scripts import make_calendar, make_day, make_day_readme

parser = RichArgumentParser(
    description="Advent of Code Helper Scripts",
    formatter_class=RichRawTextHelpFormatter,
)
subparsers = parser.add_subparsers(
    title="subcommands", description="Supported commands", help="subcommands help"
)

parser_day = subparsers.add_parser("day", help="day help", aliases=["d"])
parser_day.add_argument(
    "number", type=str, help="The day number to create the files for", nargs=1
)
parser_day.set_defaults(func=make_day)


parser_day_readme = subparsers.add_parser(
    "day-readme", help="day-readme help", aliases=["dr"]
)
parser_day_readme.add_argument(
    "--day",
    "-d",
    required=True,
    type=str,
    help="The day number to create the files for",
    nargs=1,
)
parser_day_readme.add_argument(
    "--filepath",
    "-f",
    required=True,
    type=str,
    help="The path to the extracted html file",
    nargs="*",
)
parser_day_readme.set_defaults(func=make_day_readme)


parser_calendar = subparsers.add_parser(
    "calendar", help="calendar help", aliases=["cal"]
)
parser_calendar.add_argument(
    "--filepath",
    "-f",
    required=True,
    type=str,
    help="The path to the extracted html file",
    nargs="*",
)
parser_calendar.set_defaults(func=make_calendar)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
