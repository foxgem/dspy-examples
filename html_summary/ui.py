import gradio as gr
from summary import summarize


ui = gr.Interface(
    fn=summarize,
    inputs=["text"],
    outputs=["text"],
)

ui.launch()
