import requests

class Respuestas():
	def saluda(self,sender_id):
		JSON = {"messaging_type": "RESPONSE",
		"recipient":{
  		"id":sender_id
		},
		"message":{
  		"text":"Ahí nos vemos :)"
			}
		}

		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAB5j6rfxGcBAB0oujL4hPOoNyyAU2V7463p506ynKAUDGNNegKdyUOQFu60ZAiPlHZBUcWJvCYo6fZANKtuLzCXbex3b8Hv2ZAZBZCtdAtyP8Pn41weCJ3kGLANvf4TzV1MQ3ha6qpXrt6dMCdfnVwGogEwW76ZBaow78ZBLmSbywZDZD'
		respuesta = requests.post(URL,json = JSON)
		return respuesta



	def pln(self,sender_id, lista_response):

		elementos = []
		for valores in lista_response:

			x = {'title': valores['nombre'],
			'image_url': valores['imagen_posada'],
			'subtitle': valores['fecha'],
			'buttons':[{'type': 'postback', 'title':'Confirma asistencia', 'payload': 220}]
			}
			elementos.append(x)

		JSON = {
  		"recipient":{
    	"id":sender_id,
    },
      "message":{
      "attachment":{
        "type":"template",
        "payload":{
        "template_type":"generic",
        "elements":elementos
              }
          }
        }
    }
  	

		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAB5j6rfxGcBAB0oujL4hPOoNyyAU2V7463p506ynKAUDGNNegKdyUOQFu60ZAiPlHZBUcWJvCYo6fZANKtuLzCXbex3b8Hv2ZAZBZCtdAtyP8Pn41weCJ3kGLANvf4TzV1MQ3ha6qpXrt6dMCdfnVwGogEwW76ZBaow78ZBLmSbywZDZD'
		respuesta = requests.post(URL,json = JSON)
		return respuesta

		

