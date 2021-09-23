

import React, { useEffect, useState } from 'react';
import { Card } from 'react-bootstrap';
import { Graphviz } from 'graphviz-react';
import axios from 'axios';

const Graph = () => {
    const [grafo, updateGrafo] = useState(`graph {}`);
    useEffect(() => {
        async function fetch() {
            await axios
                .post("https://quiet-springs-28392.herokuapp.com/AST")
                .then(response => {
                    if (response) {
                        console.log(response.data)
                        updateGrafo(response.data)
                    }
                })
        }
        fetch()

    })
    const Options = {
        height: 74 + "vh",
        width: 82 + "vw",
        scale: 1,
        engine: 'dot',
        fit: true,
        zoom: true,
    };
    return (


        <div className="container">
            <Card bg="danger" text="white" style={{ height: '87vh' }}>
                <Card.Header><h2>Reporte AST</h2></Card.Header>
                <Card.Body>
                    <Graphviz options={Options} dot={grafo} />
                </Card.Body>
            </Card>
        </div>


    );
}

export default Graph;