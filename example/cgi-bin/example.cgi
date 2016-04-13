#!"\xampp\perl\bin\perl.exe" -wT


use strict;
use CGI qw(param);

# Here you can do whatever you want
my $data="<h3>This is data from example.cgi fetched via AJAX request...</h3>";

# After all, push your data to output...
print "Content-type: text/plain\n\n";
print $data;
