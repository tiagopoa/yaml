import yaml
import subprocess

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

if __name__ == "__main__":
    filepath = "pipeline.yml"
    data = yaml_loader(filepath)
print()

#Verifica quantos passos existem e qual é a ordem de execução
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
            cmd = (data.get('tasks')[j][passos[i]]['cmd'])
            print("Iniciando execução do comando",cmd,"aguarde...")
            print()            
            try:
                output = subprocess.check_output(cmd, shell=False)                
            except subprocess.CalledProcessError as e:
                print()
                print ("Erro:",e.output)
            print()
            print("Processo",cmd,"finalizado.")
            print()