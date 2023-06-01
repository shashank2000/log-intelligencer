import log_vectordb
import log_ingestor
import query_engine
import os
import time


def ingest_data():
    print(time.time())
    a = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_0"))
    print(time.time())
    b = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_1"))
    print(time.time())
    c = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_2"))

    print("here")
    db = log_vectordb.LogVectorDB()
    for a in [a, b, c]:
        for log in a.logs:
            db.append(log)

    return db

db = ingest_data()
qe = query_engine.QueryEngine(db)
print(qe.query("What servers were created?", "all", ""))
        



