import log_vectordb

class QueryEngine:
    def __init__(self):
        self.db = log_vectordb.LogVectorDB()
    
    # @brief Queries the database for logs that match the given text according to node or timestamp
    def query(text, node=-1, timestamp=-1):
        list_of_log_data = []
        if (node > 0):
            # Filter based on node questions
            list_of_log_data.append(db.get_by(node, "node"))
        if (timestamp > 0):
            # Filter based on timestamp questions
            # TODO: what about timestamp + node questions?
            list_of_log_data.append(db.get_by(timestamp, "timestamp"))
    
        
    