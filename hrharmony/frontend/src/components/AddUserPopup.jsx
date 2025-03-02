import React, { useState } from "react";

const AddUserPopup = ({ closePopup }) => {
    const [email, setEmail] = useState("");
    const [department, setDepartment] = useState("");

    const handleAddUser = () => {
        if (!email || !department) {
            alert("Please enter an email and select a department.");
            return;
        }
        console.log("Adding user:", email, "to department:", department);
        closePopup();
    };

    return (
        <dialog className="modal modal-open">
            <div className="modal-box bg-base-200">
                <h3 className="font-bold text-lg text-primary">Add User</h3>

                <input
                    type="email"
                    placeholder="Employee Email"
                    className="input input-bordered w-full mt-3"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <select
                    className="select select-bordered w-full mt-3"
                    value={department}
                    onChange={(e) => setDepartment(e.target.value)}
                >
                    <option value="" disabled selected>Select Department</option>
                    <option value="HR">HR</option>
                    <option value="IT">IT</option>
                </select>

                {/* Properly Aligned Buttons */}
                <div className="modal-action flex justify-between gap-2">
                    <button
                        className="btn btn-primary w-1/2"
                        onClick={handleAddUser}
                    >
                        Create Account
                    </button>
                    <button
                        className="btn btn-error w-1/2"
                        onClick={closePopup}
                    >
                        Close
                    </button>
                </div>
            </div>
        </dialog>
    );
};

export default AddUserPopup;
