import date_dif as dt
from datetime import datetime

# recebendo as datas pelo console e convertendo
date1 = input("digite uma data: ")
print("a data digitada foi" , date1 , " digite outra data ")
date2 = input()
print("as datas digitadas foram: " , date1, "e",date2)  

data_1  = datetime.strptime(date1, "%d de %B de %Y")
data_2  = datetime.strptime(date2, "%d de %B de %Y")

dt.diferenca_date(data_1, data_2)
print(" a número de dias entre as datas é: ", dt.diferenca_date(data_1, data_2))

# recebendo por arquivo de texto 
