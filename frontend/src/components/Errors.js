import React from 'react'
import { Table } from 'react-bootstrap';

import { obtenerFecha } from './helper';


const Errors = () => {



    return (

        <div className="container  justify-content-center">
            <h1 style={{ color: "white" }}>Reporte de errores</h1>
            <Table striped bordered hover variant="dark">
                <thead>
                    <tr>
                        <th>No.</th>
                        <th>Descripcion</th>
                        <th>Linea</th>
                        <th>Columna</th>
                        <th>Fecha y Hora</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Prueba</td>
                        <td>0</td>
                        <td>0</td>
                        <td>{obtenerFecha()}</td>
                    </tr>

                </tbody>
            </Table>
        </div>
    );
}

export default Errors;