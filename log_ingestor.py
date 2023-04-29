# LogIngestor class
# @brief: This class is responsible for ingesting the log file of a single node
# and storing the representation in VectorDB

import re
import os

class LogIngestor:
    def __init__(self, filepath):
        self.logs = []

        try:
            print(filepath)
            with open(filepath, "r") as f:
                for line in f:
                    node_name = self.filename_to_nodename(filepath)
                    line_tuple = self.parse_line(line, node_name)
                    self.logs.append(line_tuple)
        except:
            print("Error: File " + filepath + " had an error while being processed.")
            return
        
    # @brief Parses line into a tuple
    # @input Line formatted as timestamp:log text
    # @input Node name ("Node 1", "Node 2", etc")
    # @return A tuple that contains (timestamp, node id, log text)
    def parse_line(self, input, node_name):
        arr_ts_log = input.split(":") # array of timestamp and log
        timestamp = arr_ts_log[0]
        log_text = arr_ts_log[1]
        return (timestamp, node_name, log_text)
        
    # @brief Converts a filename to a node name
    def filename_to_nodename(self, filename):
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