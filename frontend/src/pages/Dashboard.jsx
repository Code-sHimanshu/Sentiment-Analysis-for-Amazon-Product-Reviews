import React, { useState } from "react";

export default function Dashboard() {
  const [review, setReview] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/api/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ review }),
      });

      if (!response.ok) {
        throw new Error("API request failed");
      }

      const data = await response.json();
      setResult(data.sentiment);
    } catch (err) {
      console.error(err);
      setError("Error fetching sentiment result. Check backend connection.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-gray-100 via-gray-200 to-gray-300 px-6 py-10">
      {/* Header */}
      <div className="text-center mb-10">
        <h1 className="text-4xl font-extrabold text-[#232F3E] mb-3 tracking-tight drop-shadow-sm">
          🛒 Amazon Sentiment Dashboard
        </h1>
        <p className="text-lg text-gray-600">
          Analyze customer product reviews using AI
        </p>
      </div>

      {/* Card */}
      <div className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-2xl border border-gray-100 hover:shadow-2xl transition-shadow duration-300">
        <form onSubmit={handleSubmit} className="flex flex-col">
          <label className="text-lg font-semibold text-gray-700 mb-2">
            ✍️ Enter a Product Review:
          </label>
          <textarea
            value={review}
            onChange={(e) => setReview(e.target.value)}
            placeholder="Type your review here..."
            className="w-full h-32 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-400 focus:outline-none resize-none text-gray-800"
          />

          <button
            type="submit"
            className={`mt-5 py-2.5 rounded-lg font-semibold text-white transition-all duration-300 ${
              loading
                ? "bg-yellow-400 cursor-not-allowed"
                : "bg-[#FF9900] hover:bg-[#F59E0B]"
            }`}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze Sentiment"}
          </button>
        </form>

        {/* Result Section */}
        <div className="mt-6 text-center">
          {error && (
            <p className="text-red-500 font-medium animate-pulse">{error}</p>
          )}
          {result && (
            <div className="mt-4 text-xl font-semibold">
              Sentiment:&nbsp;
              <span
                className={`${
                  result === "positive"
                    ? "text-green-600"
                    : result === "negative"
                    ? "text-red-600"
                    : "text-yellow-600"
                }`}
              >
                {result.toUpperCase()}
              </span>
            </div>
          )}
        </div>
      </div>

      {/* Charts Section (Coming next) */}
      <div className="mt-10 w-full max-w-2xl bg-white p-6 rounded-xl shadow-md border border-gray-100 text-center">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">
          Sentiment Overview (Coming Soon)
        </h2>
        <p className="text-gray-500 text-sm">
          Interactive charts will appear here once we integrate Recharts 📊
        </p>
      </div>

      {/* Footer */}
      <footer className="mt-12 text-gray-500 text-sm text-center">
        © {new Date().getFullYear()} Amazon Sentiment Dashboard | Built by HIMANSHU SINGH, AI/ML Intern at InlighnX Global Pvt. Ltd. 💛
      </footer>
    </div>
  );
}
