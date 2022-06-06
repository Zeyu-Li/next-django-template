import Header from '../components/head/Header'
import '../styles/_globals.scss'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Header />
      <noscript>You need to enable JavaScript to run this app.</noscript>
      <Component {...pageProps} />
    </>
  )
}

export default MyApp
