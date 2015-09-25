BEGIN {print " to find the max value and name"}
$1 > maxval { maxval = $1; maxname = $2}
{ print "maxmum value:" maxval }
END { print "Associated name: " maxname }
