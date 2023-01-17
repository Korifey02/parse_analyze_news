import React, { FC } from 'react'
import { Table } from 'react-bootstrap'
import query from '../api/query'
import { uniq } from 'lodash'

export const TonalityTable: FC = () => {
  const { data: tonalityItems, isLoading } = query.tonality()

  return (
    <div style={ { maxHeight: '70vh', overflow: 'hidden', overflowY: 'auto' } }>
      <Table striped bordered hover>
        <thead>
        <th>№</th>
        <th>Текст</th>
        <th>Тональность</th>
        <th>Сущности</th>
        </thead>
        <tbody>{
          tonalityItems?.map((item, i) => (<tr key={ item._id }>
            <td>{ i + 1 }</td>
            <td style={{textAlign: 'justify'}}>{ item.text }</td>
            <td>{ item.ton === 'Positive' ? 'Позитивная' : 'Негативная' }</td>
            <td>{ uniq(item.person_non_person).join(', ') }</td>
          </tr>))
        }</tbody>
      </Table>
    </div>
  )
}