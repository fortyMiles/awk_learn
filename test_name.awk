 {name[$1] = 1}
END {for (i in name)
	 for(j in name)
		 print i, j
 }
