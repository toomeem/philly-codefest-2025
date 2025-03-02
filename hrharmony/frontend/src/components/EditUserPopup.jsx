import React, { useState, useEffect } from "react";

const EditUserPopup = ({ closePopup }) => {
    const [users, setUsers] = useState([]);
    const [selectedUser, setSelectedUser] = useState(null);
    const [newDepartment, setNewDepartment] = useState("");

    useEffect(() => {
        // Fetch users from the backend
        const fetchUsers = async () => {
            try {
                const response = await fetch("http://localhost:8080/org_users", {
                    method: "GET",
                    headers: { "Content-Type": "application/json" },
                });
                const data = await response.json();
                if (response.ok) {
                    console.log("Users fetched successfully:", data.users);
                    setUsers(data.users);
                } else {
                    console.error("Error fetching users:", data.error);
                }
            } catch (error) {
                console.error("Failed to fetch users:", error);
            }
        };

        fetchUsers();
    }, []);

    const handleEditUser = async () => {
        if (!selectedUser || !newDepartment) return;

        try {
            const response = await fetch(`http://localhost:8080/user/${selectedUser.id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ department: newDepartment }),
            });

            const data = await response.json();
            if (response.ok) {
                alert("User updated successfully!");
                setUsers(users.map(user =>
                    user.id === selectedUser.id ? { ...user, department: newDepartment } : user
                ));
                setSelectedUser(null);
                setNewDepartment("");
            } else {
                alert(`Error: ${data.error}`);
            }
        } catch (error) {
            console.error("Error updating user:", error);
            alert("Failed to update user.");
        }
    };

    const handleRemoveUser = async (id) => {
        try {
            const response = await fetch(`http://localhost:8080/user/${id}`, {
                method: "DELETE",
            });

            const data = await response.json();
            if (response.ok) {
                setUsers(users.filter(user => user.id !== id));
                alert("User deleted successfully.");
            } else {
                alert(`Error: ${data.error}`);
            }
        } catch (error) {
            console.error("Error deleting user:", error);
            alert("Failed to delete user.");
        }
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
                                <button className="btn btn-sm btn-warning" onClick={() => setSelectedUser(user)}>
                                    Edit
                                </button>
                                <button className="btn btn-sm btn-error" onClick={() => handleRemoveUser(user.id)}>
                                    Remove
                                </button>
                            </div>
                        </li>
                    ))}
                </ul>

                {selectedUser && (
                    <div className="mt-4">
                        <h4 className="text-lg text-yellow-300">Editing {selectedUser.email}</h4>
                        <select
                            className="select select-bordered w-full mt-2"
                            value={newDepartment}
                            onChange={(e) => setNewDepartment(e.target.value)}
                        >
                            <option value="" disabled>Select New Department</option>
                            <option value="HR">HR</option>
                            <option value="IT">IT</option>
                        </select>
                        <button className="btn btn-primary w-full mt-2" onClick={handleEditUser}>
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
