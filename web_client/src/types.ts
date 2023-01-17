export type TNewsItem = {
  _id: string
  title: string
  date: string
  url: string
  body: string
}

export type TMarkedNewsItem = {
  _id: string
  text: string
  person_non_person: string[]
  date: string
  url: string
}

export type TTonalityItem = {
  _id: string
  text: string
  ton: 'Positive' | 'Negative'
  person_non_person: string[]
}

export type TWord2VecItem = [string, number]

export const MONTHES = [ 'Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек' ] as const

export type TMonth = typeof MONTHES[number]