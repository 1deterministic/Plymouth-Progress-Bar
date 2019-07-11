#!/bin/bash

build=./build
color_schemes=./color-schemes


if [ ! -d $build ]; then
    mkdir $build
fi

for i in $color_schemes/*;
do
    for f in $i/*;
    do
        [ -d $f ] && $(
            name=$(basename $f)-$(basename $(dirname $f))
            
            if [ ! -d $build/$name ]; then
                mkdir $build/$name
            fi

            cp $f/background.png $build/$name &&
            cp $f/box.png $build/$name &&
            cp $f/bullet.png $build/$name &&
            cp $f/entry.png $build/$name &&
            cp $f/lock.png $build/$name &&
            cp $f/logo.png $build/$name &&
            cp $f/progress-bar.png $build/$name &&
            cp $f/progress-box.png $build/$name &&
            sed "s/::NAME::/$name/g" plymouth > $build/$name/$name.plymouth &&
            cat script > $build/$name/$name.script
        )
    done;
done;

echo "Done!"
