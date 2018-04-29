import yaml
import subprocess

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

#def yaml_dump(filepath, data):
#    """Dumps data to a yaml file"""
#    with open(filepath, "w") as file_descriptor:
#        yaml.dump(data, file_descriptor)
#        #print(data)

if __name__ == "__main__":
    filepath = "pipeline.yml"
    data = yaml_loader(filepath)

#data = yaml_loader(filepath)
#print(data['steps'][0]['execute'][0])
#print(data['tasks'][1])
print()

#Verifica quantos passos existem e qual é a ordem de execução
x=0
passos={}
for i in data['steps'][0]['execute']:
    passos[x]=data['steps'][0]['execute'][x]
    x+=1
    #print(passos)

#Procura a primeira instrução nos passos e executa
for i in range(0,x):
    if (str(data['tasks'][0]).find(passos[i]) ==-1):
        print()
    else:
        print("executando:",data['tasks'][i])
        cmd = str(data['tasks'][i])
        #print(cmd[21:52])
        r = subprocess.call(cmd[21:52], shell=True)
        #proc = subprocess.Popen (cmd[21:52], shell=True,stdout=subprocess.PIPE).stdout.read()
        print()

#Procura a segunda instrução nos passos e executa
for i in range(0,x):
    if (str(data['tasks'][1]).find(passos[i]) ==-1):
        print()
    else:
        print("executando:", data['tasks'][i])
        cmd = str(data['tasks'][i])
        #print(cmd[19:69])
        r = subprocess.call(cmd[19:69], shell=True)
        #proc = subprocess.Popen (cmd[19:69], shell=True,stdout=subprocess.PIPE).stdout.read()
        print()


   




#print(yaml.dump(data.get('tasks'), default_flow_style=False))
#print(yaml.dump(data.get('steps'), default_flow_style=False))
    