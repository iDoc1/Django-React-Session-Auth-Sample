import React from 'react';
import { Link } from 'react-router-dom';

function Home({isAuthenticated}) {

    // Login button to be shown only if user is not already authenticated (logged in)
    const loginButton = (
        <>
            <p>Click button to login</p>
            <Link className='btn btn-primary btn-lg' to='login'>Login</Link>
        </>
    );

    return (
        <>
            <div className='mt-5 p-5 bg-light'>
                <h1 className='display-4'>Welcome to the Session Auth App</h1>
                <p className='lead'>This app uses session authentication to allow a user to login.</p>
                <p className='lead'>Once logged in the user can view their profile.</p>
                <hr className='my-4' />
                {isAuthenticated ? null : loginButton}
            </div>
        </>
    );
}

export default Home;