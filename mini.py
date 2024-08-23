from dotenv import load_dotenv
import dspy

load_dotenv()

# Set up the LM.
turbo = dspy.OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=250)
dspy.configure(lm=turbo)

qa = dspy.ChainOfThought("question -> answer")
response = qa(question="What is the capital of France?")

print(response.answer)
