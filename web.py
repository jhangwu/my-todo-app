# Day 20 - Web app building
import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    user_input = st.session_state["new_todo"] + "\n"
    todos.append(user_input)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my TodoApp")
st.write("This app is to increase your productivity and time management!")
text_input = st.text_input(label="Please enter a new todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()






