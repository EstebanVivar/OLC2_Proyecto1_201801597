import React, { Fragment } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import 'codemirror/theme/material.css';
import { Button } from 'react-bootstrap';

const Editor = () => {
    return (
        <Fragment>
            <div class="container">
                <div className="row">
                    <div className="col">
                        <h3 style={{ color: 'white' }}>Editor de entrada</h3>
                        <CodeMirror
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
                            width="545"
                            height="375px"
                            options={{
                                lineNumbers:false,
                                theme: 'material',
                                mode: 'plain-text',
                            }}
                        />
                    </div>
                </div>
            </div>
            <br/>
            <div class="container d-flex justify-content-center">
                <div className="row">
                    <div className="col-6">
                        <Button><h3 style={{ color: 'white' }}>Analizar</h3></Button>
                    </div>
                </div>
            </div>
        </Fragment >
    );
}

export default Editor;