import React from 'react';

function TodoItem({ todo, completeTrigger, deleteTodo }) {
  function checkboxMarked() {
    completeTrigger(todo.id);
  }

  function triggerDeleteAction() {
    deleteTodo(todo.id);
  }

// Uzdevumu struktūras atgriešana
  return (
    <div style={{ display: 'flex', opacity: todo.completed ? 0.5 : 1 }} className='todoItem'>
      <button onClick={checkboxMarked} className='itemButton'>✓</button>
      <button onClick={triggerDeleteAction} className='itemButton'>⌦</button>
      <li
        style={{
          color: todo.completed ? 'grey' : 'white',
          textDecoration: todo.completed ? 'line-through' : null
        }}
      >
        {todo.task}
      </li>
    </div>
  );
}

export default TodoItem;
