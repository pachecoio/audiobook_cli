from flask import Flask
import click
from book_controller import BookController, BookException

app = Flask(__name__)

@app.cli.command("read")
@click.argument("book", required=True)
@click.argument("page_start", required=True, type=int)
@click.argument("page_end", required=True, type=int)
def read_book(book, page_start, page_end):
    click.echo("Read book {}".format(book))
    book_controller = BookController(filename=book)
    try:
        limit = page_end if page_end < len(book_controller.images) else len(book_controller.images)
        for page in range(page_start, limit):
            book_controller.read_page(page)
            print("read page {}".format(page))
            book_controller.run()
    except BookException as err:
        click.echo(err.message)
    except Exception as err:
        click.echo("Error found")

app.run()
