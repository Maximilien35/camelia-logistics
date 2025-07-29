import os
dossier='/home/jocker/camelia/image'
extensions=[".jpeg",".jpg",".png",".gif",".bmp"]
comp=1
for fichier in os.listdir(dossier):
    if os.path.splitext(fichier)[1].lower()in extensions:
        nouveau_nom=f"image{comp}{os.path.splitext(fichier)[1]}"
        os.rename(os.path.join(dossier,fichier),os.path.join(dossier,nouveau_nom))
        comp+=1