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
	
* Plein de hacks pour les boutons :

	```` pythonlen_path = len(convert_url_to_utf8(env.variables.page.abs_url).split('/'))
        fix_url = env.macros.fix_url
        if len_path> 1 :
            path_img = "/"+'../'*(len(convert_url_to_utf8(env.variables.page.abs_url).split('/'))-3)
        else : 
            path_img =""
        if '127.0.0.1' not in env.variables.config['site_url'] :
            path_img = fix_url(path_img)
        path_file = '/'.join(filter(lambda folder: folder != "", 		convert_url_to_utf8(env.variables.page.abs_url).split('/')[1:-2]))
	````
	
	et 
	
	```` python
	div_edit += tooltip_button(f"""'interpretACE("editor_{tc}","{mode}")'""", f"""<img src="{path_img}images/buttons/icons8-play-64.png"><span class="tooltiptext">Lancer</span>""")
        div_edit += create_unittest_button(tc, nom_script, path_file, mode, MAX) + blank_space(1)
        div_edit += tooltip_button(f"""\'downloadFile("editor_{tc}","{nom_script}")\'""", f"""<img src="{path_img}images/buttons/icons8-download-64.png"><span class="tooltiptext">Télécharger</span>""")+ blank_space()
        div_edit += create_upload_button(tc) + blank_space(1)
        div_edit += tooltip_button(f"""\'reload("{tc}")\'""", f"""<img src="{path_img}images/buttons/icons8-restart-64.png"><span class="tooltiptext">Recharger</span>""") + blank_space()
        div_edit += tooltip_button(f"""\'saveEditor("{tc}")\'""", f"""<img src="{path_img}images/buttons/icons8-save-64.png"><span class="tooltiptext">Sauvegarder</span>""")
        div_edit += '</div>'
	````
	
	{-- NE PAS OUBLIER DE CHANGER POUR TESTS ET UPLOAD --}