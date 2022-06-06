import Link from 'next/link'
import styles from '../styles/pages/user/index.module.scss'

const Home = () => {
  return (
    <>
      <main>
        <div className={styles.main_page}>
          <h1>Welcome to the Next-Django Template</h1>
          <p>To contribute to this repo, click the button below</p>
          <Link href="https://github.com/sponsors/Zeyu-Li">
            <button>Contribute Now</button>
          </Link>
        </div>
      </main>
    </>
  )
}

export default Home
