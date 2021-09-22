import React, { Fragment, useState } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import 'codemirror/theme/material.css';
import { Button, Form } from 'react-bootstrap';
import axios from 'axios';



const Editor = () => {
    const [TextEditor, getEditor] = useState("");

    const [TextConsole, setConsole] = useState("");

    const getX = async (e) => {
        e.preventDefault();
        await axios
            .post("http://localhost:5000/Analisis", { input: TextEditor })
            .then(response => {
                if (response) {
                    console.log(response.data)
                    setConsole(response.data)
                }
            })
    }


    return (
        <Fragment>
            <Form onSubmit={getX}>
                    <div className="row">
                        <div className="col">
                            <h3 style={{ color: 'white' }}>
                                Editor de entrada
                            </h3>
                            <CodeMirror
                                value={TextEditor}
                                onChange={(v) => {
                                    getEditor(v.getValue())
                                }}
                                width="750px"
                                height="500px"
                                
                                options={{
                                    theme: 'material',
                                    mode: 'julia',
                                }}
                            />
                        </div>
                        
                <br />
                        <div className="col">
                            <h3 style={{ color: 'white' }}>Consola</h3>
                            <CodeMirror
                                value={TextConsole}
                                width="750px"
                                height="500px"
                                options={{
                                    lineNumbers: false,
                                    theme: 'material',
                                    mode: 'plain-text',
                                }}
                            />
                        </div>
                    </div>
                <br />
                <div className="container d-flex justify-content-center">
                    <div className="row">
                        <div className="col-6">
                            <Button type="submit">
                                <h3 style={{ color: 'white' }}>
                                    Analizar
                                </h3>
                            </Button>
                        </div>
                    </div>
                </div>
            </Form>
        </Fragment >
    );
}

export default Editor;