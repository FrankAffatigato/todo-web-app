import streamlit as st
import functions as f

todos = f.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)
    print(todo)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is built to increase your productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Schedule appointment",
              on_change=add_todo, key='new_todo')

print("hello")