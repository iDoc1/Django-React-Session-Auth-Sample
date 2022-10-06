import React from 'react';
import Cookies from 'js-cookie';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useNavigate } from 'react-router-dom';

function NavBar({isAuthenticated, setIsAuthenticated}) {
    const navigate = useNavigate();

    const logout = async () => {
        let response = await fetch('http://127.0.0.1:8000/accounts/logout', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": Cookies.get("csrftoken"),
            },
            credentials: 'include'
        });
        let data = await response.json();

        // If JSON data contains success field then set authentication to false
        if (data.success) {
            setIsAuthenticated(false);
            navigate('/');
        } else {
            alert("Error occurred while attempting to log out user.")
        }
    }

    // Links to show if user has not logged in
    const guestLinks = (
        <>
            <Nav.Link href='/login'>Login</Nav.Link>
            <Nav.Link href='/register'>Register</Nav.Link>
        </>
    );

    // Links to show if user has logged in
    const authLinks = (
        <>
            <Nav.Link href='/dashboard'>Dashboard</Nav.Link>
            <Nav.Link onClick={logout}>Logout</Nav.Link>
        </>
    );

    return (
        <>
            <Navbar bg='dark' variant='dark'>
                <Container>
                <Navbar.Brand href='/'>Session Auth</Navbar.Brand>
                <Nav className='me-auto'>
                    <Nav.Link href='/'>Home</Nav.Link>
                    {isAuthenticated ? authLinks : guestLinks}
                </Nav>
                </Container>
            </Navbar>
        </>
    );
}

export default NavBar;