# execute the pkill
exec { 'kill':
command  => 'pkill killmenow',
provider => 'shell',
}