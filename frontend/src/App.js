import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Register from './pages/Register';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/ProtectedRoute';


function App() {
    const [isAuthenticated, setIsAuthenticated] = useState(true);

    // Checks if the current user is already logged in and sets state accordingly
    const checkAuthenticated = async () => {
        let response = await fetch('http://127.0.0.1:8000/accounts/authenticated', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
              },            
            credentials: 'include'
        });
        let data = await response.json();

        if (data.is_authenticated === 'success') {
            setIsAuthenticated(true);
        } else {
            setIsAuthenticated(false);
        }
    }

    // Check authentication any time the app is loaded
    useEffect(() => {
        checkAuthenticated();
    }, []);


    return (
        <>
            
            <Router>
                <NavBar 
                    isAuthenticated={isAuthenticated}
                    setIsAuthenticated={setIsAuthenticated} />
                <Routes>

                    <Route exact path='/' element={
                        <Home isAuthenticated={isAuthenticated} />} />
                    <Route exact path='/register' element={<Register />} />
                    <Route exact path='/login' element={
                        <Login 
                            isAuthenticated={isAuthenticated} 
                            setIsAuthenticated={setIsAuthenticated} />} />
                    <Route exact path='/dashboard' element={
                        <ProtectedRoute isAuthenticated={isAuthenticated}>
                            <Dashboard />
                        </ProtectedRoute>
                    } />
                    
                </Routes>
            </Router>
        </>
    );
}

export default App;
