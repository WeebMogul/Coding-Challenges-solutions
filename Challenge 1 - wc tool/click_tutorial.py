import click

# @click.command()
# def hello():
#     click.echo("Hello There")

# if __name__ == "__main__":
#     hello()

# @click.command()
# @click.argument('name', default='guest')
# @click.argument('age', type=int)
# def hello(name, age):
#     click.echo(f'Hello {name}, you are {age} years old')

# if __name__ == '__main__':
#     hello()

# @click.command()
# @click.option('--n', type=int, default=1)
# def dots(n):
#     click.echo('.'*n)

# if __name__ == '__main__':
#     dots()

# @click.command()
# @click.option("--name", prompt="Your name", help="Provide your name")
# def hello(name):
#     click.echo(f"Hello, {name}")

# if __name__ == "__main__":
#     hello()

# @click.command()
# @click.option('--blue', is_flag=True, help='message in blue color')
# def hello(blue):

#     if blue:
#         click.secho('Hello there', fg='blue')
#     else:
#         click.secho('Hello there')

# if __name__ == "__main__":
#     hello()

# @click.command()
# @click.argument('file_name',type=click.File('r'))
# @click.argument('lines', default=-1, type=int)

# def head(file_name, lines):
#     counter = 0

#     for line in file_name:
#         print(line.strip())
#         counter += 1

#         if counter == lines:
#             break

# if __name__ == "__main__":
#     head()

# @click.command()
# @click.argument('file_name',type=click.Path(exists=True))
# @click.argument('lines', default=-1, type=int)
# def head(file_name, lines):

#     with open(file_name, 'r') as f:

#         counter = 0

#         for line in f:
#             print(line.strip())
#             counter += 1

#             if counter == lines:
#                 break

# if __name__ == "__main__":
#     head()

# @click.group()
# def messages():
#     pass

# @click.command()
# def generic():
#     click.echo("Hello there")

# @click.command()
# def welcome():
#     click.echo("Welcome")

# messages.add_command(generic)
# messages.add_command(welcome)

# if __name__=='__main__':
#     messages()

@click.group()
def cli():
    pass

@cli.command(name='gen')
def generic():
    click.echo("Hello there")

@cli.command(name='wel')
def welcome():
    click.echo("Welcome")

if __name__=="__main__":
    cli()