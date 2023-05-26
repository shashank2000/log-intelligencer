# LogVectorDB class
# @brief: This class is responsible for storing the log data in an easy-to-query
# format
import log_data 
import redis

class LogVectorDB:
    def __init__(self, use_redis=False):
        self.ts_to_data = {}
        self.node_to_data = {} # Append only, sorted automatically due to how we ingest data
        self.redisdb = redis.Redis(host='localhost', port=6379, db=0) if use_redis else None

    # @brief Appends data to the database according to both timestamp and node name
    # @input Data object can contain timestamp, node, and log text
    # @return None
    def append(self, data):
        # Add to ts_to_data
        if data.timestamp and data.timestamp in self.ts_to_data:
            self.ts_to_data[data.timestamp].append(data)
        else:
            self.ts_to_data[data.timestamp] = [data]
        
        # Add to node_to_data
        if data.node and data.node in self.node_to_data:
            self.node_to_data[data.node].append(data)
        else:
            self.node_to_data[data.node] = [data]
            
    # @brief Gets data from the database according to either timestamp or node
    # @input Key to query by (timestamp or node name)
    # @input Type of key ("timestamp" or "node")
    # @return List of Data objects
    def get_by(self, key, type):
        if self.redisdb:
            return self.redisdb.get(key) 
        
        if type == "timestamp":
            return self.ts_to_data[key]
        elif type == "node":
            return self.node_to_data[key]
        else:
            return None
        
    # @brief Gets all keys from the database according to either timestamp or node
    # @input Type of key ("timestamp" or "node")
    # @return List of keys
    def get_keys(self, type):
        if type == "timestamp":
            return self.ts_to_data.keys()
        elif type == "node":
            return self.node_to_data.keys()
        else:
            return None