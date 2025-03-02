import React, { useState } from "react";
import Navbar from "../../components/navbar.jsx";

const UserProfile = () => {
    const [isEditing, setIsEditing] = useState(false);

    return (
        <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center">
            {/* Navbar */}
            <Navbar />

            {/* Profile Page */}
            <div className="flex flex-col w-4/5 mt-24 bg-gray-800 rounded-lg shadow-lg overflow-hidden p-6">
                {/* Profile Details */}
                <main className="flex flex-col items-center text-center">
                    <img
                        src="https://randomuser.me/api/portraits/women/44.jpg"
                        alt="User Profile"
                        className="w-24 h-24 rounded-full object-cover"
                    />
                    <h2 className="text-2xl font-bold text-yellow-400 mt-4">Welcome, Ida</h2>

                    <div className="mt-6 space-y-3 text-left">
                        <p><strong>Full Name:</strong> Ida Miller</p>
                        <p><strong>Pronouns:</strong> She/Her</p>
                        <p><strong>Email:</strong> ida.admin@example.com</p>
                        <p><strong>Position/Department:</strong> HR Manager</p>
                        <p><strong>About Me:</strong> Passionate about fostering a positive workplace culture and helping employees thrive.</p>
                    </div>

                    <button
                        onClick={() => setIsEditing(true)}
                        className="btn btn-warning mt-4"
                    >
                        Edit Profile
                    </button>
                </main>
            </div>

            {/* Edit Profile Popup */}
            {isEditing && (
                <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
                    <div className="bg-gray-800 p-6 rounded-lg shadow-lg w-96">
                        <h3 className="text-xl font-bold mb-4">Edit Profile</h3>
                        {/* Form inputs for editing */}
                        <input type="text" placeholder="Full Name" className="input input-bordered w-full mb-3" />
                        <input type="text" placeholder="Pronouns" className="input input-bordered w-full mb-3" />
                        <input type="email" placeholder="Email" className="input input-bordered w-full mb-3" />
                        <input type="text" placeholder="Position/Department" className="input input-bordered w-full mb-3" />
                        <textarea placeholder="About Me" className="textarea textarea-bordered w-full mb-3"></textarea>
                        <div className="flex justify-between">
                            <button
                                onClick={() => setIsEditing(false)}
                                className="btn btn-error"
                            >
                                Cancel
                            </button>
                            <button className="btn btn-success">Save</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default UserProfile;