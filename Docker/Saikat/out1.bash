#!/bin/bash
s=1
`sudo docker stats --no-stream |grep -v nginx > out`
`sudo cat out |awk '{print $3}' | sed "1d" | sed "s/%//" > out1`
u=`grep -v nginx out1 |awk '{s+=$1} END {printf "%.0f\n", s}'`
d=`grep -v nginx out1 |wc -l`
echo 1;
while :
do
	echo 2;
	if [ $d -lt 1 ]
	then
		echo 3a;
		`sudo docker-compose up -d --scale kitchen=$s`
	else
		echo 3b;
		`sudo docker stats --no-stream |grep -v nginx > out`
		`sudo cat out |awk '{print $3}' | sed "1d" | sed "s/%//" > out1`
		u=`grep -v nginx out1 |awk '{s+=$1} END {printf "%.0f\n", s}'`
		d=`grep -v nginx out1 |wc -l`
		o=$((u / d));
		if [ $o -gt 7 ]
		then
			echo 4a;
			s=$((s+1));
			`sudo docker-compose up -d --scale kitchen=$s`
		elif [ $o -lt 3 ]
		then
			echo 4b;
			s=$((s-1));
			`sudo docker-compose up -d --scale kitchen=$s`
		fi
	fi
	sleep 1m
done
#echo $d;
#echo $u;
#o=$((u / d));
#echo $o;
#sleep 1m
