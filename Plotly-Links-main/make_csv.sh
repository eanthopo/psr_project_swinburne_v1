#!/bin/sh

infile=databasev2.dat
outfile=databasev2.csv

awk  '{for (i=1;i<=NF;i++){if (i < NF){printf "%s ~ ",  $i }else{printf "%s \n", $i}}}' $infile > $outfile
