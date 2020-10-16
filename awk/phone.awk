BEGIN {
  print "Phone Numbers"
  print "-----------------"
}

/[0-9]/

END{
  print "-----------------"
}
