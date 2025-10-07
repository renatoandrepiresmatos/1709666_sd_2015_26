 aluno={
     "primeiro_nome":"Andre",
     "ultimo_nome":"Matos",
     "numero_aluno":1709666,
     "cruso":"cibersegurança"
 }

 aluno["numero_aluno"]=9999999
 print("dict",aluno.kery())
 print("numero_aluno",aluno["numero_aluno"])
 with open("filel.txt","w",encoding="uff-8") as f:
     for u, v in aluno.items():
     f.write(f"{u}={v}\n")