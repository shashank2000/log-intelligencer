import log_vectordb
import log_ingestor
import query_engine
import os
import time


def ingest_data():
    print(time.time())
    a = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_127.0.0.1:1025"))
    print(time.time())
    b = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_127.0.0.1:1026"))
    print(time.time())
    c = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_127.0.0.1:1027"))

    print("here")
    db = log_vectordb.LogVectorDB()
    for a in [a, b, c]:
        for log in a.logs:
            db.append(log)

    return db

db = ingest_data()

print("done populating db. going to query")
qe = query_engine.QueryEngine(db, 5)
response, matched_logs, cost = qe.query("Who is the leader?", "all", "")
print(response)
print(matched_logs)
print("$" + str(cost))
