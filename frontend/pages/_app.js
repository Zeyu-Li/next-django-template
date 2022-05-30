import Head from '../components/head/Head'
import '../styles/_globals.scss'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head />
      <noscript>You need to enable JavaScript to run this app.</noscript>
      <Component {...pageProps} />
    </>
  )
}

export default MyApp
