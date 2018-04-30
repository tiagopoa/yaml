import yaml
import subprocess
import time

hoje = "%s" % (time.strftime("%Y%m%d"))

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def pipeline_executor(data):
    #Verifica quantos passos existem e armazena qual é a ordem de execução
    x=0
    passos={}
    for i in data['steps'][0]['execute']:
        passos[x]=data['steps'][0]['execute'][x]
        x+=1

    #Procura as instruções e as executa na ordem correta.
    for i in range(0,x):
        for j in range(0,x):
            if (str(data['tasks'][j]).find(passos[i])==-1):
                print()
            else:
                arquivo = open("ci_script.%s.log" % (hoje), "a")
                hora = time.strftime("%H:%M:%S")
                cmd = (data.get('tasks')[j][passos[i]]['cmd'])
                print("Iniciando execução do comando",cmd,"aguarde...")
                arquivo.write("[%s]Iniciando execução do comando [%s] aguarde...\r\n" % (hora,cmd))
                print()            
                try:
                    subprocess.check_output(cmd, shell=False)                 
                except subprocess.CalledProcessError as e:
                    print()
                    print ("Erro:",e.output)
                    arquivo.write("[%s] Erro: [%s]\r\n" % (hora,e.output))
                print()
                print("Execução do comando",cmd,"finalizado.")
                arquivo.write("[%s] Execução do comando [%s] finalizado.\r\n" % (hora,cmd))
                print()
                arquivo.close()

if __name__ == "__main__":
    filepath = "pipeline.yml"
    data = yaml_loader(filepath)
    pipeline_executor(data)

