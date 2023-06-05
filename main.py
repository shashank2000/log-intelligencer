import log_vectordb
import log_ingestor
import query_engine
import os
import time
import pickle

def ingest_data():
    if os.path.exists("db.pickle"):
        with open("db.pickle", "rb") as f:
            return pickle.load(f)
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

    # make a pickle file
    with open("db.pickle", "wb") as f:
        pickle.dump(db, f)

    return db