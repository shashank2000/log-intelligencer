import gradio as gr

queries = []

def make_query(query):
    queries.append(query)
    return "Actual query response", ["matched logs"], queries[-4:]

demo = gr.Interface(
    fn=make_query, 
    inputs=gr.Textbox(label="Query"), 
    outputs=[gr.Textbox(label="Actual response"), gr.JSON(label="Matched logs"), gr.JSON(label="Previous queries")],
    title="SearchSmart^TM",
    css=".gradio-container {background: url('file=headscratcher.png')}"
)
demo.launch()