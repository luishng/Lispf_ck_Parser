import ox
import click
import pprint

@click.command()
@click.argument('lispf_data', type=click.File('r'))
def ast(lispf_data):

    lexer = ox.make_lexer([
        ('NUMBER', r'\d+'),
        ('NAME', r'[a-zA-Z]+'),
        ('LPARAN', r'[(]'),
        ('RPARAN', r'[)]'),
    ])
    tokens_list = ['NUMBER', 'NAME', 'LPARAN', 'RPARAN', 'COMMENT', 'NEWLINE']