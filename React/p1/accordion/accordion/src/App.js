import './App.css';
import data from './data'
import React, {useState} from 'react';
import SingleQuestion from './Question'
function App() {
  const [questions, setQuestions]=useState(data)
  return (
    <main>
      <div className="container">
        <h3>101 About Jongseong</h3>
        <section className="info">
          {questions.map((question) => {
            return (
              <SingleQuestion key={question.id} {...question}/>
              )
          })}
        </section>
      </div>
    </main>
  );
}

export default App;
