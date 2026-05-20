#!/bin/bash

for x in {a..z}
do
    mkdir $x
    cd $x
    for y in {a..z}
    do
        mkdir $y
        cd $y
        for z in {a..z}
        do 
            mkdir $z
            cd $z
            for a in {a..z}
            do 
                mkdir $a
                
            done
            cd ..
        done
        cd ..

    done
    cd ..

done




