import Link from 'next/link'
import { useEffect, useState } from 'react'
import { get } from '../components/common/Api'
import Title from '../components/common/Title'
import styles from '../styles/pages/user/index.module.scss'

const Home = () => {
  const [backendStatus, setBackendStatus] = useState('Loading...')

  useEffect(() => {
    get('healthcheck')
      .then((data) => {
        setBackendStatus('healthy')
      })
      .catch((e) => {
        const errorMessage = e.message || 'unavailable'
        setBackendStatus(errorMessage)
        console.error(`Unable to get status: ${errorMessage}`)
      })
  }, [])

  return (
    <>
      <Title title="Next-Django Template App" />
      <main>
        <div className={styles.main_page}>
          <h1>
            Welcome to the
            <br />
            Next-Django Template
          </h1>
          <p>The one stop shop for a full stack app</p>
          <p>
            Currently the server is <code>{backendStatus}</code>
          </p>
          <Link
            href="https://github.com/Zeyu-Li/next-django-template"
            target="_blank"
            title="Contribute now"
          >
            <button>Contribute Now</button>
          </Link>
          <br />
          <Link
            href="https://github.com/sponsors/Zeyu-Li"
            target="_blank"
            title="Support the Creator"
          >
            <button>Support the Creator</button>
          </Link>
        </div>
      </main>
    </>
  )
}

export default Home
