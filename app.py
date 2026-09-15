from datetime import datetime, timezone

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///social_feed.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)


@app.route("/create", methods=["POST"])
def create_post():
    username = request.form.get("username", "").strip()
    content = request.form.get("content", "").strip()

    if not username or not content:
        flash("Please enter both your name and a post.", "error")
        return redirect(url_for("index"))

    if len(username) > 50:
        flash("Name must be 50 characters or less.", "error")
        return redirect(url_for("index"))

    if len(content) > 500:
        flash("Posts must be 500 characters or less.", "error")
        return redirect(url_for("index"))

    db.session.add(Post(username=username, content=content))
    db.session.commit()

    flash("Your post was published successfully.", "success")
    return redirect(url_for("index"))


@app.route("/like/<int:post_id>", methods=["POST"])
def like_post(post_id):
    post = db.get_or_404(Post, post_id)
    post.likes += 1
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()

    flash("Post deleted.", "success")
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(_error):
    return render_template(
        "error.html",
        title="Page not found",
        message="The page you requested could not be found.",
    ), 404


if __name__ == "__main__":
    app.run(debug=True)
