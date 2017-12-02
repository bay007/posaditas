#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from respuestas import Respuestas

app = Flask(__name__)

ACCESS_TOKEN = 'EAAB5j6rfxGcBAB0oujL4hPOoNyyAU2V7463p506ynKAUDGNNegKdyUOQFu60ZAiPlHZBUcWJvCYo6fZANKtuLzCXbex3b8Hv2ZAZBZCtdAtyP8Pn41weCJ3kGLANvf4TzV1MQ3ha6qpXrt6dMCdfnVwGogEwW76ZBaow78ZBLmSbywZDZD'
VERIFY_TOKEN = 'cintaroja'
@app.route('/')
def home():
	return 'Inicio del servidor'

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	if request.method == 'POST':
		mensaje = request.json
		print(mensaje)

		for event in mensaje['entry']:
			messaging = event ['messaging']
			for event_message in messaging:
				sender_id = event_message['sender']['id']
				try:
					message = event_message['message']['text']
					pln = event_message['message']['nlp']['entities']['intent'][0]['value']
				except:
					message = "HOLA"

				print(message + 'por' + sender_id + " " + str("nlp"))
				respuestas = Respuestas()

				if message.upper() == 'HOLA':
					respuestas.saluda(sender_id)
				elif message.upper() == 'QUICK':
					respuestas.quick(sender_id)
				elif message.upper() == 'GENERIC':
					respuestas.generic(sender_id)
				elif pln.upper() == 'QUIERO':
					r = requests.get('http://3f3ab335.ngrok.io/api/v1/posadas/')
					respuestas.pln(sender_id, r.json())



		return 'ok'
	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return 'Verificar token'


if __name__ == '__main__':
	app.run(port = 5000, debug = True)