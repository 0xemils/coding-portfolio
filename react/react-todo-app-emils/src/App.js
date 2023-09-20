import React, { useEffect, useState } from 'react';
import TodoForm from './parts/TodoForm';
import TodoRecords from './parts/TodoRecords';

const LOCAL_STORAGE_KEY = 'react-todo-list-todoObjects';

function App() {
  const [todoObjects, setTodoObjects] = useState([]);
  const [filter, setFilter] = useState('all');
  const [filteredObjects, setFilteredObjects] = useState([]);


  useEffect(() => {
    const storageTodoObjects = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));
    if (storageTodoObjects) {
      setTodoObjects(storageTodoObjects);
    }
  }, []);

  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(todoObjects));
  }, [todoObjects]);

  useEffect(() => {
    const filterHandler = () => {
      switch (filter) {
        case 'completed':
          setFilteredObjects(todoObjects.filter(todo => todo.completed === true))
          break;
        case 'uncompleted':
          setFilteredObjects(todoObjects.filter(todo => todo.completed === false))
          break;
        default:
          setFilteredObjects(todoObjects);
          break;
      }
    };
    filterHandler();
  }, [todoObjects, filter]);

  function completeTrigger(id) {
    setTodoObjects(
      todoObjects.map( todo => {
        if (todo.id === id) {
          return {
            ...todo,
            completed: !todo.completed
          };
        }
        return todo;
      })
    );
  }

  function addTodo(todo) {
    // Add new object to the TODO list
    setTodoObjects([todo, ...todoObjects]);
  }

  // Delete object from the TODO list
  function deleteTodo(id) {
    setTodoObjects(todoObjects.filter(todo => todo.id !== id));
  }

  // Returning the structure of the app
  return (
    <div className="todoContainer">
      <header className="App-header">
        <h1 className='titleStyle'>TO DO List</h1>
        <TodoForm
          addTodo={addTodo}
          setFilter={setFilter}
        />
        <TodoRecords
          todoObjects={todoObjects}
          completeTrigger={completeTrigger}
          deleteTodo={deleteTodo}
          filteredObjects={filteredObjects}
        />
      </header>
    </div>
  );
}

export default App;
