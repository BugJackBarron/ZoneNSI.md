# Quelques REGEX


## Regex et Latex


* `\\textit{(.*?)}` : trouve  toute chaîne de caractère correspondant à `\textit{...}` et peut être remplacée par exemple par `?\1\?`, ce qui donnera :
	* `\textit{bidule}` ---> `?bidule?`