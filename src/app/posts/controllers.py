from app import app

from flask import Blueprint, render_template

from app.posts.forms import PostForm
from  app.posts.models import Post

mod_post = Blueprint('posts',__name__, url_prefix='/posts')

@mod_post.route('/')
def post_index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts = posts)