# The Void

A Flask app that accepts any kind of HTTP request, in any path and just returns
a default message and an HTTP-200.

The code is quite simple. If you're curious or just want to implement something like this yourself, do take a look at the source.

## Running

Clone this repository to your machine and then choose you preferred method

### Docker

1. Build the image

    ```bash
    docker build . -t the_void
    ```

2. Run it

    ```bash
    docker run -it -p 5000:5000 the_void
    ```

The app will be accessible in your machine's 5000 port

### Poetry

1. Install [poetry](https://github.com/sdispater/poetry)

2. Install this project dependencies by going to its directory and issuing an
`poetry install` command

3. Run it `poetry run python the_void.py`

## License

MIT
