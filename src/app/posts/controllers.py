from app import app

from flask import Blueprint, render_template, jsonify

from app.posts.forms import PostForm
from  app.posts.models import Post

mod_post = Blueprint('posts',__name__)

@mod_post.route('/')
def post_index():
    posts = Post.query.all()
    return jsonify(json_list=[p.serialize for p in posts])
@mod_post.route('/<int:id>', methods=['GET'])
def post_show(id):
    post = Post.query.get(id)
    return jsonify(post.serialize)