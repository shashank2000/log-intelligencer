# Log Intelligence tool

## Setup
Create a new virtual environment, then run `pip3 install -r requirements.txt`

## Organization

System design: there is an embedder, log ingestion engine, vector DB and a query engine. 

Log ingestion engine can either read from files or from a stream. 

We need a UI as well ideally, that'll make it a nice full-featured product. 


To run the sample queries, run `python3 gradio_test.py`

Lastly, we have tests. To run the test suite, run `pytest`. 
