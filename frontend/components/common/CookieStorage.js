import Cookies from 'js-cookie'

export const getAccessToken = () => {
  return Cookies.get('accessToken')
}
export const setAccessToken = (token) => {
  return Cookies.set('accessToken', token)
}
