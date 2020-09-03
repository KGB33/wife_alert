from flask import current_app, render_template

from . import ASYNC_LOOP
from .forms import ButtonForm
from . import gpio


@current_app.route("/", methods=["GET", "POST"])
def index():
    """
    Display a big red button to make the light flash
    """
    form = ButtonForm()
    if form.validate_on_submit():
        ASYNC_LOOP.run_until_complete(gpio.make_blink())
    return render_template("index.html", form=form)
