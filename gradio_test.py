import gradio as gr

queries = []

# first ingest and store the logs 

def make_query(query):
    queries.append(query)
    return "Actual query response", ["matched logs"], queries[-4:]

demo = gr.Interface(
    fn=make_query, 
    inputs=gr.Textbox(label="Query"), 
    outputs=[gr.Textbox(label="Actual response"), gr.JSON(label="Matched logs"), gr.JSON(label="Previous queries")],
    title="LogIntelligencer"
)
demo.launch()