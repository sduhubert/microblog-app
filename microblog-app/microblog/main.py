import datetime
import dateutil.tz


from flask import Blueprint, render_template, request, redirect, url_for, abort
import flask_login


from . import model, db


bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    user = model.User(email="mary@example.com", name="hubert")
    query = db.select(model.Post).order_by(model.Post.timestamp.desc()).limit(10)
    posts = db.session.execute(query).scalars().all()
    return render_template("main/index.html", posts=posts)

@bp.route("/profile/<int:user_id>")
@flask_login.login_required
def profile(user_id):
    user = db.get_or_404(model.User, user_id)
    query = db.select(model.Post).filter_by(user=user).order_by(model.Post.timestamp.desc())
    posts = db.session.execute(query).scalars().all()
    return render_template("main/user_template.html", user=user, posts=posts)

@bp.route("/post", methods=["POST"])
@flask_login.login_required
def new_post():
    user = flask_login.current_user
    text = request.form.get("text")
    new_post = model.Post(user=user, text=text, timestamp=datetime.datetime.now(dateutil.tz.tzlocal()))
    
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(url_for("main.post", post_id=new_post.id))

@bp.route("/post/<int:post_id>")
@flask_login.login_required
def post(post_id):
    post = db.get_or_404(model.Post, post_id)
    return render_template("main/post.html", post=post)