import React, { Component } from 'react';
import logo from './navidad.svg';
import './App.css';
import {Card} from 'antd';
import { Row, Col } from 'antd';
import 'antd/dist/antd.css'
import styled from 'styled-components';

const Bienvenida = styled.div`
  color: rgb(134, 12, 12);
  font-size: 16px;
  margin-bottom: 20px;
`
const Body = styled.div`

  margin: 50px;

`

const MiTitulo = styled.div`
  color: white;
  font-size: 18px;
  margin: 5px;
`
const Subtitulo = MiTitulo.extend`
  font-size: 15px;
  margin: 5px;
`

const Division = Body.extend`
  margin: 0px;
`

class App extends Component {

  state = {
    data: []
  }

componentDidMount () {

fetch('http://3f3ab335.ngrok.io/api/v1/posadas/').then(res => res.json()).then((data) => {
    console.log('data', data)
    this.setState(() => ({ data }))
  })
}

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <MiTitulo>Mi Posadita</MiTitulo>
          <Subtitulo>Donde la verdadera magia sucede</Subtitulo>
        </header>
        <Body>
          <Bienvenida>
          Este espacio fue dedicado para poder ayudarte a mejorar la organización y participación en las posadas, esperemos te sea de gran utilidad!
          </Bienvenida>
          <Division>
            <Row>
              <Col span={8}>
                <Card style={{ width: 240 }} bodyStyle={{ padding: 0 }}>
                  <div className="custom-image">
                    <img alt="Evento posada 1" width="100%" src="http://blog.kiwilimon.com/wp-content/uploads/2014/12/recetas-para-posadas-de-navidad.jpg" />
                  </div>
                  <div className="custom-card">
                    <h3>Nombre de posada 1</h3>
                  <p>www.miposatida.com</p>
                  </div>
                </Card>
              </Col>
              <Col span={8}>
                <Card style={{ width: 240 }} bodyStyle={{ padding: 0 }}>
                  <div className="custom-image">
                    <img alt="Evento posada 1" width="100%" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />
                  </div>
                  <div className="custom-card">
                    <h3>Nombre de posada 1</h3>
                  <p>www.miposatida.com</p>
                  </div>
                </Card>
              </Col>
              <Col span={8}>
                <Card style={{ width: 240 }} bodyStyle={{ padding: 0 }}>
                  <div className="custom-image">
                    <img alt="Evento posada 1" width="100%" src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />
                  </div>
                  <div className="custom-card">
                    <h3>Nombre de posada 1</h3>
                  <p>www.miposatida.com</p>
                  </div>
                </Card>
              </Col>
            </Row>
          </Division>
        </Body>
      </div>
    );
  }
}

export default App;
