import React, { useState, useEffect, useRef } from 'react';

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

    const updateChat = () => {
        if (inputText.trim() !== '') {
            addMessage(inputText, 'user');
            setTimeout(() => {
                addMessage(`You said: "${inputText}"`, 'bot');
            }, 500);
            setInputText('');
        }
    };

    const startNewConversation = () => {
        setConversations([...conversations, `Conversation ${conversations.length + 1}`]);
        setMessages([]);
    };

    return (
        <div className="bg-gray-900 text-white min-h-screen flex flex-col">
            <header className="navbar bg-base-100 p-4 w-full">
                <div className="flex-none">
                    <button className="btn btn-square btn-ghost">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block h-5 w-5 stroke-current">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
                <div className="flex-1">
                    <a className="btn btn-ghost text-xl">HR Harmony</a>
                </div>
                <div className="flex-none">
                    <div className="dropdown dropdown-end">
                        <div tabIndex="0" role="button" className="btn btn-ghost btn-circle avatar">
                            <div className="w-10 rounded-full">
                                <img alt="User Avatar" src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                            </div>
                        </div>
                        <ul tabIndex="0" className="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                            <li><a className="justify-between">Profile<span className="badge">New</span></a></li>
                            <li><a>Settings</a></li>
                            <li><a>Logout</a></li>
                        </ul>
                    </div>
                </div>
            </header>

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
