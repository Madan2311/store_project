from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def HelloWorld():
    return html.div("Proyecto de una tienda")

app = FastAPI()
configure(app, HelloWorld)