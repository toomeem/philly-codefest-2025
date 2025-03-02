import React from "react";
import Navbar from "../../components/navbar.jsx";
import { Link } from "react-router-dom"; // Import Link from react-router-dom

const WelcomePage = () => {
    return (
        <div className="bg-gray-900 text-white min-h-screen flex flex-col items-center justify-center">
            <Navbar />

            {/* Unified Section */}
            <section
                className="relative w-full flex flex-col items-center text-center bg-cover bg-center min-h-screen justify-center"
                style={{ backgroundImage: "url('https://source.unsplash.com/1600x900/?office,work')" }}
            >
                <div className="absolute inset-0 bg-black bg-opacity-50"></div>
                <div className="relative z-10 animate-fade-in max-w-4xl flex flex-col items-center justify-center">
                    <h1 className="text-4xl md:text-6xl font-extrabold tracking-wide mb-3">
                        Welcome to HR Harmony
                    </h1>
                    <p className="text-md md:text-lg opacity-80 max-w-2xl mx-auto">
                        Your AI-powered assistant for all HR-related queries and workplace solutions.
                    </p>

                    {/* Correct navigation */}
                    <div className="mt-4 flex justify-center">
                        <Link to="/Login" className="btn btn-outline btn-primary">
                            Try the Chatbot
                        </Link>
                    </div>

                    <div className="mt-8 text-center">
                        <h2 className="text-3xl md:text-4xl font-bold mb-4">About HR Harmony</h2>
                        <p className="text-md md:text-lg max-w-3xl mx-auto opacity-80">
                            HR Harmony is your trusted AI-powered assistant, helping businesses and employees navigate HR policies and best practices with ease.
                        </p>
                    </div>

                    <div className="stats stats-vertical lg:stats-horizontal shadow">
                        {/* Downloads */}
                        <div className="stat">
                            <div className="stat-figure text-blue-600">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    className="inline-block h-8 w-8 stroke-current"
                                >
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth="2"
                                        d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                    ></path>
                                </svg>
                            </div>
                            <div className="stat-title">Downloads</div>
                            <div className="stat-value text-blue-600">31K</div>
                            <div className="stat-desc">Jan 1st - Feb 1st</div>
                        </div>

                        {/* New Users */}
                        <div className="stat">
                            <div className="stat-figure text-blue-600">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    className="inline-block h-8 w-8 stroke-current"
                                >
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth="2"
                                        d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
                                    ></path>
                                </svg>
                            </div>
                            <div className="stat-title">New Users</div>
                            <div className="stat-value text-blue-600">4,200</div>
                            <div className="stat-desc">↗︎ 400 (22%)</div>
                        </div>

                        {/* New Registers */}
                        <div className="stat">
                            <div className="stat-figure text-blue-600">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    className="inline-block h-8 w-8 stroke-current"
                                >
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth="2"
                                        d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"
                                    ></path>
                                </svg>
                            </div>
                            <div className="stat-title">New Registers</div>
                            <div className="stat-value text-blue-600">1,200</div>
                            <div className="stat-desc">↘︎ 90 (14%)</div>
                        </div>
                    </div>

                </div>
            </section>

            <style>
                {`
                    @keyframes fade-in {
                        from { opacity: 0; transform: translateY(20px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                    .animate-fade-in { animation: fade-in 1s ease-out forwards; }
                `}
            </style>
        </div>
    );
};

export default WelcomePage;
