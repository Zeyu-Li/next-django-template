import Link from 'next/link'

const Custom404 = () => {
  return (
    <>
      <h1>Page not found ¯\(°_o)/¯</h1>
      <Link href={'/'}>
        <button>Back to Home</button>
      </Link>
    </>
  )
}
export default Custom404
