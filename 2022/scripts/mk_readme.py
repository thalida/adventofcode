import os
import pathlib
import re
import sys
import parsel
import jinja2
import html2text

template_path = pathlib.Path(os.path.dirname(sys.argv[0]), './templates/README.md.jinja')
output_path = pathlib.Path(os.path.dirname(sys.argv[0]), f'../{sys.argv[2]}', 'README.md')

cb_format_pattern = re.compile(r'(`.+?`)', re.S)
def fix_inline_code_formatting(text):
    """Used to fix formatting of when inline code tags have bold tags `**bold**` inside
    """
    text = cb_format_pattern.sub(lambda m: m.group().replace('**', '`**`'), text)
    text = cb_format_pattern.sub(lambda m: m.group().replace('_', '`_`'), text)
    # Now clean up the double tick marks making sure not to replace the triple ticks
    text = re.sub(r'([^`])``([^`])', r'\1\2', text)
    return text

# First remove un needed style tag
with open(sys.argv[1], 'r') as f:
    prefix_regex = re.compile('<style data-savepage-href="/static/highcontrast.css.*</style>', re.MULTILINE|re.DOTALL)
    cleaned = re.sub(prefix_regex, '', f.read())
with open(sys.argv[1], 'w') as f:
    f.write(cleaned)

# Parse the content
problems = parsel.Selector(text=open(sys.argv[1]).read()).css('article.day-desc')

day_title = problems[0].css('h2::text').extract_first().replace('---', '').strip()

# Remove headers from the problem text. Use the one in the Readme's template
h2t = html2text.HTML2Text()
problem_part1 = h2t.handle(re.sub(r"<.?h2.*h2>", "", problems[0].extract()).strip())
problem_part2 = h2t.handle(re.sub(r"<.?h2.*h2>", "", problems[1].extract()).strip())

tm = jinja2.Template(open(template_path).read())
readme_template = tm.render(
    day_title=day_title,
    problem_part1=fix_inline_code_formatting(problem_part1),
    problem_part2=fix_inline_code_formatting(problem_part2),
)

# Save new readme to the days folder
with open(output_path, 'w') as f:
    f.write(readme_template)
