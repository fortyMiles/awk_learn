{
	++predct[$2] # record nodes in predct, $2's predessor number increment one.
	predct[$1] = predct[$1] # add the predes which is zero to queue
	succlist[$1, ++succnt[$1]] = $2
}

END {
	 qlo = 1 # it's the queue's first element's index
	 for(i in predct){
		n++;
		if (predct[i] == 0) # if find a "input node"
			q[++qhi] = i # qhi it's the queue's end element's index, push an element to queue
	 }

	 while(qlo <= qhi){
		t = q[qlo++];
		print t
		for (i = 1; i <= succnt[t]; i++){
			s = succlist[t, i]
			if(--predct[s] == 0)
				q[++qhi] = s
			}
	  }
	  if (qhi != n) print "tsort error: cycle in input"
	}
