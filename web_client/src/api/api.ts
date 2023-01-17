import {
  TMarkedNewsItem,
  TMonth,
  TNewsItem,
  TTonalityItem,
  TWord2VecItem,
} from '../types'
import client from './client'
import { compact } from 'lodash'

export type TApiNewsOfMonthParams = { amount?: number, month_you_wanted?: TMonth }
export type TApiMarkedNewsParams = { amount?: number }

export const api = {
  newsOfMonth: async (params?: TApiNewsOfMonthParams): Promise<TNewsItem[]> => {
    const _params: string = compact([
      params?.amount && `amount=${ params.amount }`,
      params?.month_you_wanted && `month_you_wanted=${ params.month_you_wanted }`,
    ]).join('&')
    return (await client.get<TNewsItem[]>(`/parse/get_news_of_the_month?${ _params }`)).data
  },
  markedNews: async (params?: TApiMarkedNewsParams): Promise<TMarkedNewsItem[]> => {
    const _params: string = compact([
      params?.amount && `amount=${ params.amount }`,
    ]).join('&')
    return (await client.get<TMarkedNewsItem[]>(`/parse/get_marked_news?${ _params }`)).data
  },
  tonality: async (): Promise<TTonalityItem[]> => (await client.get<TTonalityItem[]>('/parse/tonalty')).data,
  word2vec: async (word: string): Promise<TWord2VecItem[]> => (await client.get<TWord2VecItem[]>(`/parse/word2vec?word=${word}`)).data,
}
