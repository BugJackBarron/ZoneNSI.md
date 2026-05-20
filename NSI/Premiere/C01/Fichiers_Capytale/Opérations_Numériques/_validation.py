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
            
        
        
    

test_exo1 = ValidateAnswers({"Quel est le nombre associé à la variable `c` ?" : ['15'],
                             "Quel est le nombre associé à la variable `d` ?" : ['2'],
                             "Quel est le nombre associé à la variable `e` ?" : ['225'],
                             "Quel est le nombre associé à la variable `f` ?" : ['243'],
                             "Quel est le nombre associé à la variable `g` ?" : ['7.5'],
                             "Quel est le nombre associé à la variable `h` ?" : ['7'],
                             "Quel est le nombre associé à la variable `i` ?" : ['1'],
                            }, strict=True)
test_exo2 = ValidateAnswers({"Les variables `a` et `c` sont elles égales ?" : ['n', 'no', 'non'],})
test_exo3 = ValidateAnswers({"Donnez la valeur de `113 // 5` :" : ['22'],
                             "Donnez la valeur de `113 % 5` :" : ['3'],
                             "Donnez la valeur de `113 / 5` :" : ['22.6'],
                            }, strict=True)
test_exo4 = ValidateAnswers({"Tapez l'expression équivalente :" : ['3+4*5**3']
                            }, strict=True)
test_exo5 = ValidateAnswers({"Tapez l'expression équivalente :" : ['1/7+4-(3/5+2)']
                            }, strict=True)
test_exo6 = ValidateAnswers({"Tapez l'expression équivalente :" : ['(5+3**4)/6']
                            }, strict=True)
test_exo7 = ValidateAnswers({"Tapez l'expression équivalente :" : ['1/(1+1/2)']
                            }, strict=True)
test_exo8 = ValidateAnswers({"Donnez la valeur associée à `a` ?" : ["16"]})