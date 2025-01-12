#!/bin/bash

rm -f test/q/commencement.txt
touch test/q/commencement.txt
echo "La suite se trouve dans s/u/i" > test/q/commencement.txt

rm -f test/s/u/i/c_est_la.txt
touch test/s/u/i/c_est_la.txt
echo "le chemin à suivre est dans un des sous-dossier du dossier actuel, et est dans un fichier txt" > test/s/u/i/c_est_la.txt

rm -f test/s/u/i/p/bravo.txt
touch test/s/u/i/p/bravo.txt
echo "Pour continuer, vous devrez d'abord créer un fichier nommé bob_is_here.txt dans le répertoire a/t/e/r, puis exécuter le fichier is_bob_here.sh situé dans le même dossier, grâce à la commande bash is_bob_here.sh." > test/s/u/i/p/bravo.txt

rm -f test/a/t/e/r/is_bob_here.sh
rm -f test/i/c/i/Bill.txt
touch test/a/t/e/r/is_bob_here.sh
echo "FILE=bob_is_here.txt" > test/a/t/e/r/is_bob_here.sh
echo "if [ -f \"\$FILE\" ]; then" >> test/a/t/e/r/is_bob_here.sh
echo "echo \"Bob est là ! Mais ou se trouve Bill.txt ?\"" >> test/a/t/e/r/is_bob_here.sh
echo "touch ../../../../i/c/i/Bill.txt" >> test/a/t/e/r/is_bob_here.sh
echo "else" >> test/a/t/e/r/is_bob_here.sh 
echo "echo \"Bob n'est pas là ! Recommencez !\"" >> test/a/t/e/r/is_bob_here.sh
echo "fi" >> test/a/t/e/r/is_bob_here.sh

rm -f test/i/c/i/c_est_ca_a_lire.txt
touch test/i/c/i/c_est_ca_a_lire.txt
echo "Supprimez Bill, puis renommez is_Bill_killed.txt en is_Bill_killed.sh, puis exécutez-le !" >> test/i/c/i/c_est_ca_a_lire.txt

rm -f test/i/c/i/is_Bill_killed.sh
rm -f test/i/c/i/is_Bill_killed.txt
rm -f test/i/c/i/Bill.txt
touch test/i/c/i/is_Bill_killed.txt
echo "FILE=Bill.txt" > test/i/c/i/is_Bill_killed.txt
echo "if [ -f \"\$FILE\" ]; then" >> test/i/c/i/is_Bill_killed.txt
echo "echo \"Bill est toujours là ! Recommencez !\"" >> test/i/c/i/is_Bill_killed.txt

echo "else" >> test/i/c/i/is_Bill_killed.txt
echo "echo \"Bill n'est plus ! Rendez-vous à p/a/b/u !\"" >> test/i/c/i/is_Bill_killed.txt
echo "fi" >> test/i/c/i/is_Bill_killed.txt

rm -f test/p/a/b/u/c_est_par_la.txt
touch test/p/a/b/u/c_est_par_la.txt
echo "Dans l'arborescence se trouve trois fichiers contenant la chaine de caractère superindice en majuscule. Trouvez-les et cherchez la sortie de cet exercice" > test/p/a/b/u/c_est_par_la.txt

rm -f test/c/t/r/i1
touch test/c/t/r/i1
echo "SUPERINDICE 1 : t" >test/c/t/r/i1

rm -f test/k/l/z/i2
touch test/k/l/z/i2
echo "SUPERINDICE 2 : m" >test/k/l/z/i2

rm -f test/b/d/y/i3
touch test/b/d/y/i3
echo "SUPERINDICE 3 : s" >test/b/d/y/i3

rm -f test/t/m/s/terminus.txt
touch test/t/m/s/terminus.txt
echo "Bravo ! Vous maitrisez la ligne de commande Linux (ou presque)" > test/t/m/s/terminus.txt

rm -f test/f/h/m/i1
touch test/f/h/m/i1
echo "superindice 1 : d" >test/f/h/m/i1

rm -f test/a/t/w/i2
touch test/a/t/w/i2
echo "superindice 2 : t" >test/a/t/w/i2

rm -f test/p/o/p/i3
touch test/p/o/p/i3
echo "superindice 3 : c" > test/p/o/p/i3

rm -f test/d/t/c/serait_ce_la_fin.txt
touch test/d/t/c/serait_ce_la_fin.txt
echo "Et bien non, vous n'avez pas bien lu l'énoncé ! Dommage !" > test/d/t/c/serait_ce_la_fin.txt




