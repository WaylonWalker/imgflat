import os
import glob
import base64
from jinja2 import Environment, PackageLoader, select_autoescape
import click

env = Environment(
    loader=PackageLoader('imgflat', 'templates'),
    autoescape=select_autoescape(['html', '.md']),
)

@click.command(help='A tool for creating a flat file containing all of the images in a directory inline.')
@click.option('--output',
    default='default.md',
    help='output filename and extension')
@click.option('--recursive',
              is_flag=True,
              default=False,
              help='Recurse through file system or use top level directory only')
def inline(
    output,
    recursive,
    img_types=['*.png', '*.jpg'],
):
    
    basename = os.path.basename(os.getcwd())
    
    if output == 'default.md':
        output = f'images in {basename}.md'

    output_type = os.path.splitext(output)[1]

    if output_type in ['.markdown', '.md', '.multimarkdown', '.multi-markdown']:
        template = env.get_template('markdown.md')
    elif output_type in ['.html', '.htm']:
        template = env.get_template('html.html')
    else:
        click.echo(f'output type {output_type} not supported')

    if recursive:
        img_types = [f'**/*{img_type}' for img_type in img_types]

    files = []
    for type in img_types:
        files.extend(glob.glob(type, recursive=recursive))

    encoded = {}
    for file in files:
        with open(file, 'rb') as f:
            encoded[file] = base64.b64encode(f.read()).decode('utf-8')

    body = template.render(directory=basename, files=encoded)

    with open(output, 'wb') as f:
        f.write(body.encode('utf-8'))

if __name__ == '__main__':

    inline()
