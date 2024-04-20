from core import db
from core.apis.decorators import AuthPrincipal
from core.libs import assertions, helpers
from core.models.users import User


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Teacher %r>' % self.id

    # @classmethod
    # def filter(cls, *criterion):
    #     db_query = db.session.query(cls)
    #     return db_query.filter(*criterion)

    @classmethod
    def list_teachers(cls):
        return db.session.query(User).filter(User.id == cls.user_id).all()
