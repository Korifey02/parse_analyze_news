import axios, { CreateAxiosDefaults } from 'axios'
import { QueryClient } from '@tanstack/react-query'

const baseURL = process.env.REACT_APP_SERVER_HOST
  ? `http://${ process.env.REACT_APP_SERVER_HOST }:${ process.env.REACT_APP_SERVER_PORT }`
  : 'http://127.0.0.1:8000'

const createClientInstance = () => {
  const defaultOptions: CreateAxiosDefaults = {
    baseURL,
    headers: {
      'Content-Type': 'application/json',
    },
    withCredentials: true,
  }

  // Create instance
  const instance = axios.create(defaultOptions)
  return instance
}

export default createClientInstance()

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: false,
      // refetchOnWindowFocus : false,
      // onError : err => toast.error(JSON.stringify((err as AxiosError<TServerAnswer>).response?.data)),
    },
  },
})