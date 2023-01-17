import React, {
  FC,
  useState,
} from 'react'
import { TApiNewsOfMonthParams } from '../api/api'
import query from '../api/query'
import { Table } from 'react-bootstrap'

export const NewsOfMonthTable: FC = () => {
  const [ newsOfMonthParams, setNewsOfMonthParams ] = useState<TApiNewsOfMonthParams>(
    { amount: 100, month_you_wanted: 'Дек' },
  )
  const { data: newsOfMonth, isLoading: isLoadingNewsOfMonth } = query.newsOfMonth(newsOfMonthParams)

  return (
    <div style={ { maxHeight: '70vh', overflow: 'hidden', overflowY: 'auto' } }>
      <Table striped bordered hover>
        <thead>
        <th>№</th>
        <th>Заголовок</th>
        <th>Дата</th>
        <th>Контент</th>
        </thead>
        <tbody>{
          newsOfMonth?.map((newsItem, i) => (<tr key={ newsItem._id }>
            <td>{ i + 1 }</td>
            <td><a target="_blank" href={ newsItem.url }>{ newsItem.title }</a></td>
            <td style={ { whiteSpace: 'nowrap' } }>{ newsItem.date }</td>
            <td style={{textAlign: 'justify'}}>{ newsItem.body }</td>
          </tr>))
        }</tbody>
      </Table>
    </div>
  )
}