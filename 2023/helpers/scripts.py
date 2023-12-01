import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

import html2text
import jinja2
import parsel
from rich import pretty
from rich.console import Console
from rich.text import Text

pretty.install()

console = Console()

templates_dir = Path(__file__).resolve().parent.parent / "templates"


def make_day(args):
    day_number = args.number[0]

    console.print(f":santa: Make Day {day_number} \n", style="bold blue")

    template = templates_dir / "day"
    output = Path.cwd() / f"day-{day_number}"

    try:
        shutil.copytree(template, output)
    except FileExistsError:
        console.print("Oops: Day already exists", style="bold red")
        return

    console.print(
        ":file_folder: Output:",
        Text.from_markup(f"[link={output}]{output}[/link]"),
        style="white bright_cyan",
    )
    console.print("\nDone :tada:", style="bold green")


def make_calendar(args):
    console.print(":calendar: Make Calendar \n", style="bold blue")

    filepath = " ".join(args.filepath)
    extracted_html_path = Path(sys.path[0], filepath)

    console.print(
        ":globe_with_meridians: Input:",
        Text.from_markup(f"[link={extracted_html_path}]{extracted_html_path}[/link]"),
        style="bold white",
    )

    template = templates_dir / "year.README.jinja"
    output = Path.cwd() / "README.md"

    with open(extracted_html_path, "r") as f:
        html_file = f.read()
        html_file = html_file.replace(
            '<span class="calendar-mark-complete">*</span>', "⭐️"
        )
        html_file = html_file.replace(
            '<span class="calendar-mark-verycomplete">*</span>', "⭐️"
        )

    calendar_html = parsel.Selector(text=html_file).css(".calendar")
    calendar_html.css("#calendar-countdown").drop()

    h2t = html2text.HTML2Text()
    h2t.ignore_links = True
    calendar = h2t.handle(calendar_html[0].extract().strip())

    tm = jinja2.Template(open(template).read())
    formatted_calendar = tm.render(calendar=calendar)

    with open(output, "w") as f:
        f.write(formatted_calendar)

    console.print(
        ":page_facing_up: Output:",
        Text.from_markup(f"[link={output}]{output}[/link]"),
        style="white bright_cyan",
    )
    console.print("\nDone :tada:", style="bold green")


def make_day_readme(args):
    console.print(":pencil: Make Day Readme \n", style="bold blue")

    extracted_html_path = " ".join(args.filepath)

    template = templates_dir / "day.README.jinja"
    output = Path.cwd() / f"day-{args.day[0]}" / "README.md"

    cb_format_pattern = re.compile(r"(`.+?`)", re.S)

    def fix_inline_code_formatting(text):
        """Used to fix formatting of when inline code tags have bold tags `**bold**` inside"""
        text = cb_format_pattern.sub(lambda m: m.group().replace("**", "`**`"), text)
        text = cb_format_pattern.sub(lambda m: m.group().replace("_", "`_`"), text)
        # Now clean up the double tick marks making sure not to replace the triple ticks
        text = re.sub(r"([^`])``([^`])", r"\1\2", text)
        return text

    # First remove un needed style tag
    try:
        with open(extracted_html_path, "r") as f:
            prefix_regex = re.compile(
                '<style data-savepage-href="/static/highcontrast.css.*</style>',
                re.MULTILINE | re.DOTALL,
            )
            cleaned = re.sub(prefix_regex, "", f.read())

        with open(extracted_html_path, "w") as f:
            f.write(cleaned)
    except FileNotFoundError:
        console.print(
            "Oops: File not found:", quote(extracted_html_path), style="bold red"
        )
        return

    # Parse the content
    problems = parsel.Selector(text=open(extracted_html_path).read()).css(
        "article.day-desc"
    )

    day_title = problems[0].css("h2::text").extract_first().replace("---", "").strip()

    # Remove headers from the problem text. Use the ones in the Readme template
    h2t = html2text.HTML2Text()
    problem_part1 = h2t.handle(re.sub(r"<.?h2.*h2>", "", problems[0].extract()).strip())
    problem_part2 = h2t.handle(re.sub(r"<.?h2.*h2>", "", problems[1].extract()).strip())

    tm = jinja2.Template(open(template).read())
    readme_template = tm.render(
        day_title=day_title,
        problem_part1=fix_inline_code_formatting(problem_part1),
        problem_part2=fix_inline_code_formatting(problem_part2),
    )

    # Save new readme to the days folder
    with open(output, "w") as f:
        f.write(readme_template)

    console.print(
        ":page_facing_up: Output:",
        Text.from_markup(f"[link={output}]{output}[/link]"),
        style="white bright_cyan",
    )
    console.print("\nDone :tada:", style="bold green")
