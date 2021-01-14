import numpy as np
import pandas as pd

arquivo = pd.read_csv("testedt.csv")
ignore=[]
referencia = dict()
tabelas_lb=[("Medias","mean",4),
            ("Melhores","min",3),
            ("Medianas","median",6)]


f = open("tabela.html", "w")
f.write("<html>")
f.write("<head><link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"></head>")
f.write("<body>")
f.write("<h3>Tabela geral</h3>")
f.write("<table class=\"fixed\">")
f.write("<tr>")
for i in arquivo:
    if np.max(arquivo[i].iloc[1:])!=-1:
        if i!='Unnamed: 0':
            f.write("<th>"+i+"</th>")
        else:
            f.write("<th> </th>")
        if i!='alg' and i!='Unnamed: 0':
            rvec = list(arquivo[i])
            while -1 in rvec:
                rvec.remove(-1)
            if i[-2:]=="sr":
                referencia[i]=(np.max(rvec),arquivo[i].iloc[0],np.min(rvec))
            else:
                referencia[i]=(np.min(rvec),arquivo[i].iloc[0],np.max(rvec))
    else:
        ignore.append(i)
f.write("</tr>")
for i in range(len(arquivo.index)):
    f.write("<tr>")
    for j in arquivo:
        if j not in ignore:
            f.write("<td>")
            if j!='alg' and j!='Unnamed: 0':
                if arquivo[j].iloc[i]==referencia[j][0]:
                    #Melhor resultado
                    f.write("<b>")
                if i>0:
                    if arquivo[j].iloc[i] != -1:
                        if j[-2:]=="sr":
                            if arquivo[j].iloc[i]>=referencia[j][1]:
                                #taxa de sucesso melhor que a ref
                                f.write("<p style=\"color:blue\">")
                        else:
                            if arquivo[j].iloc[i]<=referencia[j][1]:
                                f.write("<p style=\"color:blue\">")
                    if arquivo[j].iloc[i]==referencia[j][2] and arquivo[j].iloc[i]!=referencia[j][0]:
                        #Pior resultado
                        f.write("<p style=\"color:red\">")
            if arquivo[j].iloc[i] != -1:
                if j[-3:]=='std':
                    f.write(str("{:.2e}".format(arquivo[j].iloc[i])))
                elif j[-4:]=='mean':
                    f.write(str(round(arquivo[j].iloc[i],2)))
                else:
                    f.write(str(arquivo[j].iloc[i]))
            else:
                f.write(" ")
            if j!='alg' and j!='Unnamed: 0':
                if arquivo[j].iloc[i] != -1:
                    if arquivo[j].iloc[i]==referencia[j][0]:
                        #Melhor resultado
                        f.write("</b>")
                    if i>0:
                        if j[-2:]=="sr":
                            if arquivo[j].iloc[i]>=referencia[j][1]:
                                #taxa de sucesso melhor que a ref
                                f.write("</p>")
                        else:
                            if arquivo[j].iloc[i]<=referencia[j][1]:
                                f.write("</p>")
                    if arquivo[j].iloc[i]==referencia[j][2] and arquivo[j].iloc[i]!=referencia[j][0]:
                        #Pior resultado
                        f.write("</p>")
                f.write("</td>")
    f.write("</tr>")
            
                
for k in tabelas_lb:
    f.write("</table>")
    f.write("<h3>"+k[0]+"</h3>")
    f.write("<table class=\"fixed\">")
    f.write("<tr>")
    for i in arquivo:
        if i not in ignore:
            if i[-k[2]:]==k[1]:
                f.write("<th>"+i[:-k[2]]+"</th>")
            elif i=='alg':
                f.write("<th>"+i+"</th>")
            elif i=='Unnamed: 0':
                f.write("<th> </th>")
    f.write("</tr>")
    for i in range(len(arquivo.index)):
        f.write("<tr>")
        for j in arquivo:
            if j not in ignore:
                if j[-k[2]:]==k[1] or j=='alg' or j=='Unnamed: 0':
                    f.write("<td>")
                    if j!='alg' and j!='Unnamed: 0':
                        if arquivo[j].iloc[i]==referencia[j][0]:
                            #Melhor resultado
                            f.write("<b>")
                        if i>0:
                            if arquivo[j].iloc[i] != -1:
                                if j[-2:]=="sr":
                                    if arquivo[j].iloc[i]>=referencia[j][1]:
                                        #taxa de sucesso melhor que a ref
                                        f.write("<p style=\"color:blue\">")
                                else:
                                    if arquivo[j].iloc[i]<=referencia[j][1]:
                                        f.write("<p style=\"color:blue\">")
                            if arquivo[j].iloc[i]==referencia[j][2] and arquivo[j].iloc[i]!=referencia[j][0]:
                                #Pior resultado
                                f.write("<p style=\"color:red\">")
                    if arquivo[j].iloc[i] != -1:
                        if j[-3:]=='std':
                            f.write(str("{:.2e}".format(arquivo[j].iloc[i])))
                        elif j[-4:]=='mean':
                            f.write(str(round(arquivo[j].iloc[i],2)))
                        else:
                            f.write(str(arquivo[j].iloc[i]))
                    else:
                        f.write(" ")
                    if j!='alg' and j!='Unnamed: 0':
                        if arquivo[j].iloc[i] != -1:
                            if arquivo[j].iloc[i]==referencia[j][0]:
                                #Melhor resultado
                                f.write("</b>")
                            if i>0:
                                if j[-2:]=="sr":
                                    if arquivo[j].iloc[i]>=referencia[j][1]:
                                        #taxa de sucesso melhor que a ref
                                        f.write("</p>")
                                else:
                                    if arquivo[j].iloc[i]<=referencia[j][1]:
                                        f.write("</p>")
                            if arquivo[j].iloc[i]==referencia[j][2] and arquivo[j].iloc[i]!=referencia[j][0]:
                                #Pior resultado
                                f.write("</p>")
                        f.write("</td>")
        f.write("</tr>")

    f.write("</table>")
f.write("</body>")
f.write("</html>")
f.close()
