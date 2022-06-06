import Link from 'next/link'
import Title from '../components/common/Title'
import styles from '../styles/pages/shared/404.module.scss'

const Custom404 = () => {
  return (
    <>
      <Title title="Page Stolen 😳" />
      <main>
        <div className={styles.error_page}>
          <h1>Page not found ¯\(°_o)/¯</h1>
          <Link href={'/'}>
            <button>Back to Home</button>
          </Link>
        </div>
      </main>
    </>
  )
}
export default Custom404
