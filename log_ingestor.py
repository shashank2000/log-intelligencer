# LogIngestor class
# @brief: This class is responsible for ingesting the log file of a single node
# and storing the representation in VectorDB

import re
import os
import log_vectordb
import log_data 

class LogIngestor:
    def __init__(self, filepath):
        self.logs = []

        try:
            print(filepath)
            with open(filepath, "r") as f:
                for line in f:
                    node_name = self.__filename_to_nodename(filepath)
                    obj = self.__parse_line(line, node_name)
                    self.logs.append(obj)
        except:
            print("Error: File " + filepath + " had an error while being processed.")
            return
        
    # @brief Parses line into a Data object
    # @input Line formatted as timestamp:log text
    # @input Node name ("Node 1", "Node 2", etc")
    # @return A Data object that contains (timestamp, node id, log text)
    def __parse_line(self, input, node_name):
        arr_ts_log = input.split(":") # array of timestamp and log
        data = log_data.Data(arr_ts_log[0], node_name, arr_ts_log[1])
        return data
        
    # @brief Converts a filename to a node name
    # @input Filename of the log file. Assumes the filename contains
    #        "NodeX.txt" where X is the node number
    def __filename_to_nodename(self, filename):
        # Use regular expressions to find the node number in the filename
        match = re.search(r'Node(\d+)', filename) #TODO: depends on filename format
        if match:
            node_number = match.group(1)
            # Convert the node number to the desired format
            node_name = "Node " + node_number
            return node_name
        else:
            # if the filename doesn't match the expected format, return None
            return None
            

# run the script
a = LogIngestor(os.path.join(os.getcwd(), "Node1.txt"))
print(a.logs)

db = log_vectordb.LogVectorDB()
db.append(a.logs[0])
print(db.get_keys("node"))
print(db.get_keys("timestamp"))

print(db.get_by("Node 1", "node")[0].text)
print(db.get_by("1857890", "timestamp")[0].text)