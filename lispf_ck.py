import ox
import click
import pprint

@click.command()
@click.argument('lispf_data', type=click.File('r'))
def ast(lispf_data):

    lexer = ox.make_lexer([
        ('NUMBER', r'\d+'),
        ('NAME', r'[-a-zA-Z]+'),
        ('LPARAN', r'[(]'),
        ('RPARAN', r'[)]'),
        ('COMMENT', r';.*'),
        ('NEWLINE', r'\s+'),
    ])
    tokens_list = ['NAME', 'NUMBER', 'LPARAN', 'RPARAN']
    parser = ox.make_parser([
        ('stmt : LPARAN RPARAN', lambda x,y: '()'),
        ('stmt : LPARAN expr RPARAN', lambda x,y,z: y),
        ('expr : term expr', lambda x,y: (x,) + y),
        ('expr : term', lambda x: (x,)),
        ('term : stmt', lambda x: x),
        ('term : NUMBER', lambda x: x),
        ('term : NAME', lambda x: x),
    ], tokens_list)

    data = lispf_data.read()
    print(lexer(data))

ast()