import React from 'react';
import { Button, Card } from 'react-bootstrap';


const Reports = () => {
    return (
        <div class="container d-flex justify-content-center">
            <div className="row">
                <div className="col">
                    <Card bg="warning" text="white" style={{ height: '20rem' }}>
                        <Card.Header><h2>Reporte de Errores</h2></Card.Header>
                        <Card.Body>
                            <Card.Text>
                                <div className="container justify-content-center">
                                    <h5>Este reporte muestra los errores detectados durante el ultimo analisis.</h5>
                                </div>

                            </Card.Text>
                            <br/><br/>
                            <div className="container d-flex justify-content-center">
                                <Button variant="dark" href='/Errores'>
                                    Mostrar
                                </Button>
                            </div>
                        </Card.Body>
                    </Card>
                </div>
                <div className="col">
                    <Card bg="success" text="white" style={{ height: '20rem' }}>
                        <Card.Header><h2>Tabla de simbolos</h2></Card.Header>
                        <Card.Body>
                            <Card.Text>
                                <div className="container justify-content-center">
                                    <h5>Este reporte muestra los simbolos reconocidos y sus propiedades del ultimo analisis.</h5>
                                </div>

                            </Card.Text>
                            <br/>
                            <div className="container d-flex justify-content-center">
                                <Button variant="dark" href='/TablaSimbolos'>
                                    Mostrar
                                </Button>
                            </div>
                        </Card.Body>
                    </Card>
                </div>
                <div className="col">
                    <Card bg="danger" text="white" style={{ height: '20rem' }}>
                        <Card.Header><h2>Reporte AST</h2></Card.Header>
                        <Card.Body>
                            <Card.Text>
                                <div className="container justify-content-center">
                                    <h5>Este reporte muestra el arbol de analisis resultado del ultimo analisis.</h5>
                                </div>

                            </Card.Text>
                            <br/><br/>
                            <div className="container d-flex justify-content-center">
                                <Button variant="dark" >
                                    Mostrar
                                </Button>
                            </div>
                        </Card.Body>
                    </Card>
                </div>
            </div>
        </div>
    );
}

export default Reports;