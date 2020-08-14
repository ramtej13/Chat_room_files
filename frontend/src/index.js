import React from "react";
import ReactDom from "react-dom";
import Chat from './container/chat';
import WebSocketInstance from './websocket';

class App extends React.Component {

    componentDidMount() {
        WebSocketInstance.connect();
    }
    render() {
        return (
            <Chat />
        )
    }
}

ReactDom.render(<App />, document.getElementById("app"));