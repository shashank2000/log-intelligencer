# LogIngestor class
# @brief: This class is responsible for ingesting the log file of a single node
# and storing the representation in VectorDB

import re
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
                    if obj is not None:
                        self.logs.append(obj)    
        except:
            print("Error: File " + filepath + " had an error while being processed.")
            return
        
    # @brief Parses line into a Data object
    # @input Line formatted as timestamp:log text
    # @input Node name ("Node 1", "Node 2", etc")
    # @input Delimiter (default is "]")
    # @return A Data object that contains (timestamp, node id, log text).
    #         Returns None if the line is not formatted correctly
    def __parse_line(self, input, node_name, delimiter="] "):
        if input[0] == "[":
            arr_ts_log = input.split(delimiter) # array of timestamp and log
            timestamp = arr_ts_log[0]
            
            # Remove [[ or [ from start of timestamp
            if timestamp[0] == "[":
                timestamp = timestamp[1:]
                if timestamp[0] == "[": # Race condition in logs?
                    timestamp = timestamp[1:]
                                
            # Strip out newlines in log_text
            log_text = arr_ts_log[1]
            log_text = log_text.replace("\n", "")
            
            data = log_data.Data(timestamp, node_name, log_text)
            return data
        return None #TODO: problem. Logs go on multiple lines ): This ignores any part on other lines
            
    # @brief Converts a filename to a node name
    # @input Filename of the log file. Assumes the filename contains
    #        "NodeX.txt" where X is the node number
    def __filename_to_nodename(self, filename):
        # Use regular expressions to find the node number in the filename
        match = re.search(r'node_(\d+)', filename) #TODO: depends on filename format
        if match:
            node_number = match.group(1)
            # Convert the node number to the desired format
            node_name = "Node " + node_number
            return node_name
        else:
            # if the filename doesn't match the expected format, return None
            return None
            