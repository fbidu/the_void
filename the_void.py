"""
A very simple Flask app that accepts calls from
any method on any endpoint and just ignores it
without erroring or returning anything
"""
from flask import Flask, jsonify
from werkzeug.routing import Rule


app = Flask(__name__)

"""
Here is the trick to allow for requests from any path with any method.

The "any path" part is the simplest. We create a catch-all route that
accepts the path "path". This is the second rule. The first rule is
aimed at requests for the root of the app, "/". In there, we just
set the path to an empty string and allow it to go down to the
general "path:path" rule.

The "any method" part is a little tricky and more implicit. When
we set up a Rule using Werkzeug's Routing module and we do _not_
provide an "methods" argument, all methods are allowed. For
more details, see

- https://stackoverflow.com/a/16612377/2713733

- werkzeug.routing.Rule docs @
  https://werkzeug.palletsprojects.com/en/0.15.x/routing/#maps-rules-and-adapters
"""
app.url_map.add(Rule("/", endpoint="void", defaults={"path": ""}))
app.url_map.add(Rule("/<path:path>", endpoint="void"))


@app.endpoint("void")
def void(path):
    """
    The void itself.
    You can do any sort of fun stuff here.
    Logging, filtering, etc. Or just the void consume everything.
    """
    return jsonify({"message": "Enter the void!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
