import React, {
  FC,
  useState,
} from 'react'
import { Table } from 'react-bootstrap'
import { TApiMarkedNewsParams } from '../api/api'
import query from '../api/query'
import { uniq } from 'lodash'

export const MarkedNewsTable: FC = () => {
  const [ markedNewsParams, setMarkedNewsParams ] = useState<TApiMarkedNewsParams>(
    { amount: 100 },
  )
  const { data: markedNews, isLoading: isLoadingMarkedNews } = query.markedNews(markedNewsParams)

  return (
    <div style={ { maxHeight: '70vh', overflow: 'hidden', overflowY: 'auto' } }>
      <Table striped bordered hover>
        <thead>
        <th>№</th>
        <th>Ссылка</th>
        <th>Дата</th>
        <th>Сущности</th>
        <th>Предложение</th>
        </thead>
        <tbody>{
          markedNews?.map((newsItem, i) => (<tr key={ newsItem._id }>
            <td>{ i + 1 }</td>
            <td><a target="_blank" href={ newsItem.url }>Первоисточник</a></td>
            <td style={ { whiteSpace: 'nowrap' } }>{ newsItem.date }</td>
            <td>{ uniq(newsItem.person_non_person).join(', ') }</td>
            <td style={{textAlign: 'justify'}}>{ newsItem.text }</td>
          </tr>))
        }</tbody>
      </Table>
    </div>
  )
}