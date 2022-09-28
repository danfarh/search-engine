from elasticsearch import Elasticsearch

client = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, "scheme": "https"}])


def create_index(index):
    client.indices.create(index=index, ignore=400)


def insert_data(_index, _id, data):
    res = client.index(index=_index, id=_id, doc_type="_doc", body=data)
    print(res)