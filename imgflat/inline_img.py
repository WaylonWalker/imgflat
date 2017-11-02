import os
import glob
import base64
from jinja2 import Environment, FileSystemLoader
import click

env = Environment(loader=FileSystemLoader('templates'))


@click.command(help='hi')
@click.option('--output',
    default='default.md',
    help='output filename and extension')
def inline(
    output,
    img_types=['*.png', '*.jpg'],
):
    
    basename = os.path.basename(os.getcwd())
    
    if output == 'default.md':
        output = f'{basename}.md'

    output_type = os.path.splitext(output)[1]
    print(f'{output}: type;{output_type}')


    if output_type in ['.markdown', '.md', '.multimarkdown', '.multi-markdown']:
        template = env.get_template('markdown.md')
    elif output_type in ['.html', '.htm']:
        template = env.get_template('html.html')
    else:
        click.echo(f'output type {output_type} not supported')

    files = []
    for type in img_types:
        files.extend(glob.glob(type))

    encoded = {}
    for file in files:
        with open(file, 'rb') as f:
            encoded[file] = base64.b64encode(f.read()).decode('utf-8')

    body = template.render(directory=basename, files=encoded)

    with open(output, 'wb') as f:
        f.write(body.encode('utf-8'))

if __name__ == '__main__':

    inline()
