import os
import pathlib
import re
import sys
import parsel
import jinja2
import html2text

template_path = pathlib.Path(os.path.dirname(sys.argv[0]), './templates/readmes/index.md.jinja')
output_path = pathlib.Path(os.path.dirname(sys.argv[0]), '../README.md')

def fix_formatting(text):
    return text.replace('*', '⭐️')

h2t = html2text.HTML2Text()
h2t.ignore_links = True
calendar_html = parsel.Selector(text=open(sys.argv[1]).read()).css('.calendar')
calendar = h2t.handle(calendar_html[0].extract().strip())

tm = jinja2.Template(open(template_path).read())
readme_template = tm.render(
    calendar=fix_formatting(calendar),
)

with open(output_path, 'w') as f:
    f.write(readme_template)
