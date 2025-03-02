import React, { useState, useEffect, useRef } from "react";
import Navbar from "../../components/navbar.jsx";

const ChatbotPage = () => {
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState('');
    const [conversations, setConversations] = useState(['Conversation 1', 'Conversation 2']);
    const chatContainerRef = useRef(null);

    useEffect(() => {
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
    }, [messages]);

    const addMessage = (message, sender) => {
        setMessages(prevMessages => [...prevMessages, { sender, message }]);
    };

    const updateChat = async () => {
        if (inputText.trim() !== '') {
            const userMessage = inputText;
            addMessage(userMessage, 'user');
            setInputText('');

            try {
                const response = await fetch("http://localhost:8080/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        user_id: "4a85be08-8b60-46f1-a062-8ecf5b527c28",
                        query: userMessage
                    })
                });

                const data = await response.json();
                if (response.ok) {
                    addMessage(data.response, 'bot');
                } else {
                    addMessage("Error fetching response", 'bot');
                }
            } catch (error) {
                addMessage("Server error, please try again later", 'bot');
            }
        }
    };
    const startNewConversation = () => {
        setConversations([...conversations, `Conversation ${conversations.length + 1}`]);
        setMessages([]);
    };
    // conversations[2] = [
    //     {
    //     "role": "user",
    //     "content": "is remote work allowed?"
    //     },
    //     {
    //     "role": "assistant",
    //     "content": "Yes, flexible work arrangements, including remote work, are available for eligible employees at Nexora Tech Solutions. However, specific eligibility criteria and guidelines may apply, so it's best to check with your manager or HR for more details regarding your situation and the process to request remote work."
    //     },
    //     {
    //     "role": "user",
    //     "content": "Do I have pto?"
    //     },
    //     {
    //     "role": "assistant",
    //     "content": "To find out if you have Paid Time Off (PTO) and what your current balance is, you should check your employment records or HR dashboard. If you're unable to access this information, I recommend reaching out to HR directly for assistance. They can provide specific details regarding your PTO entitlement and remaining balance."
    //     },
    //     {
    //     "role": "user",
    //     "content": "is remote work allowed?"
    //     },
    //     {
    //     "role": "assistant",
    //     "content": "Yes, remote work is allowed at Nexora Tech Solutions for eligible employees, as flexible work arrangements are available. However, specific eligibility criteria and guidelines may apply, so it's best to discuss the details with your manager or HR to understand the process and requirements for requesting remote work."
    //     },
    //     {
    //     "role": "user",
    //     "content": "do resignations require 2 weeks?"
    //     },
    //     {
    //     "role": "assistant",
    //     "content": "Yes, it is generally expected that employees provide a two-week notice period when resigning from their position. This allows for a smoother transition and gives the company time to manage the departure. However, it's always a good idea to check with your specific department or HR for any additional requirements or variations on this policy."
    //     }
    // ]

    return (
        <div className="bg-gray-900 text-white min-h-screen flex flex-col">
            <Navbar /> {/* Use Navbar Component */}

            <div className="flex flex-grow h-[calc(100vh-4rem)]">
                <div className="w-80 bg-base-200 p-4 flex flex-col">
                    <button className="btn btn-primary mb-4" onClick={startNewConversation}>New Conversation</button>
                    <ul className="menu text-base-content flex-grow overflow-y-auto">
                        {conversations.map((conv, index) => (
                            <li key={index}><a>{conv}</a></li>
                        ))}
                    </ul>
                </div>

                <main className="flex flex-col flex-grow bg-gray-700 h-full">
                    <div ref={chatContainerRef} className="flex-grow overflow-y-auto p-2 space-y-4 max-h-[calc(100vh-8rem)]">
                        {messages.map((msg, index) => (
                            <div key={index} className={`chat ${msg.sender === 'user' ? 'chat-end' : 'chat-start'}`}>
                                <div className="chat-image avatar">
                                    <div className="w-10 rounded-full">
                                        <img alt="Avatar" src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                                    </div>
                                </div>
                                <div className="chat-header">
                                    {msg.sender === 'user' ? 'User' : 'Bot'}
                                    <time className="text-xs opacity-50 ml-2">12:45</time>
                                </div>
                                <div className="chat-bubble">{msg.message}</div>
                                <div className="chat-footer opacity-50">Delivered</div>
                            </div>
                        ))}
                    </div>
                    <div className="p-4 border-t border-gray-600 flex items-center w-full">
                        <input type="text" value={inputText} onChange={(e) => setInputText(e.target.value)}
                            onKeyDown={(e) => e.key === 'Enter' && updateChat()}
                            className="input input-bordered w-full" placeholder="Type your message..." />
                        <button onClick={updateChat} className="ml-2 btn btn-primary">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" className="w-6 h-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                            </svg>
                        </button>
                    </div>
                </main>
            </div>
        </div>
    );
};

export default ChatbotPage;
