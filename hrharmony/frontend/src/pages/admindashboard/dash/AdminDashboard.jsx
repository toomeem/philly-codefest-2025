import React, { useState } from "react";
import Navbar from "../../../components/navbar.jsx";
import AddDocumentPopup from "../../../components/AddDocumentPopup.jsx";
import EditDocumentPopup from "../../../components/EditDocumentPopup.jsx";
import AddUserPopup from "../../../components/AddUserPopup.jsx";
import EditUserPopup from "../../../components/EditUserPopup.jsx";

const AdminDashboard = () => {
    const [activePopup, setActivePopup] = useState(null);

    const openPopup = (popupId) => {
        setActivePopup(popupId);
    };

    const closePopup = () => {
        setActivePopup(null);
    };

    return (
        <div className="min-h-screen flex flex-col items-center bg-gray-900 text-gray-100">
            {/* Navigation Bar */}
            <Navbar />

            {/* Admin Dashboard */}
            <div className="flex flex-col items-center text-center p-10 w-full max-w-4xl">
                <h2 className="text-5xl text-yellow-400 font-bold mb-8">Welcome, Admin</h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
                    {[
                        { id: "addDocPopup", icon: "fa-file-upload", text: "Add Document" },
                        { id: "editDocPopup", icon: "fa-edit", text: "Edit Document" },
                        { id: "addUserPopup", icon: "fa-user-plus", text: "Add User" },
                        { id: "editUserPopup", icon: "fa-user-cog", text: "Edit User" },
                    ].map(({ id, icon, text }) => (
                        <button
                            key={id}
                            className="flex flex-col items-center justify-center p-6 text-lg font-semibold bg-gray-800 text-white rounded-lg shadow-lg hover:bg-yellow-400 hover:text-gray-900 transition transform hover:scale-105"
                            onClick={() => openPopup(id)}
                        >
                            <i className={`fas ${icon} text-3xl mb-3`}></i>
                            {text}
                        </button>
                    ))}
                </div>
            </div>

            {/* Popups */}
            {activePopup === "addDocPopup" && <AddDocumentPopup closePopup={closePopup} />}
            {activePopup === "editDocPopup" && <EditDocumentPopup closePopup={closePopup} />}
            {activePopup === "addUserPopup" && <AddUserPopup closePopup={closePopup} />}
            {activePopup === "editUserPopup" && <EditUserPopup closePopup={closePopup} />}
        </div>
    );
};

export default AdminDashboard;
