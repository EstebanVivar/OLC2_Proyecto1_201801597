import React from 'react'
import { Table } from 'react-bootstrap';


const Symbols = () => {
    return (
        <div className="container  justify-content-center">
            <h1 style={{ color: "white" }}>Tabla de simbolos</h1>
            <Table striped bordered hover variant="dark">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Tipo</th>
                        <th>Entorno</th>
                        <th>Fila</th>
                        <th>Columna</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>x</td>
                        <td></td>
                        <td>Global</td>
                        <td>2</td>
                        <td>18</td>
                    </tr>

                </tbody>
            </Table>
        </div>
    );
}

export default Symbols;