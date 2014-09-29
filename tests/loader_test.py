import json
from cliche.services.wikipedia import loader as dbpedia
from cliche.services.wikipedia.workauthor import WorkAuthor


def test_loader(monkeypatch, fx_session, fx_celery_app):
    class FakeQuery(object):
        def convert(self):
            return {"results": {"bindings": [{"callret-0": {"value": "150"}}]}}

    monkeypatch.setattr("SPARQLWrapper.SPARQLWrapper.query", FakeQuery)

    relation_num = dbpedia.count_by_relation(
        p=[
            'dbpprop:author',
            'dbpedia-owl:writer',
            'dbpedia-owl:author'
        ]
    )

    class FakeQuery(object):
        offset = 0

        def convert(self):
            with open('tests/select_relation.json') as fp:
                offset = FakeQuery.offset
                fakeResult = (json.load(fp))[offset:offset+100:]
                FakeQuery.offset += 100
                return {"results": {"bindings": fakeResult}}

    monkeypatch.setattr("SPARQLWrapper.SPARQLWrapper.query", FakeQuery)
    dbpedia.load_page(1, relation_num)
    num = fx_session.query(WorkAuthor).count()
    assert num == 100
