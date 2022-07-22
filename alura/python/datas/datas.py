from datetime import datetime, timedelta

class Datas:

    def __init__(self):
        self.timestamp = datetime.today()

    def mes(self):
        meses = [
        'janeiro', 'fevereiro',  'março'  ,
        'abril'  ,   'maio'   ,  'junho'  ,
        'julho'  ,  'agosto'  , 'setembro',
        'outubro', 'novembro' , 'dezembro'
        ]
        mes = self.timestamp.month
        return meses[mes-1]
    
    def dia_da_semana(self):   
        semana = [
            'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'
        ]
        dia = self.timestamp.weekday()
        return semana[dia]
        