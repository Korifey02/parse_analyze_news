import React, {
  FC,
  useState,
} from 'react'
import query from '../api/query'
import {
  Button,
  Form,
  Table,
} from 'react-bootstrap'

export const Word2VecTable: FC = () => {
  const [ word, setWord ] = useState<string>('')
  const { mutateAsync, data, isLoading } = query.word2vec()

  return (
    <div style={ { maxHeight: '70vh', overflow: 'hidden', overflowY: 'auto' } }>
      <Form style={ { display: 'flex', gap: '10px', margin: '10px' } }>
        <Form.Control
          style={ { flexGrow: 1 } }
          type="text"
          placeholder="Слово"
          value={ word }
          onChange={ e => setWord(e.currentTarget.value) }
          disabled={ isLoading }
        />
        <Button disabled={ isLoading } variant="success" onClick={ () => mutateAsync(word) }>Отправить</Button>
      </Form>
      <Table striped bordered hover>
        <thead>
        <th>№</th>
        <th>Слово</th>
        <th>Коэффициент</th>
        </thead>
        <tbody>{
          data?.map(([ _word, ratio ], i) => (<tr key={ _word }>
            <td>{ i + 1 }</td>
            <td>{ _word }</td>
            <td>{ ratio }</td>
          </tr>))
        }</tbody>
      </Table>
    </div>
  )
}