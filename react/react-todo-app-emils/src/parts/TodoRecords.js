import React from 'react'
import TodoItem from './TodoItem'

const styles = {
  ul: {
    listStyle: 'none'
  }
}

function TodoRecords({ todoObjects, completeTrigger, deleteTodo, filteredObjects }) {
// Uzdevumu saraksta struktūras atgriešana
  return (
    <ul style={styles.ul}>
      {filteredObjects.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          completeTrigger={completeTrigger}
          deleteTodo={deleteTodo}
        />
      ))}
    </ul>
  )
}

export default TodoRecords;
