import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { Table } from 'react-bootstrap';

const Symbols = () => {
    const [simbols, updateSimbols] = useState([]);

    useEffect(() => {
        async function fetch() {
            await axios
                .post("http://localhost:5000/TablaSimbolos")
                .then(response => {
                    if (response) {
                        updateSimbols(response.data)
                    }
                })
        }
        fetch()
    }, [])

    return (
        <div className="container  justify-content-center">
            <h1 style={{ color: "white" }}>Tabla de simbolos</h1>
            <Table striped bordered hover variant="dark">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Entorno</th>
                        <th>Tipo</th>
                        <th>Fila</th>
                        <th>Columna</th>
                    </tr>
                </thead>
                <tbody>                   
                    {simbols.map(item => {
                        return (
                            <tr key={item.id}>

                                <td>{item.id}</td>
                                <td>{item.ambito}</td>
                                <td>{item.tipo}</td>
                                <td>{item.fila}</td>
                                <td>{item.columna}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </Table>
        </div>
    );
}

export default Symbols;