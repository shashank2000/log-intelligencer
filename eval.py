import query_engine
from main import ingest_data
import json 

queries = [
    "who is the leader",
    "what servers were initialized",
]

print("initializing vector database")
db = ingest_data()

from collections import defaultdict
results = defaultdict(dict)

# 5, 10, 20, 50, 100
for k in [5, 10, 20, 50, 100]:
    print("k = " + str(k))
    qe = query_engine.QueryEngine(db, k=k)

    for query in queries:
        response, matched_logs = qe.query(text=query, node="all", timestamp="")
        print(query)
        print(response)
        print(matched_logs)
        results[query][k] = [response, matched_logs]


# write results to file
with open("results.json", "w") as f:
    print("writing results to file", results)
    json.dump(results, f)

# TODO: make a table of results, plot of accuracy 

# with k = 1




# with k = 5
# didn't do very well on "what servers were initialized" because not enough logs retrieved
# did well on "who is the leader"n

# with k = 10

