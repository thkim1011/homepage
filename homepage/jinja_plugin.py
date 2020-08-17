import re

JINJA_STATEMENT_PATTERN = re.compile(r'\{\%(.*)\%\}')
JINJA_EXPRESSION_PATTERN = r'\{\{(.*)\}\}'
JINJA_COMMENT_PATTERN = r'\{\#(.*)\#\}'

def parse_jinja_statement(self, m, state):
    return 'jinja_statement', m.group(0)
   
def render_jinja_statement(string):
    return string + 'test'

def plugin_jinja(md):
    md.block.register_rule(
        'jinja_statement',
        JINJA_STATEMENT_PATTERN,
        parse_jinja_statement
    )
    md.block.rules.append('jinja_statement')

    if md.renderer.NAME == 'html':
        md.renderer.register('jinja_statement', render_jinja_statement)
