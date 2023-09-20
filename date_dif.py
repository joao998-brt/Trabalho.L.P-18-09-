import datetime

def diferenca_date_console():
    
    entrada = input("Digite as datas no formato 'dia de mês de ano': ")
    #data1, data2 = entrada.split(" - ")
   # diferenca_days = abs((data2 - data1).days)
    #return data1.strip(), data2.strip()
    #return diferenca_days
    #convertendo as datas
    data1_str, data2_str = entrada.split(" - ")

    data1 = datetime.strptime(data1_str, "%d de %B de %Y")
    data2  = datetime.strptime(data2_str, "%d de %B de %Y")
    
    return data2 - data1

def diferenca_date_arquivo(datas_arquivo):
    with open(datas_arquivo, "r", encoding="utf-8") as file:
        conteudo = file.read()
        data1_str, data2_str = conteudo.split(" - ")
    return data1_str.strip(), data2_str.strip()
    
