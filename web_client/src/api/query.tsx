import {
  useMutation,
  useQuery,
} from '@tanstack/react-query'
import {
  api,
  TApiMarkedNewsParams,
  TApiNewsOfMonthParams,
} from './api'

export const queryKeys = {
  newsOfTheMonthKey: [ 'newsOfMonth' ],
  markedNews: [ 'markedNews' ],
  tonality: [ 'tonality' ],
  word2vec: [ 'word2vec' ],
}
const query = {
  newsOfMonth: (params?: TApiNewsOfMonthParams) => useQuery({
    queryKey: queryKeys.newsOfTheMonthKey,
    queryFn: async () => api.newsOfMonth(params),
  }),
  markedNews: (params?: TApiMarkedNewsParams) => useQuery({
    queryKey: queryKeys.markedNews,
    queryFn: async () => api.markedNews(params),
  }),
  tonality: () => useQuery({
    queryKey: queryKeys.tonality,
    queryFn: api.tonality,
  }),
  word2vec: () => useMutation({
    mutationKey: queryKeys.word2vec,
    mutationFn: api.word2vec,
  }),
}
export default query