import React from "react";
import amazonLogo from "../assets/amazon_logo.png";
import "../styles/theme.css";

const Navbar = () => {
  return (
    <nav
      style={{
        backgroundColor: "var(--amazon-black)",
        padding: "10px 20px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        color: "white",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <img src={amazonLogo} alt="Amazon Logo" style={{ height: "32px" }} />
        <h2 style={{ color: "var(--amazon-orange)", margin: 0 }}>
          Sentiment Insights
        </h2>
      </div>
      <span style={{ fontSize: "14px" }}>Amazon Product Reviews</span>
    </nav>
  );
};

export default Navbar;
