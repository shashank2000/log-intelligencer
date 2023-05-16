# ingestor and vectordb tests

from unittest import TestCase
import os
import log_vectordb
import log_ingestor

class TestIngestorAndStore(TestCase):
    def test_log_ingest_and_store(self):
        a = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_0"))
        self.assertEqual(len(a.logs), 181)
        
        b = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_1"))
        self.assertEqual(len(b.logs), 662)
        
        c = log_ingestor.LogIngestor(os.path.join(os.getcwd() + "/log_examples", "node_2"))
        self.assertEqual(len(c.logs), 504)
             
        db = log_vectordb.LogVectorDB()
        for a in [a, b, c]:
            for log in a.logs:
                db.append(log)
        
        self.assertEqual(len(db.get_keys("node")), 3)   
        
        total_timestamp_values = 0
        for key in db.get_keys("timestamp"):
            total_timestamp_values += len(db.get_by(key, "timestamp"))
        self.assertEqual(total_timestamp_values, 181+662+504)

        self.assertEqual(db.get_by("1", "node")[0].text, "Creating server with id 1")
        self.assertEqual(db.get_by("467694:43:13::6", "timestamp")[0].text, "Creating server with id 1")
        
c = TestIngestorAndStore()
c.test_log_ingest_and_store()
