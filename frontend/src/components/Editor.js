import React, { Fragment } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import 'codemirror/theme/monokai.css';
import { Button } from 'react-bootstrap';

const Editor = () => {
    return (
        <Fragment>
            <div class="container">
                <div className="row">
                    <div className="col">
                        <h1>Editor de entrada</h1>
                        <CodeMirror
                            value="code"
                            width="545px"
                            height="400px"
                            options={{
                                theme: 'monokai',
                                mode: 'jsx',
                            }}
                        />
                    </div>
                    <div className="col">
                        <h1>Consola</h1>
                        <CodeMirror
                            value="code"
                            width="545"
                            height="400px"
                            options={{
                                theme: 'monokai',
                                mode: 'jsx',
                            }}
                        />
                    </div>
                </div>
            </div>
            <br/>
            <div class="container d-flex justify-content-center">
                <div className="row">
                    <div className="col-6">
                        <Button><h3>Analizar</h3></Button>
                    </div>
                </div>
            </div>
        </Fragment >
    );
}

export default Editor;