from .. import db


class Page:
    page_number = 7


class Choice(db.Model):
    __tablename__ = 'choicedba'
    id = db.Column(db.BIGINT, primary_key=True)
    question = db.Column(db.VARCHAR(500))
    option1 = db.Column(db.VARCHAR(300))
    option2 = db.Column(db.VARCHAR(300))
    option3 = db.Column(db.VARCHAR(300))
    option4 = db.Column(db.VARCHAR(300))
    rightanswer = db.Column(db.VARCHAR(10))


qtable_dict = {'choice': Choice}
