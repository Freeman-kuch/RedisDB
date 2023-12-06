from flask import Flask
from flask_caching import Cache
import config


app = Flask(__name__)
app.config.from_object(config.Config)
cache = Cache(app)


@app.route("/")
@cache.cached(timeout=20)
def index(foo: str = None):
    if not foo:
        foo = cache.set("foo", "foo")
    return f"just to remember {foo} how this is done"


@app.route("/")
@cache.memoize(timeout=20)
def home(foo: str = None):
    if not foo:
        foo = cache.set("foo", "foo")
    return f"just to remember {foo} how this is "


if __name__ == "__main__":
    app.run(debug=True)
    cache.clear()