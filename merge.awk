{ count[$1] = count[$1] + $2 }
END { for (i in count) print i, count[i] }

