import pinecone

pinecone.init(api_key="75167d0a-082b-4ad3-931f-57aba2864c26",
              environment="us-west1-gcp")

# use existing index 

index = pinecone.Index("log_index")

# ingest data
# loop through log_example.txt
# each line is a json object
# ingest each line as a json object

with open("log_example.txt", "r") as f:
    for line in f:
        # convert to 1000d vector
        # use simple embedding model locally
        embedding = pinecone.Embedding("simple_embedding")
        index.ingest(embedding, line)

