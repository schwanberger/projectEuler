#!/bin/bash
for f in *.PDF
do
    pdftotext -q $f derp.txt;
    cat derp.txt | sed '2!d' | egrep -o '[0-9]{8}.*' | awk '{$1=""; $NF=""; print $0}' > herp.txt
    value=`cat herp.txt | sed -e 's/ /_/g'`
    mv "$f" ""$value"overf._Danica.PDF"
done

#rm *.txt