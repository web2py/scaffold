if db(db.doc).isempty():
    from gluon.contrib.populate import populate
    populate(db.doc, 1000)
    db.commit()
    sample = [(row.id, unicode(row.body)) for row in db(db.doc).select()]
    Whoosh().learn(sample)
