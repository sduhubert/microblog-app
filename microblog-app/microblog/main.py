import datetime
import dateutil.tz


from flask import Blueprint, render_template
import flask_login


from . import model


bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    user = model.User(email="mary@example.com", name="hubert")
    posts = [
        model.Post(
            user=user, text="I be out here in this class fr lol :>", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            user=user, text="Yet another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
@flask_login.login_required
def profile():
    user = model.User(email="mary@example.com", name="hubert")
    posts = [
        model.Post(
            user=user, text="I be out here in this class fr lol :>", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            user=user, text="Yet another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/user_template.html", user=user, posts=posts)

@bp.route("/post")
@flask_login.login_required
def post():
    user = model.User(email="mary@example.com", name="hubert")
    post = model.Post(user, "I be out here in this class fr lol :>", datetime.datetime.now(dateutil.tz.tzlocal()))
    replies = [
        model.Post(
            user=user, text="Way to go Hubert!", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ), 
        model.Post(
            user=user, text="Thanks for sharing!", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
           user=user, text="So wholesome!", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("post_view_template.html", user=user, post=post, posts=replies)