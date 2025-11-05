/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        amazonBlue: "#232F3E",
        amazonYellow: "#FF9900",
        amazonGray: "#F3F3F3",
      },
    },
  },
  plugins: [],
};
