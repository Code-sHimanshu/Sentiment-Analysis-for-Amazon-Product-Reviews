import React from "react";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import "./styles/theme.css";

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <Dashboard />
    </div>
  );
}

export default App;
