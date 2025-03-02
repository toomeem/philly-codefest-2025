import React from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const navigate = useNavigate();

    const handleLogin = () => {
        // Simulate authentication logic
        // After successful login, redirect to chatbot page
        navigate("/chatbot");
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-gray-200 p-4">
            {/* Login Section */}
            <div className="flex flex-col w-full md:w-3/5 bg-gray-800 rounded-lg shadow-lg overflow-hidden mt-24 md:mt-28 p-8 max-w-lg">
                <h2 className="text-center text-2xl font-bold mb-6">Login</h2>
                <div className="form-control w-full">
                    <label className="label"><span className="label-text">Username or Email</span></label>
                    <input type="text" placeholder="Enter your email" className="input input-bordered w-full" />
                </div>
                <div className="form-control w-full mt-4">
                    <label className="label"><span className="label-text">Password</span></label>
                    <input type="password" placeholder="Enter your password" className="input input-bordered w-full" />
                </div>
                <div className="flex items-center mt-4">
                    <input type="checkbox" className="checkbox mr-2" />
                    <span>Remember me</span>
                </div>
                <button onClick={handleLogin} className="btn btn-primary w-full mt-4">Login</button>

                {/* Google Login */}
                <div className="mt-6">
                    <button className="btn btn-primary bg-red-500 text-white w-full">
                        <i className="fab fa-google mr-2"></i>Login with Google
                    </button>
                </div>

                {/* Back to Home Button */}
                <button
                    onClick={() => navigate("/")}
                    className="btn btn-defult w-full mt-4"
                >
                    Back to Home
                </button>
            </div>
        </div>
    );
};

export default Login;