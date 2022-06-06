# Quelques REGEX


## Regex et Latex


* `\\textit{(.*?)}` : trouve  toute chaîne de caractère correspondant à `\textit{...}` et peut être remplacée par exemple par `?\1\?`, ce qui donnera :
	* `\textit{bidule}` ---> `?bidule?`
* `\\includegraphics[(.*?)]{(.*?)}` devrait permettre de faire	`[\2](\2)){: style="width:80%; margin:auto;display:block;background-color: #546d78;"}`, mais ça ne fonctionne pas.