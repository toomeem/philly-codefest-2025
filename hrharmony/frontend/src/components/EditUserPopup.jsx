import React, { useState } from "react";

const EditUserPopup = ({ closePopup }) => {
    const [users, setUsers] = useState([
        { id: 1, email: "john@example.com", department: "HR" },
        { id: 2, email: "jane@example.com", department: "IT" },
    ]);
    const [selectedUser, setSelectedUser] = useState(null);
    const [newDepartment, setNewDepartment] = useState("");

    const handleRemoveUser = (id) => {
        setUsers(users.filter(user => user.id !== id));
    };

    const handleEditUser = () => {
        if (!selectedUser || !newDepartment) return;
        setUsers(users.map(user =>
            user.id === selectedUser.id ? { ...user, department: newDepartment } : user
        ));
        setSelectedUser(null);
        setNewDepartment("");
    };

    return (
        <dialog className="modal modal-open">
            <div className="modal-box bg-base-200">
                <h3 className="font-bold text-lg text-primary">Edit User</h3>

                <ul className="mt-3">
                    {users.map(user => (
                        <li key={user.id} className="flex justify-between items-center p-2 bg-base-100 rounded-md my-1">
                            <span>{user.email} ({user.department})</span>
                            <div className="flex gap-2">
                                <button
                                    className="btn btn-sm btn-warning"
                                    onClick={() => setSelectedUser(user)}
                                >
                                    Edit
                                </button>
                                <button
                                    className="btn btn-sm btn-error"
                                    onClick={() => handleRemoveUser(user.id)}
                                >
                                    Remove
                                </button>
                            </div>
                        </li>
                    ))}
                </ul>

                {/* Edit User Section */}
                {selectedUser && (
                    <div className="mt-4">
                        <h4 className="text-lg text-yellow-300">Editing {selectedUser.email}</h4>
                        <select
                            className="select select-bordered w-full mt-2"
                            value={newDepartment}
                            onChange={(e) => setNewDepartment(e.target.value)}
                        >
                            <option value="" disabled selected>Select New Department</option>
                            <option value="HR">HR</option>
                            <option value="IT">IT</option>
                        </select>
                        <button
                            className="btn btn-primary w-full mt-2"
                            onClick={handleEditUser}
                        >
                            Save Changes
                        </button>
                    </div>
                )}

                <div className="modal-action">
                    <button className="btn btn-error w-full" onClick={closePopup}>
                        Close
                    </button>
                </div>
            </div>
        </dialog>
    );
};

export default EditUserPopup;
