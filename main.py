from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/envia", methods=['GET','POST'])
def envia():
  dados = request.json
  #variavel = request.form['variavel']
  with open("dados.csv","a") as arquivo :
    arquivo.write("01"+","+str(dados["valor"])+'\n')
    arquivo.close
    return dados

@app.route("/cumprimento", methods=['GET','POST']) 
def babado():
  return "Oiie, amigo!! Seja bem vindo à minha API. Agora estamos conectados."


@app.route("/mediaNomes", methods=['GET','POST'])
def mediaNomes():

  data = {'name': ['Oliver', 'Harry', 'George', 'Noah'],
          'percentage': [90, 99, 50, 65],
          'grade': [88, 76, 95, 79]}
  df = pd.DataFrame(data)
  mean_df = df['grade'].mean()
  
  return (str(mean_df))


@app.route("/media", methods=['GET','POST'])
def media():

  with open("dados.csv","a") as arquivo :
    df = pd.DataFrame(arquivo)
    mean_df = df['valor'].mean()
  
    return (str(mean_df))



  # df = pd.DataFrame(data)
  #mean_df = df['grade'].mean()
  #print(df['grade'].describe())
  

    


# rodar a api
app.run(host='0.0.0.0')

# Código no postman
#{
  #  "sensor":"03" ,
 #   "valor":"200"

#}
