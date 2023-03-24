with open("archivos\\lluvia.txt",'w',encoding="UTF-8") as archivo:
    #sobreescribir archivo
    #archivo.write("Dejo de llover")
    archivo.writelines(["Seguro llueve de nuevo\n","O sale el sol"])
    archivo.writelines(["\nQuiero descansar"])