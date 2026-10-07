import streamlit as st


# Page settings make the app look good in a browser tab.
st.set_page_config(
    page_title="Maryam's AI Study Agent",
    page_icon="🤖",
    layout="centered",
)


def agent_think(user_question):
    """Return a helpful answer using simple, offline topic matching.

    This agent does not need an API key. It uses prepared study guidance and
    chooses the most useful response based on words in the user's question.
    """
    question = user_question.lower().strip()

    if not question:
        return "Please ask me a question about Python, pandas, or data analytics."

    if "loop" in question or "for loop" in question or "while" in question:
        return """### Python loops

Python has two common loops:

* A `for` loop repeats once for each item in a sequence.
* A `while` loop repeats while a condition is `True`.

```python
for number in range(1, 4):
    print(number)

count = 1
while count <= 3:
    print(count)
    count += 1
```

Use `break` to stop a loop early and `continue` to skip to the next
iteration. Remember to update the condition in a `while` loop so it does not
run forever."""

    if "pandas" in question or "dataframe" in question:
        return """### Pandas quick guide

Pandas is a Python library for working with tables of data. A
`DataFrame` is like a spreadsheet with rows and columns.

```python
import pandas as pd

data = pd.read_csv("sales.csv")
print(data.head())
print(data.info())
summary = data.groupby("category")["sales"].sum()
```

Useful methods include `head()`, `info()`, `describe()`, `isna()`,
`dropna()`, `fillna()`, `groupby()`, and `sort_values()`. Start by
understanding your columns, checking missing values, and then asking a
business question of the data."""

    if "roadmap" in question or "learn data" in question or "analytics" in question:
        return """### Data analytics roadmap

1. Learn Python basics: variables, conditions, loops, functions, and files.
2. Practice NumPy and pandas for cleaning and transforming data.
3. Learn charts with Matplotlib or Seaborn.
4. Study statistics: averages, spread, correlation, and basic probability.
5. Learn SQL to work with databases.
6. Build projects and explain your findings clearly.
7. Create a portfolio with notebooks, dashboards, and short case studies.

For a three-month project, study one topic each week and finish every week
with a small practical exercise."""

    if "project" in question or "idea" in question:
        return """### Project ideas

Here are beginner-friendly data analytics projects:

* Analyze sales data and find the best-selling products.
* Explore student performance and compare study habits with results.
* Study Pakistan weather data and identify seasonal patterns.
* Build a personal expense tracker with pandas.
* Analyze customer reviews and count common positive or negative words.

Choose a project with a clear question, clean the data, make three to five
visualizations, and finish with simple recommendations."""

    if "maryam" in question or "about you" in question or "about me" in question:
        return """### About Maryam

Maryam Imdad is a Data Analytics learner from Gujranwala, Pakistan. She is
developing skills in Python, C++, and Data Analysis. This three-month project
is her AI Study Agent, created to support her learning and portfolio."""

    return """I can help you study **Python loops**, **pandas**, and the
**data analytics roadmap**. I can also suggest **project ideas** or tell you
**about Maryam**.

Try asking: *"How does a for loop work?"* or *"Give me a pandas project
idea."*"""


# Store the conversation in the session so it remains visible after each input.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I am Maryam's offline AI Study Agent. "
                "Ask me anything about Python, pandas, or data analytics."
            ),
        }
    ]


st.title("Maryam's AI Study Agent")
st.subheader("Python & Data Analytics Assistant")
st.write(
    "A simple, offline study companion for learning Python and building "
    "data analytics skills."
)


with st.sidebar:
    st.header("About Maryam")
    st.write("**Name:** Maryam Imdad")
    st.write("**From:** Gujranwala, Pakistan")
    st.write("**Email:** maryamimdadali@gmail.com")
    st.write("**Field:** Data Analytics")
    st.write("**Skills:** Python, C++, Data Analysis")
    st.write("**LinkedIn:** [in/maryam-imdad](https://www.linkedin.com/in/maryam-imdad)")
    st.divider()
    st.caption("This agent works automatically without an API key.")


# Display all previous messages in the chat window.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_question = st.chat_input("Ask a question about Python or data analytics...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    answer = agent_think(user_question)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)


st.divider()
st.caption("Developed by Maryam Imdad")