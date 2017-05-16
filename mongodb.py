from flask import Flask, render_template, redirect, request
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from flask_bootstrap import Bootstrap
from wtforms import validators

app = Flask(__name__)

db = MongoEngine()
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 20510
}
app.config['SECRET_KEY'] = 'harldajfsl;dj'
bootstrap = Bootstrap()

db.init_app(app)
bootstrap.init_app(app)

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

class Content(db.EmbeddedDocument):
    text = db.StringField()
    lang = db.StringField(max_length=3)

class Post(db.Document):
    title = db.StringField(max_length=120, required=True, validators=[
        validators.InputRequired(message='Missing title.'),])
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=30))
    comments = db.EmbeddedDocumentField(Content)

PostForm = model_form(Post)

@app.route('/')
def add_post():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        redirect('done')
    return render_template('add_post.html', form=form)

if __name__ == '__main__':
    app.run()