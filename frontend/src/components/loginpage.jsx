import React from "react";
import './loginpage.css';

const loginpage = () => {
    return <div className = "page">
        <div className = "box">
            <h1>Login</h1>
            <div className = " input-box">
                <input type="text" placeholder="username" required/>
            </div>
            <div className="input-box">
                <input type="password" placeholder="password" required/>
            </div>
            <button type="submit">Login</button>
        </div>
    </div>
}

export default loginpage;