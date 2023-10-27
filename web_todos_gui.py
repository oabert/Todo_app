import streamlit as st

from functions import get_read_todos, write_todos

todos_list = get_read_todos()


def add_todo():
    todo_input = st.session_state['new_todo'] + '\n'
    # """Updated todo list with .append"""
    todos_list.append(todo_input)
    # """write/add new todo to the list/update todos_list.txt"""
    write_todos(todos_list)
    st.session_state['new_todo'] = ''


""""""

st.title('My todo app')
st.subheader('This is my todolist project')
st.write('This app will increase your productivity')

for index, todo_item in enumerate(todos_list):
    checkbox = st.checkbox(todo_item, key=todo_item)
    if checkbox:
        todos_list.pop(index)
        write_todos(todos_list)
        del st.session_state[todo_item]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add your todo...',
              on_change=add_todo, key='new_todo')

# print('Hello')
