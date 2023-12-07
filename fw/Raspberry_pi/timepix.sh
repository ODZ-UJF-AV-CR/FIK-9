#!/bin/bash
export LD_LIBRARY_PATH=/home/rp/Documents/timepix
frameCount=$1
frameTime=$2
outDir=$3
i=1

while [ 1 ]
	do
		outFile=$outDir/data_${i}.clog
		~/Documents/timepix/fik9 $frameCount $frameTime $outFile
		#chmod +rw $outFile
		counts="$(grep -c "\[" "$outFile")"
		if test -f "$outFile"; then
			echo $outFile  $(date '+%s') $counts >> tpx.csv
			((i=i+1))
		fi
	done
