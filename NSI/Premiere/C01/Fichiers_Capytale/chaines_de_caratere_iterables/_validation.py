from capytale.autoeval import Validate, ValidateVariables, ValidateFunction, ValidateFunctionPretty, validationclass
from random import shuffle, randint
import __main__
import sys

Validate().__call__()

@validationclass    
class ValidateVariablesWithTypeAndGiveUp(ValidateVariables) :
    def __init__(self, names_and_values, **kwargs) :
        super().__init__(names_and_values, **kwargs)
        
        
    def handle_full_success(self):
        pass
    
    def handle_failure(self, value, target, result) -> bool:
        print(f"Ta variable '{value}' n'est soit pas du bon type ({type(target)}), soit n'a pas la bonne valeur({result} != {target}).", file=sys.stderr,
        )
        
    def __call__(self):
        success = super().__call__()
        if success :
            for value, target in zip(self._values, self._targets) :
                # value : nom de variable
                # target : valeur cible
                M = getattr(__main__, value)
                # M : valeur de associée à la variable value
                if type(M) != type(target) :
                    self.handle_failure(value, target, M)
                    success = False
        if success :
            if len(self._values) > 1:
                print("👏 Bravo, tes variables sont bien définies !")
            elif len(self._values) == 1:
                print(f"👏 Bravo, ta variable '{self._values[0]}' est bien définie !")
        if not(success) and self.trial_count() > 5 :
             print("Il faudrait demander un peu d'aide au professeur ou à tes camarades !", file=sys.stderr)
        return success
    
@validationclass
class ValidateAnswers(ValidateVariables) :
    def __init__(self, names_and_values, **kwargs):
        super().__init__(names_and_values)
        self.questions = names_and_values
        if 'strict' in kwargs :
            self.strict = kwargs['strict']
        else :
            self.strict = False
        
    def handle_failure(self, answer) -> bool:
        print(
            f"Ta réponse '{answer}' n'est pas correcte. Soit tu te trompes, soit ton orthographe n'est pas correcte",
            file=sys.stderr,
        )
        if self.trial_count() > 5 :
             print("Il faudrait demander un peu d'aide au professeur ou à tes camarades !", file=sys.stderr)
        return False

    def handle_exception(self, exc, question) -> bool:
        print(
            f"Une erreur {exc} a été levée dans la réponse à la question {question}",
            file=sys.stderr,
        )
        return False

    def handle_full_success(self):
        if len(self._values) > 1:
            print("👏 Bravo, tu as répondu correctement à toutes les questions !")
        elif len(self._values) == 1:
            print(f"👏 Bravo, ta réponse est correcte !")
            
    def __call__(self) :
        for question in self.questions :
            try :
                ans = input(question).strip()
                if not(self.strict) :
                    ans=ans.lower()
                if ans not in self.questions[question]:
                    return self.handle_failure(ans)
            except Exception as ex :
                return self.handle_exception(ex, question)
        self.handle_full_success()
        
        return True
            
        
test_exo1_1 = ValidateVariables({"texte1" : "Hello World !"})
test_exo1_2 = ValidateVariables({"texte2" : "Hello World !".upper()})

from string import printable
base = " "*10000
phrase = "Il n'y a plus de mystère ! La chaine de caractère que vous devez donner en réponse à la question est :'Ada Lovelace et Alan Turing' ! N'oubliez pas les guillemets ou les apostrophes !".replace(" ", "_")
mystere = base.join(phrase)

magie = ["Abracadabra"[:i] for i in range(len("Abracadabra")+1)]
magie_stable = ["Abracadabra"[:i] for i in range(len("Abracadabra")+1)]

test_exo2 = ValidateAnswers({
    "Quelle est la longueur de la chaine associée à la varibale mystere ?" : ["1820183", "1 820 183"]})
test_exo3 = ValidateAnswers({"Quelle est le caractère d'indice 100 010 de la variable mystere ?" : ["l"]}, strict = True)
test_exo4 = ValidateVariables({"petit_mystere" : mystere.replace(" ","")})
test_exo5 = ValidateVariables({"petit_mystere" : mystere.replace(" ","").replace("_"," ")})
test_exo6 = ValidateAnswers({"Donnez la chaine réponse " : ["'Ada Lovelace et Alan Turing'", '"Ada Lovelace et Alan Turing"']}, strict = True)
test_exo7 = ValidateVariables({"ma_liste" : [2**2, 3**2, 5**2, 7**2, 11**2]})
test_exo8 = ValidateVariables({"mon_tuple" : (1**2, 3**2, 5**2, 7**2, 9**2)})
test_exo9 = ValidateAnswers({"Peut on ajouter un élément à ma_liste" :['y', 'yes', 'o', 'oui'],
                             "Peut on ajouter un élément à mon_tuple" :['n', 'no', 'non']})
test_exo10 = ValidateVariables({"ma_liste" : [2**2, 3**2, 5**2, 7**2, 11**2, 13**2]})                          

test_exo11 = ValidateAnswers({
    "Combien d'éléments y-a-t'il dans la liste magie" : ["12"]})
test_exo12 = ValidateAnswers({
    "Quel est l'élément d'indice 5 de la liste magie ?" : ["'Abrac'", '"Abrac"']}, strict=True)
test_exo13 = ValidateVariables({"magie" : magie_stable[:-1]})                          
test_exo14 = ValidateVariables({"magie" : ['Bravo !'] + magie_stable[1:-1]})                          


