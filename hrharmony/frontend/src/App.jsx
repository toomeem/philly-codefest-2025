import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import WelcomePage from "./pages/welcomepage/welcomepage.jsx";
import LoginPage from "./pages/login/loginpage.jsx";
import Dashboard from "./pages/admindashboard/dash/AdminDashboard.jsx";
import Profile from "./pages/profile/profile.jsx";
import ChatbotPage from "./pages/chatbot/chatbotpage.jsx"; // Uncomment when ready

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} /> {/* Make WelcomePage the landing page */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
        {<Route path="/chatbot" element={<ChatbotPage />} />}
      </Routes>
    </Router>
  );
}

export default App;
