import datetime
import dateutil.tz


from flask import Blueprint, render_template


from . import model


bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(1, "mary@example.com", "@hubert")
    posts = [
        model.Post(
            1, user, "I be out here in this class fr lol :>", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            3, user, "Yet another post", datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(1, "mary@example.com", "@hubert")
    posts = [
        model.Post(
            1, user, "I be out here in this class fr lol :>", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/user_template.html", user=user, posts=posts)

@bp.route("/post")
def post():
    user = model.User(1, "mary@example.com", "@hubert")
    post = model.Post(1, user, "I be out here in this class fr lol :>", datetime.datetime.now(dateutil.tz.tzlocal()))
    replies = [
        model.Post(
            2, user, "Way to go Hubert!", datetime.datetime.now(dateutil.tz.tzlocal())
        ), 
        model.Post(
            3, user, "Thanks for sharing!", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            4, user, "So wholesome!", datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("post_view_template.html", user=user, post=post, posts=replies)