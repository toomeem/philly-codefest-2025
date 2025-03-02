import React, { useState } from "react";

const AddDocumentPopup = ({ closePopup }) => {
    const [selectedDepartment, setSelectedDepartment] = useState("");
    const [file, setFile] = useState(null);

    const handleUpload = () => {
        if (!selectedDepartment || !file) {
            alert("Please select a department and upload a file.");
            return;
        }
        console.log("Uploading file:", file.name, "to department:", selectedDepartment);
        closePopup();
    };

    return (
        <dialog className="modal modal-open">
            <div className="modal-box bg-base-200">
                <h3 className="font-bold text-lg text-primary">Add Document</h3>

                {/* Select Department */}
                <select
                    className="select select-bordered w-full mt-3"
                    value={selectedDepartment}
                    onChange={(e) => setSelectedDepartment(e.target.value)}
                >
                    <option value="" disabled selected>Select Department</option>
                    <option value="HR">HR</option>
                    <option value="IT">IT</option>
                    <option value="Finance">Finance</option>
                </select>

                {/* File Input */}
                <input
                    type="file"
                    className="file-input file-input-bordered w-full mt-3"
                    onChange={(e) => setFile(e.target.files[0])}
                    disabled={!selectedDepartment}
                />

                {/* Action Buttons */}
                <div className="modal-action">
                    <button
                        className="btn btn-primary w-full"
                        onClick={handleUpload}
                        disabled={!selectedDepartment || !file}
                    >
                        Upload
                    </button>
                    <button
                        className="btn btn-error w-full mt-2"
                        onClick={closePopup}
                    >
                        Close
                    </button>
                </div>
            </div>
        </dialog>
    );
};

export default AddDocumentPopup;
