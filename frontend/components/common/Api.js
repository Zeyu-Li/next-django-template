import axios from 'axios'
import CONSTANTS from '../constants/constants'
import { getAccessToken } from './CookieStorage'

const getProtocol = () => {
  return new URL(CONSTANTS.DEFAULT_BASE_URL).protocol
}

const getDomain = () => {
  return new URL(CONSTANTS.DEFAULT_BASE_URL).hostname
}

export const host = `${getProtocol()}//${getDomain()}/`

export const get = (uri) => {
  const headers = {
    Authorization: `Bearer ${getAccessToken()}`,
  }

  return axios
    .get(host + uri, {
      headers,
    })
    .then((r) => r.data)
}

export const post = (uri, data) => {
  return fetch(host + uri, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${getAccessToken()}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  }).then(async (response) => {
    if (response.ok) {
      return response.json()
    }
    throw new Error((await response.json()).message)
  })
}

export const del = (uri, data) => {
  const headers = {
    Authorization: `Bearer ${getAccessToken()}`,
  }

  return axios
    .delete(host + uri, {
      data,
      headers,
    })
    .then((r) => r.data)
}

export const patch = (uri, data) => {
  const headers = {
    Authorization: `Bearer ${getAccessToken()}`,
  }

  return axios.patch(host + uri, data, { headers })
}
