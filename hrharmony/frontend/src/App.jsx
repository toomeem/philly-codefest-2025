import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ChatbotPage from './pages/chatbot/chatbotpage.jsx'  // Import the chatbot page component

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      {/* Display the chatbot page */}
      <ChatbotPage />  {/* Chatbot page component is rendered here */}
    </div>
  )
}

export default App
