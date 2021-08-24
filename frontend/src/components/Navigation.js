import React, { Fragment } from 'react';


import { Navbar, Nav } from 'react-bootstrap';

const Navigation = () => {
    return (
        <Fragment>
            <Navbar collapseOnSelect sticky="top" style={{boxShadow: "0px 3px 10px rgba(0, 2, 8, 0.4)"}}  bg='primary' variant='dark'>
                <Navbar.Brand  style={{fontSize:"28px", fontWeight:"bolder"}} href="/Bienvenida">&nbsp;&nbsp;JOLC</Navbar.Brand>
                <Navbar.Toggle aria-controls='responsive-navbar-nav' />
                <Navbar.Collapse id='responsive-navbar-nav'>
                    <Nav className="me-auto">
                        <Nav.Link style={{fontSize:"20px"}} href="/Analisis">Analisis</Nav.Link>
                        <Nav.Link style={{fontSize:"20px"}} href="/Reportes">Reportes</Nav.Link>
                    </Nav>
                    
                </Navbar.Collapse>
            </Navbar>
            <br/>
        </Fragment>
    );
}

export default Navigation;