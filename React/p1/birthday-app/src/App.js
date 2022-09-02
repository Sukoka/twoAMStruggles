import './App.css';
import List from './List';
import Data from './Data';
import React, {useState} from 'react';
function App() {
  const [people, setPeople]= useState(Data)
    return (
    <main>
      <section className='container'>
        <h3>{people.length} Birthdays today HEEE</h3>
        <List people={people}/>
        <button onClick={() => setPeople([])}>Click!!</button>
      </section>
      
     </main>
  );
}

export default App;
