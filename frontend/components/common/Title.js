import Head from 'next/head'

const Title = ({ title }) => {
  return (
    <Head>
      <title>{title}</title>
    </Head>
  )
}
export default Title
