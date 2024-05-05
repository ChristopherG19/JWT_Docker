import './App.css'
import { useState } from 'react'
import axios from 'axios'

const App = () => {
  // Se definen variables a utilizar durante ejecución
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [token, setToken] = useState('')
  const [message, setMessage] = useState('')

  // Función para manejar el registro
  const Register = async () => {
    console.log(username, password)
    try {
      const response = await axios.post('http://localhost:5000/register', {
        username,
        password
      })
      setMessage(response.data.message)
    } catch (error) {
      setMessage(error.response.data.message)
    }
  }

  // Función para manejar el login
  const Login = async () => {
    console.log(username, password)
    try {
      const response = await axios.post('http://localhost:5000/login', {
        username,
        password
      })
      if (response.data.access_token) {
        setToken(response.data.access_token)
        setMessage('Login exitoso')
      } else {
        setMessage('Error en inicio de sesión')
      }
    } catch (error) {
      setMessage(error.response.data.message)
    }
  }

  // Función para acceder a un recurso protegido
  const handleProtected = async () => {
    try {
      const response = await axios.get('http://localhost:5000/protected', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      setMessage(response.data.message)
    } catch (error) {
      setMessage(error.response.data.message)
    }
  }

  // Interfaz de usuario del componente.
  return (
    <div className="container">
      <h1 className="title">JWT Auth</h1>
      <div className="form-group">
        <input
          type="text"
          className="input-field"
          placeholder="Username"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
        />
        <input
          type="password"
          className="input-field"
          placeholder="Password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />
        <br></br>
        <br></br>
        <button className="btn" onClick={Register}>Register</button>
        <br></br>
        <br></br>
        <button className="btn" onClick={Login}>Login</button>
        <br></br>
        <br></br>
      </div>
      {token && (
        <div>
          <br></br>
          <br></br>
          <button className="btn" onClick={handleProtected}>Access Protected Resource</button>
        </div>
      )}
      {message && <h1 className="message">{message}</h1>}
    </div>
  );
}
export default App