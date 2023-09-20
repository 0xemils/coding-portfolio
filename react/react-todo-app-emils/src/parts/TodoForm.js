import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';;

// Jaunas funkcijas izveidošana. Funkcija atbild par To Do iavadīšanās formu.
function TodoForm({ addTodo, setFilter }) {
  const [todo, setTodo] = useState({
    id: '',
    name: '',
    completed: false
  });

// Funkcija, kas nostrādā, kad lietotājs ieraksta ievadi
  function handleInputChange(e) {
    // e.target.value satur jaunu ievadi no onChange
    // notikums ievades elementiem
    setTodo({ ...todo, task: e.target.value})
  }

// Funkcija, kas apstrādā jaunu uzdevumu pievienošanu sarakstā.
  function handleAdd(e) {
// Noklusējuma pārlūkprogrammas iesniegšanas funkcionalitātes novēršana. Lai izvairīties no auto pārlādes.
    e.preventDefault();

    if (todo.task.trim()) {
      // trim() atbrīvo no atstarpēm
      addTodo({ ...todo, id: uuidv4() });
      // Uzdevuma ievada atietastīšana
      setTodo({ ...todo, task: '' });
    }
  }

  const statusHandler = (e) => {
    setFilter(e.target.value);
  }

// Ievadīšanas formas struktūras atgriešana
  return (
    <form onSubmit={handleAdd} className='inputField'>
      <input
        name='task'
        className='inputStyle'
        type='text'
        value={todo.task || ''}
        onChange={handleInputChange}
      />
      <button type='submit' className='formButton'>PIEVIENOT</button>
      <div>
        <select onChange={statusHandler} className='custom-select'>
          <option value='all'>VISI</option>
          <option value='completed'>IZPILDĪTIE</option>
          <option value='uncompleted'>NEIZPILDĪTIE</option>
        </select>
    </div>
    </form>
  );
}

export default TodoForm;
