listdir=$(ls)

for l in $listdir
do
    rm -rf ${l}/${l}

done
