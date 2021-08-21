import React, { Fragment } from "react";
import { Badge, Card, Dropdown } from "react-bootstrap";
const Home = () => {
	return (
		<div className="d-flex justify-content-center">
			<Card bg="dark" style={{ width: '57rem' }} className="mb-2" text="white">
				<Card.Body>
					<Card.Title>
						<h1 className="display-1">
							Hola, soy Carlos Vivar
						</h1>
						<h1 >
							<Badge pill bg="primary" >
								201801597
							</Badge>{' '}
						</h1>
					</Card.Title>
					<Card.Text >
						<br />
						<Card bg="dark" border="dark">
							<Card.Body>
								<h2>
									Este proyecto es realizado para el curso de
									<samp><var> Organizacion de Lenguajes
										y Compiladores 2
									</var>
									</samp>
									&thinsp;de la Carrera de Ingenieria de Ciencias y Sistemas en la Universidad de
									San Carlos de Guatemala,
								</h2>
							</Card.Body>
						</Card>
					</Card.Text>					
				</Card.Body>
			</Card>
		</div>
	);
}

export default Home;

