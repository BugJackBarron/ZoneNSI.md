# Tout ceci ira dans un fichier _validation.py
from capytale.autoeval import Validate, ValidateVariables, ValidateFunction, ValidateFunctionPretty, validationclass
from random import shuffle, randint
import __main__

Validate().__call__()

@validationclass
class ValidateFunctionPrettyWithGiveUp(ValidateFunctionPretty) :
    def __init__(self, func_name, test_values, 
                 target_values=None, valid_function=None, 
                 argcount=None, check_signature=False, ignore_names_in_signature=False, **kwargs) :
        super().__init__(func_name, test_values, 
                       target_values, valid_function, argcount, 
                       check_signature, ignore_names_in_signature, **kwargs)
        
    def __call__(self) :
        success = super().__call__()
        if not(success) and self.trial_count() > 5 :
            rep = input("Voulez-vous abandonner la question ? (O/N)")
            if rep.lower() in ['o', 'oui', 'y', 'yes']:
                print("Abandon de la question")
                return True
            else :
                print("Poursuite de la question")
                return success
            
@validationclass
class ValidateVariablesWithGiveUp(ValidateVariables) :
    def __init__(self, names_and_values, **kwargs) :
        super().__init__(names_and_values, **kwargs)
        
    def __call__(self) :
        success = super().__call__()
        if not(success) and self.trial_count() > 5 :
            rep = input("Voulez-vous abandonner la question ? (O/N)")
            if rep.lower() in ['o', 'oui', 'y', 'yes']:
                print("Abandon de la question")
                return True
            else :
                print("Poursuite de la question")
                return success
            
@validationclass
class ValidateMatrixWithGiveUp(ValidateVariables):
    def __init__(self, names_and_values):
        super().__init__(names_and_values)
        

    def __call__(self):
        if not hasattr(__main__, self._values[0]) :
            print(f"Tu n'as pas défini de variable '{self._values[0]}''")
            success = False
        else :
            M = getattr(__main__, self._values[0])
            if M != self._targets[0] :
                print(f"Ta variable '{self._values[0]}' n'a pas la bonne valeur")
                success = False
            elif M[0] is M[1] :
                print("Attention, une matrice ne s'initialise pas comme une liste !")
                success = False
            else :
                print("Bravo")
                success = True
                
        if self.trial_count() > 5 :
            rep = input("Voulez-vous abandonner la question ? (O/N)")
            if rep.lower() in ['o', 'oui', 'y', 'yes']:
                print("Abandon de la question")
                return True
            else :
                print("Poursuite de la question")
                return success
        else :
            return success
        
        
        
        
test_exo1 = ValidateVariablesWithGiveUp({'liste_1' : [a ** 2 for a in range(0,26)]})
t1 = [n for n in range(-20, 20)]
shuffle(t1)
t2 = [n for n in range(-30, -5)]
shuffle(t2)
a = randint(-10, 10)
b = randint(-10, 10)
c = randint(-10, 10)
def f(x) :
    return a*x**2+b*x+c
t3 = [f(x) for x in range(-30, 30)]
shuffle(t3)
test_exo2 = ValidateFunctionPrettyWithGiveUp('get_max', ([5], t1, t2,  t3),
                                   target_values = [ 5, max(t1), max(t2), max(t3)])
test_exo3 = ValidateFunctionPrettyWithGiveUp('get_index_of_max', ([5], t1, t2,  t3),
                                   target_values = [ 0, t1.index(max(t1)), t2.index(max(t2)), t3.index(max(t3))])

nb_test = [randint(0,10), randint(-30,30), randint(-50, 0), f(randint(-40, 40))]
test_exo4 = ValidateFunctionPrettyWithGiveUp('is_in', (([5], nb_test[0]),
                                             (t1,nb_test[1]),
                                             (t2, nb_test[2]),
                                             (t3, nb_test[3])),
                                   target_values = [ nb_test[0] in [5],
                                                    nb_test[1] in t1,
                                                    nb_test[2] in t2,
                                                    nb_test[3] in t3])
def _my_get_over(liste : list, n : int) -> list :
    new_liste = []
    for elem in liste :
        if elem > n :
            new_liste.append(elem)
    return sorted(new_liste)

test_exo5 = ValidateFunctionPrettyWithGiveUp('get_over',(([5], nb_test[0]),
                                             (t1,nb_test[1]),
                                             (t2, nb_test[2]),
                                             (t3, nb_test[3])),
                                   valid_function=_my_get_over)

test_exo6 = ValidateVariablesWithGiveUp({'T' : [None]*10})



test_exo7 = ValidateMatrixWithGiveUp({'M':[[0]*6 for _ in range(7)]})

matrix_for_tests = [
    
    [[randint(0,255)]],
    [[randint(0,255)]*4 for _ in range(6)],
    [[randint(0,255)]*10 for _ in range(1)],
    [[randint(0,255)] for _ in range(8)],
    [[randint(0,255)]*4 for _ in range(4)]
]

def _my_count_lines(M : list)->int :
    return len(M)

def _my_count_columns(M : list)->int :
    return len(M[0])

def _my_negatif(M : list) -> list :
    lines, columns = len(M), len(M[0])
    new_matrix = [[0]*columns for _ in range(lines)]
    for x in range(lines) :
        for y in range(columns) :
            new_matrix[x][y] = 255 -M[x][y]
    return new_matrix
        

test_exo8 = ValidateFunctionPrettyWithGiveUp('count_lines', matrix_for_tests, valid_function = _my_count_lines)
test_exo9 = ValidateFunctionPrettyWithGiveUp('count_columns', matrix_for_tests, valid_function = _my_count_columns)
test_exo10 = ValidateFunctionPrettyWithGiveUp('negatif', matrix_for_tests, valid_function = _my_negatif)
