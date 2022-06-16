# Installation de Pyodide-mkdocs

Depuis [https://bouillotvincent.gitlab.io/pyodide-mkdocs/](https://bouillotvincent.gitlab.io/pyodide-mkdocs/){: target=_blank"}, suivre à la lettre le tutoriel.

Modifier `main.py` :

* ajouter `from math import log10`
* ajouter `MAX_EMPTY_IDE = 10` à `define_env`
* ajouter `import hashlib`
* dans `read_ext_file`, changer `docs_path = f"""docs"""`
* changement dans :
	
	```` python
	 path_file = '/'.join(filter(lambda folder: folder != "",
	convert_url_to_utf8(env.variables.page.abs_url).split('/')[1:-2])) #Changer le 2 en 1
	 ````
* changement dans 

	```` python
	if path == "":
		print(f"Try to open {docs_path}/{nom_script}.{filetype}") # suppression de /scripts/
		f = open(f"""{docs_path}/{nom_script}.{filetype}""")
	````