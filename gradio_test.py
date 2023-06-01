import gradio as gr
from main import ingest_data
import query_engine

queries = []

# first ingest and store the logs 
db = ingest_data()
qe = query_engine.QueryEngine(db)

# TODO: cache the embeddings 

def make_query(query):
    queries.append(query)
    resp = qe.query(query, "all", "")
    return resp, ["matched logs"], queries[-4:]

demo = gr.Interface(
    fn=make_query, 
    inputs=gr.Textbox(label="Query"), 
    outputs=[gr.Textbox(label="Actual response"), gr.JSON(label="Matched logs"), gr.JSON(label="Previous queries")],
    title="LogIntelligencer"
)
demo.launch()