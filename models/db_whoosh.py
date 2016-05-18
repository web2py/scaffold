class Whoosh(object):
    def __init__(self):
        import os
        from whoosh.fields import Schema, TEXT, STORED
        from whoosh.index import create_in, open_dir
        from whoosh.query import *
        self.index = os.path.join(request.folder,'whoosh')
        if not os.path.exists(self.index):
            os.mkdir(self.index)
            self.schema = Schema(id=STORED, text=TEXT(stored=True))
            self.ix = create_in(self.index, self.schema)
        else:
            self.ix = open_dir(self.index)
    def learn(self, samples):
        writer = self.ix.writer()
        for i,text in samples:
            writer.add_document(id=i,text=text.lower())
        writer.commit()
    def search(self, text, page=1, pagelen=100):
        from whoosh.qparser import QueryParser
        text = text.lower()
        with self.ix.searcher() as searcher:
            query = QueryParser("text", self.ix.schema).parse(text)
            results = searcher.search_page(query, page, pagelen)
            return [r['id'] for r in results]
