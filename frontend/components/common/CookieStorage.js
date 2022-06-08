import cookie from 'react-cookies'

export const getAccessToken = () => {
  return cookie.load('accessToken')
}
export const setAccessToken = (token) => {
  return cookie.save('accessToken', token)
}
