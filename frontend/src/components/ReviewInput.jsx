import React from "react";

export default function ReviewInput() {
  return (
    <div className="bg-white shadow-md rounded-xl p-6">
      <textarea
        className="w-full border border-gray-300 rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-yellow-400"
        rows="4"
        placeholder="Type a customer review here..."
      ></textarea>
      <button className="mt-4 w-full bg-yellow-400 text-black font-semibold py-2 px-4 rounded-lg hover:bg-yellow-500 transition">
        Analyze Sentiment
      </button>
    </div>
  );
}
