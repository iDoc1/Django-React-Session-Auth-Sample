import React from 'react';
import Cookies from 'js-cookie';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import CSRFToken from '../components/CSRFToken';

function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [rePassword, setRePassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const navigate = useNavigate();

    const registerAccount = async () => {
        let response = await fetch('http://127.0.0.1:8000/accounts/register', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": Cookies.get("csrftoken"),
              },
            body: JSON.stringify({
                username: username,
                password: password,
                re_password: rePassword
            }),
            credentials: 'include'
        });        
        let data = await response.json();

        // Check if response object has either success or error fields
        if (data.success) {
            navigate('/login')
        } else if (data.error) {
            setErrorMessage(data.error);
        } else {
            alert("Error occured while creating account");
        }
    }

    return (
        <>
            <div className='container mt-5'>
                <h3 className='mb-3'>Register an Account</h3>

                <CSRFToken />
                <Form.Group className='mb-3' controlId='formBasicPassword'>
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

                <Form.Group className='mb-3' controlId='formBasicPassword'>
                    <Form.Label>Repeat Password</Form.Label>
                    <Form.Control 
                        type='password' 
                        placeholder='Repeat Password'
                        value={rePassword}
                        onChange={e => setRePassword(e.target.value)} />
                </Form.Group>

                <p><b>{errorMessage}</b></p>

                <Button 
                    variant='primary' 
                    type='submit'
                    onClick={registerAccount}
                    >
                    Submit
                </Button>
            </div>
        </>
    );
}

export default Register;