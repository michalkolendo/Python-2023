# Przy pierwszym uruchomieniu:  flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app app
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class NoteTag(db.Model):
    __tablename__ = 'notetag'
    id = db.Column('id', db.Integer, primary_key=True)
    tag_id = db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
    note_id = db.Column('note_id', db.Integer, db.ForeignKey('note.id'))


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<tag %r>' % self.tagname


class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.String(80), nullable=False)
    tags = db.relationship("Tag",
                           secondary='notetag',
                           uselist=True,
                           backref='notes',
                           lazy='select')

    def __repr__(self):
        return '<note %r>' % self.title


def get_tags(session):
    return session.query(Tag).all()


def get_notes(session):
    return session.query(Note).all()


def create_tag(tagname, session):
    try:
        tag = Tag(tagname=tagname)
        session.add(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True


def remove_tag(tagid, session):
    try:

        tag = session.query(Tag).filter_by(id=tagid).one()
        session.delete(tag)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True


def create_note(title, note, session):
    try:
        note = Note(body=note, title=title)
        session.add(note)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True


def remove_note(noteid, session):
    try:

        note = session.query(Note).filter_by(id=noteid).one()
        session.delete(note)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True


@app.route('/')
def hello():
    return render_template('form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           tytul="Notatki", no_error=True)


@app.route('/addtag')
def addtag():
    args = request.args
    create_tag(args["tag"], db.session)

    return render_template('form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           tytul="Dodano notatke")


@app.route('/removetag')
def removetag():
    args = request.args
    remove_tag(args["tag"], db.session)
    return render_template('form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           tytul="Usunieto notatke")


@app.route('/addnote')
def addnote():
    args = request.args
    create_note(title=args["title"], note=args["note"], session=db.session)

    return render_template('form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           tytul="Dodano notatke")


@app.route('/removenote')
def removenote():
    args = request.args
    remove_note(args["note"], db.session)
    return render_template('form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           tytul="Usunieto notatke")


@app.route('/join')
def join():
    args = request.args
    jointables(args['noteID'], args['tagID'], db.session)
    return render_template('form.html', data=get_tags(db.session), notes=get_notes(db.session),
                           tytul="Usunieto notatke")


def jointables(noteid, tagid, session):
    note = session.query(Note).filter_by(id=noteid).one()
    tag = session.query(Tag).filter_by(id=tagid).one()
    note.tags.append(tag)
    session.add(note)
    session.commit()
