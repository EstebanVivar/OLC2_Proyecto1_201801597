import React, { Fragment, useState } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import 'codemirror/theme/material.css';
import { Button, Form } from 'react-bootstrap';



const Editor = () => {
    const [TextEditor, getEditor] = useState("");

    const [TextConsole, setConsole] = useState("");
   
    const getX = e => {
        e.preventDefault();
        setConsole(TextEditor);
        
    }

    return (
        <Fragment>
            <Form onSubmit={getX}>
                <div className="container">
                    <div className="row">
                        <div className="col">
                            <h3 style={{ color: 'white' }}>Editor de entrada</h3>
                            <CodeMirror
                                value={TextEditor}
                                onChange={(v) => {                                      
                                    getEditor(v.getValue())
                                }}
                                width="545px"
                                height="375px"
                                options={{
                                    theme: 'material',
                                    mode: 'julia',
                                }}
                            />
                        </div>
                        <div className="col">
                            <h3 style={{ color: 'white' }}>Consola</h3>
                            <CodeMirror
                                value={TextConsole}
                                width="545"
                                height="375px"
                                options={{
                                    lineNumbers: false,
                                    theme: 'material',
                                    mode: 'plain-text',
                                }}
                            />
                        </div>
                    </div>
                </div>
                <br />
                <div className="container d-flex justify-content-center">
                    <div className="row">
                        <div className="col-6">
                            <Button type="submit"><h3 style={{ color: 'white' }}>Analizar</h3></Button>
                        </div>
                    </div>
                </div>
            </Form>
        </Fragment >
    );
}

export default Editor;