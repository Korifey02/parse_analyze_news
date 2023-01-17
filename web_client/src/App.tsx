import React from 'react'
import { NewsOfMonthTable } from './components/NewsOfMonthTable'
import { MarkedNewsTable } from './components/MarkedNewsTable'
import { TonalityTable } from './components/TonalityTable'
import { Word2VecTable } from './components/Word2VecTable'

function App() {
  return (
    <div className="container">
      <h2 className="text-center fw-bold">100 новостей за месяц</h2>
      <NewsOfMonthTable/>
      <hr/>
      <h2 className="text-center fw-bold">Размеченные новости</h2>
      <MarkedNewsTable/>
      <hr/>
      <h2 className="text-center fw-bold">Тональность</h2>
      <TonalityTable/>
      <hr/>
      <h2 className="text-center fw-bold">Word2Vec</h2>
      <Word2VecTable/>
    </div>
  )
}

export default App

