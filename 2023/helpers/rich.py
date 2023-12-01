import argparse

from rich.console import Console

console = Console()


class RichArgumentParser(argparse.ArgumentParser):
    def _print_message(self, message, file=None):
        console.print(message)

    def add_argument_group(self, *args, **kwargs):
        group = super().add_argument_group(*args, **kwargs)
        group.title = f"[cyan]{group.title.title()}[/cyan]"
        return group


class RichRawTextHelpFormatter(argparse.RawTextHelpFormatter):
    def _split_lines(self, text, width):
        return [f"[yellow]{line}[/yellow]" for line in text.splitlines()]
