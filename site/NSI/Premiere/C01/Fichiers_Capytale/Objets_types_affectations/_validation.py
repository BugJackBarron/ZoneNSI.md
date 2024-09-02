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
        success = True
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
            
        
        
    

test_exo1 = ValidateVariablesWithTypeAndGiveUp({'a' : 5})
test_exo2 = ValidateVariablesWithTypeAndGiveUp({'b' : 3.2})
test_exo3 = ValidateVariablesWithTypeAndGiveUp({'bob' : "Bob", 'bill' : "BOB"})
test_exo4 = ValidateAnswers({"Quel est le type de la variable 'toto' ?":['str', 'string', 'chaine', 'chaine de caractères'],
                             "Quel est le type de la variable 'tata' ?":['int', 'entier'],
                             "Quel est le type de la variable 'tutu' ?":['int', 'entier'],
                            })
test_exo5 = ValidateAnswers({"La variable `toto` est-elle bien définie ?":['n', 'non', 'no']})
mystere = False
test_exo6 = ValidateAnswers({'Quel est le type de `mystere` ?' : ['bool', 'boolean', 'booléen', 'booleen'],
                             'Quel est la valeur de `mystere` ?' : ['False'],
                            }, strict = True)
test_exo7 = ValidateAnswers({"De quel type est la variable `intrigue` ? " : ['float', 'flottant', 'flottante']})