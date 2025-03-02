// EditDocumentPopup.js
import React, { useState } from "react";

const EditDocumentPopup = ({ closePopup }) => {
    const [filter, setFilter] = useState("");
    const [documents, setDocuments] = useState([
        { id: 1, name: "Report.pdf", department: "HR" },
        { id: 2, name: "Project.docx", department: "IT" },
    ]);
    const [selectedDoc, setSelectedDoc] = useState(null);

    const handleDelete = (id) => {
        setDocuments(documents.filter(doc => doc.id !== id));
    };

    return (
        <dialog className="modal modal-open">
            <div className="modal-box bg-base-200">
                <h3 className="font-bold text-lg text-primary">Edit Document</h3>
                <input type="text" placeholder="Filter documents" className="input input-bordered w-full my-3" value={filter} onChange={(e) => setFilter(e.target.value)} />
                <ul className="max-h-40 overflow-y-auto">
                    {documents.filter(doc => doc.name.toLowerCase().includes(filter.toLowerCase())).map(doc => (
                        <li key={doc.id} className="flex justify-between items-center p-2 bg-base-300 rounded-md my-1">
                            <span>{doc.name} ({doc.department})</span>
                            <button className="btn btn-sm btn-warning" onClick={() => setSelectedDoc(doc)}>Edit</button>
                            <button className="btn btn-sm btn-error" onClick={() => handleDelete(doc.id)}>Delete</button>
                        </li>
                    ))}
                </ul>
                {selectedDoc && (
                    <div className="mt-4">
                        <h4 className="text-lg text-secondary">Editing {selectedDoc.name}</h4>
                        <select className="select select-bordered w-full my-2">
                            <option value="HR">HR</option>
                            <option value="IT">IT</option>
                        </select>
                        <textarea placeholder="Additional Info" className="textarea textarea-bordered w-full my-2"></textarea>
                        <input type="file" className="file-input file-input-bordered w-full my-2" />
                        <button className="btn btn-success w-full">Save Changes</button>
                    </div>
                )}
                <div className="modal-action">
                    <button className="btn btn-error w-full" onClick={closePopup}>Close</button>
                </div>
            </div>
        </dialog>
    );
};

export default EditDocumentPopup;