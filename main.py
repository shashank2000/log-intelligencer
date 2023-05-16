import log_vectordb
import log_ingestor
import query_engine
import os

a = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_0"))
b = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_1"))
c = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_2"))
        
db = log_vectordb.LogVectorDB()
for a in [a, b, c]:
    for log in a.logs:
        db.append(log)
        
qe = query_engine.QueryEngine(db)
print(qe.query("What servers were created?", "all", ""))
        



