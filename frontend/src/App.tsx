import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={async () => {
          const res = await fetch('http://localhost:8080/api/sap/authorize/')
          console.log(await res.json())
        }}>
          Login with SAP
        </button>
        <br /><br />
        <button onClick={async () => {
          const res = await fetch('http://localhost:8080/api/sap/me/')
          console.log(await res.json())
        }}>
          Get Me from SAP API
        </button>
        <br /><br />
        <button onClick={async () => {
          const res = await fetch('http://localhost:8080/api/sap/users/')
          console.log(await res.json())
        }}>
          Get users from SAP API
        </button>
        <br /><br />
        <button onClick={async () => {
          const res = await fetch('http://localhost:8080/api/sap/lists/')
          console.log(await res.json())
        }}>
          Get lists from SAP API
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
