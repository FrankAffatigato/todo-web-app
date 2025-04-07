import functions as f

todos = f.get_todos()

for todo in todos:
    st.checkbox(todo)