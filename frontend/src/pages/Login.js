import React from 'react';
import Cookies from 'js-cookie';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import CSRFToken from '../components/CSRFToken';

function Login({isAuthenticated, setIsAuthenticated}) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    // Attempts to log user in, which will start a session
    const login = async () => {

        let response = await fetch('http://127.0.0.1:8000/accounts/login', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": Cookies.get("csrftoken"),
              },
            body: JSON.stringify({
                username: username,
                password: password
            }),
            credentials: 'include'
        });        
        let data = await response.json();

        // If response contains the field 'success' then mark user as authenticated
        if (data.success) {
            setIsAuthenticated(true);
            navigate('/dashboard');
        } else {
            setIsAuthenticated(false);
            alert('Login failed. Ensure username and password are correct.')
        }
    }

    // Redirect if user already authenticated
    if (isAuthenticated) {
        navigate('/dashboard');
    }

    return (
        <>
            <div className='container mt-5'>
                <h3 className='mb-3'>Sign In</h3>

                <CSRFToken />
                <Form.Group className='mb-3' controlId='formBasicUsername'>
                    <Form.Label>Username</Form.Label>
                    <Form.Control 
                        type='text' 
                        placeholder='Username'
                        value={username}
                        onChange={e => setUsername(e.target.value)}
                         />
                </Form.Group>  

                <Form.Group className='mb-3' controlId='formBasicPassword'>
                    <Form.Label>Password</Form.Label>
                    <Form.Control 
                        type='password' 
                        placeholder='Password'
                        value={password}
                        onChange={e => setPassword(e.target.value)} />
                </Form.Group>  

                <Button 
                    variant='primary' 
                    type='submit'
                    onClick={login}>
                    Submit
                </Button>
            </div>
        </>
    );
}

export default Login;