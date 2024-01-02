import click
import sys

# Create custom CLI commands
@click.command()

# CLI argument to add the file or data
@click.argument('file_data',type=click.File('r'),default=sys.stdin)

# CLI options to execute when applied 
@click.option('-c', help = "Display count of bytes in the file", default=False, is_flag=True)
@click.option('-l', help = "Display count of lines in the file", default=False, is_flag=True)
@click.option('-w', help = "Display count of words in the file", default=False, is_flag=True)
@click.option('-m', help = "Display count of characters in the file", default=False, is_flag=True)

def main(file_data,c,l,w,m):

    # check if the file has a name or whether it came from standard input 
    file_name = file_data.name if file_data.name != "<stdin>" else " "

    file_content = file_data.read()
    
    # display count of bytes in the text
    if c:
        click.echo(f"{byte_count(file_content)} {file_name}")
    # display count of lines in the text
    if l:
        click.echo(f"{line_count(file_content)} {file_name}")
    # display count of words in the text
    if w:
        click.echo(f"{word_count(file_content)} {file_name}")
    # display count of characters in the text
    if m:
        click.echo(f"{char_count(file_content)} {file_name}")
    if not any([c,l,w,m]):
        click.echo(f"{line_count(file_content)} {word_count(file_content)} {char_count(file_content)} {file_name}")
    
def byte_count(file_name):
    return len(file_name.encode('utf-8'))

def line_count(file_name):
    return len(file_name.split("\n"))

def word_count(file_name):
    return len(file_name.split())

def char_count(file_name):
    return len(file_name)

if __name__=="__main__":
    main()