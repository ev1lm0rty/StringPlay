BEGIN { 
  print "Usernames"
  print "----------------------------"
  FS = ":"
  OFS = " "
}

/bash/||/login/{print $1}
END {
  print "----------------------------"
}
