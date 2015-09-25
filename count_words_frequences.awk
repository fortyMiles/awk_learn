{ for (i = 1; i <= NF; i++) count[$1]++ }
END {for (i in count) print count[i],i }
