import query_engine
from main import ingest_data
import json 
import time
import matplotlib.pyplot as plt


# TODO: better embedder test
# TODO: some type of graph


queries = [
    "who is the leader",
    "what servers were initialized",
    "who are the current followers",
    "what server has crashed",
    "describe the last election"
]

print("initializing vector database")
db = ingest_data()

from collections import defaultdict
results = defaultdict(dict)

# 5, 10, 20, 50, 100
latencies = []
for k in [5, 10, 20, 50, 100]:
    print("k = " + str(k))
    qe = query_engine.QueryEngine(db, k=k)
    
    start_time = time.time()

    for query in queries:
        response, matched_logs, cost = qe.query(text=query, node="all", timestamp="")
        print(query)
        print(response)
        print(matched_logs)
        print("$" + str(cost))
        results[query][k] = {"response": response, "matched_logs": matched_logs, "cost": cost}
        
    end_time = time.time()
    elapsed_time = end_time - start_time
    average_latency = elapsed_time / len(queries) 
    latencies.append(average_latency)

# write results to file
with open("results_3.json", "w") as f:
    print("writing results to file", results)
    json.dump(results, f)

# TODO: make a table of results, plot of accuracy 

plt.plot([5, 10, 20, 50, 100], latencies, marker='o')
plt.xlabel('k')
plt.ylabel('Average Latency')
plt.title('Average Latency vs. k')
plt.grid(True)

# Save the plot as an image file
plt.savefig('latency_plot.png')

# with k = 1




# with k = 5
# didn't do very well on "what servers were initialized" because not enough logs retrieved
# did well on "who is the leader"n

# with k = 10

