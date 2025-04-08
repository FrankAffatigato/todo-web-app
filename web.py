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


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo:", placeholder="Schedule appointment",
              on_change=add_todo, key='new_todo')

# print("hello")
# st.session_state
