"""FastAPI application entry point.

This module defines the ASGI app instance and a couple of basic endpoints
used for smoke-testing the service.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Returns a simple message indicating the API is up and running.

    **Returns**:
        - A dictionary with a "message" key
         containing the string "Hello World".
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """Greet someone by their name.

    **Parameters**:
        - `name` (str): The name of the person to greet.

    **Returns**:
        - A dictionary with a "message" key containing a personalized greeting.
    """
    return {"message": f"Hello {name}"}
