import log_vectordb
import embedder
import openai
import os
import numpy as np

openai.api_key = os.environ.get('OPENAI_API_KEY')

class QueryEngine:
    def __init__(self, db, k=10):
        self.db = db
        self.embedder = embedder.Embedder()
        self.k = k

    # @brief Queries the database for logs that match the given text according to node or timestamp
    # @input Question to query by
    # @input Node id (optional). If set to "all", will query all nodes
    # @input Timestamp (optional)
    def query(self, text, node="", timestamp=""):
        list_of_log_data = self.__populate_relevant_logs(node, timestamp)

        # Get embeddings for the query text and logs
        query_embedding = self.embedder.embed(text)
        logs_embeddings = [log.embedding for log in list_of_log_data]

        top_matches_logs = self.__get_top_k_logs(logs_embeddings, query_embedding, list_of_log_data, self.k)

        user_prompt = "Query: " + text + "\nLogs: \n" + "\n".join(top_matches_logs)
        print(user_prompt)
        print("length of prompt: " + str(len(user_prompt)))
        # return "check the above bri"
        response = self.__chat_with_gpt3(user_prompt)
        return response, top_matches_logs


    def __chat_with_gpt3(self, prompt):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a log query engine. You are given a query and a list of logs. You must return an answer to the query."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.6,
            n=1,
            stop=None,
            timeout=15,
        )

        if response.choices:
            print(response)
            return response["choices"][0].message.content
        else:
            return ''

    def __get_top_k_logs(self, logs_embeddings, query_embedding, list_of_log_data, k):
        # Compare the query embedding to each log embedding. Return the top-k matches.
        top_matches = []
        for index, log_embedding in enumerate(logs_embeddings):
            similarity = self.__cosine_similarity(query_embedding, log_embedding)
            if (len(top_matches) < k):
                top_matches.append((index, similarity, log_embedding))
            else:
                # Add the new similarity to the list of top matches if it is greater than the smallest similarity in the list
                min_similarity = min(top_matches, key=lambda x: x[1])
                if (similarity > min_similarity[1]):
                    top_matches.remove(min_similarity)
                    top_matches.append((index, similarity, log_embedding))

        # Return the top-k matches as a list of log text in order of timestamp
        top_matches_logs = []
        for match in sorted(top_matches, key=lambda x: list_of_log_data[x[0]].timestamp):
            top_matches_logs.append(list_of_log_data[match[0]].text)
            
        return top_matches_logs


    def __cosine_similarity(self, query_embedding, log_embedding):
        return np.dot(query_embedding, log_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(log_embedding))


    def __populate_relevant_logs(self, node="", timestamp=""):
        list_of_log_data = []
        if (node != ""):
            # Filter based on node questions
            if (node == "all"):
                # Get all logs
                for key in self.db.get_keys("node"):
                    node_logs = self.db.get_by(key, "node")
                    list_of_log_data.extend(node_logs)
                
            else:
                list_of_log_data.extend(self.db.get_by(node, "node"))
        if (timestamp != ""):
            # Filter based on timestamp questions. Get any logs before and including timestamp
            ts_keys = self.db.get_keys("timestamp")
            for key in ts_keys:
                if key <= timestamp:
                    list_of_log_data.extend(self.db.get_by(timestamp, "timestamp"))

        return list_of_log_data
