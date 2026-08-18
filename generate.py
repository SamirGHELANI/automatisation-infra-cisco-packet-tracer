import yaml          
import os            
from jinja2 import Environment, FileSystemLoader   
 
env = Environment(
    loader=FileSystemLoader('templates'),    
    trim_blocks=True,        
    lstrip_blocks=True        
)

 
def generer_config(fichier_yaml):
     
    with open(fichier_yaml, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)     

    
    type_equipement = data['type']               
    template = env.get_template(f"{type_equipement}.j2")    

    
    config = template.render(data)     

    
    nom = data['hostname']                        
    os.makedirs('output', exist_ok=True)          
    chemin_sortie = f"output/{nom}.cfg"
    with open(chemin_sortie, 'w', encoding='utf-8') as f:
        f.write(config)

    print(f"✓ Config générée : {chemin_sortie}")

 
def generer_tout():
    for racine, dossiers, fichiers in os.walk('data'):    
        for fichier in fichiers:
            if fichier.endswith('.yaml'):
                chemin = os.path.join(racine, fichier)
                generer_config(chemin)

 
if __name__ == '__main__':
    generer_tout()
    print("Terminé !")