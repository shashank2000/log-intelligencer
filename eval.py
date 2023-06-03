import query_engine
from main import ingest_data

queries = [
    "who is the leader",
    "what servers were initialized",
]

print("initializing vector database")
db = ingest_data()

for k in [5, 10, 20, 50, 100]:
    breakpoint()
    print("k = " + str(k))
    qe = query_engine.QueryEngine(db, k=k)

    for query in queries:
        response, matched_logs = qe.query(text=query, node="all", timestamp="")
        print(query)
        print(response)
        print(matched_logs)


# with k = 5
# didn't do very well on "what servers were initialized"
# did well on "who is the leader"

# with k = 10

