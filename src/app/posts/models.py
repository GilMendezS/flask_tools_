from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=False)
    date_created = db.Column(db.DateTime,default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
    def __repr__():
        return "<Post {}>".format(self.title)
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'     : self.id,
           'title'  : self.title,
           # This is an example how to deal with Many2Many relations
           'description'  : self.description
       }