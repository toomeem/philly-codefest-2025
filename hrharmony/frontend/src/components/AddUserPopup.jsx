import React, { useState } from "react";

const AddUserPopup = ({ closePopup }) => {
    const [email, setEmail] = useState("");
    const [department, setDepartment] = useState("");

    const handleAddUser = async () => {
        if (!email || !department) {
            alert("Please enter an email and select a department.");
            return;
        }

        try {
            const response = await fetch("http://localhost:8080/user", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    email: email,
                    org_id: "org1",  // Update to dynamic input if needed
                    department: department,
                    first_name: "John",  // Update to dynamic input if needed
                    last_name: "Doe",     // Update to dynamic input if needed
                }),
                mode: 'cors'
            });

            const data = await response.json();
            if (response.ok) {
                alert(`User created! Temporary password: ${data.password}`);
                closePopup();
            } else {
                alert(`Error: ${data.error}`);
            }
        } catch (error) {
            console.error("Error creating user:", error);
            alert("Failed to create user.");
        }
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
                    <option value="" disabled>Select Department</option>
                    <option value="HR">HR</option>
                    <option value="IT">IT</option>
                </select>

                <div className="modal-action flex justify-between gap-2">
                    <button className="btn btn-primary w-1/2" onClick={handleAddUser}>
                        Create Account
                    </button>
                    <button className="btn btn-error w-1/2" onClick={closePopup}>
                        Close
                    </button>
                </div>
            </div>
        </dialog>
    );
};

export default AddUserPopup;
