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


class Judge(db.Model):
    __tablename__ = 'judgedba'
    id = db.Column(db.BIGINT, primary_key=True)
    question = db.Column(db.VARCHAR(500))
    rightanswer = db.Column(db.VARCHAR(2))


class Subject(db.Model):
    __tablename__ = 'subdba'
    id = db.Column(db.BIGINT, primary_key=True)
    question = db.Column(db.VARCHAR(500))
    refanswer = db.Column(db.VARCHAR(500))


class Paper(db.Model):
    __tablename__ = 'paper'
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.VARCHAR(20))
    begintime = db.Column(db.DATETIME)
    finishtime = db.Column(db.DATETIME)
    choi = db.Column(db.VARCHAR(100))
    judg = db.Column(db.VARCHAR(100))
    sub = db.Column(db.VARCHAR(100))
    choiscore = db.Column(db.VARCHAR(100))
    judgscore = db.Column(db.VARCHAR(100))
    subscore = db.Column(db.VARCHAR(100))
    tid = db.Column(db.BIGINT)
    classid = db.Column(db.VARCHAR(100))

    def __init__(self, name, begintime, finishtime, choi, judg, sub, choiscore, judgscore,
                 subscore, tid, classid):
        self.name = name
        self.begintime = begintime
        self.finishtime = finishtime
        self.choi = choi
        self.judg = judg
        self.sub = sub
        self.choiscore = choiscore
        self.judgscore = judgscore
        self.subscore = subscore
        self.tid = tid
        self.classid = classid
