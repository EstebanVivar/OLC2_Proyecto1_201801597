import React, { Fragment } from 'react';
import {

    BrowserRouter as Router,

    Switch,

    Route,

    useParams,

} from "react-router-dom";

import { Navbar, Nav, Container } from 'react-bootstrap';

const Navigation = () => {
    return (
        <Fragment>
            <Navbar collapseOnSelect sticky="top" expand='sm' bg='dark' variant='dark'>
                <Navbar.Brand href="#home">React Bootstrap Navbar</Navbar.Brand>
                <Navbar.Toggle aria-controls='responsive-navbar-nav' />
                <Navbar.Collapse id='responsive-navbar-nav'>
                    <Nav className="me-auto">
                        <Nav.Link href='/Bienvenida'>Bienvenida</Nav.Link>
                        <Nav.Link href="/Analisis">Analisis</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
            <br />
        </Fragment>
    );
}

export default Navigation;