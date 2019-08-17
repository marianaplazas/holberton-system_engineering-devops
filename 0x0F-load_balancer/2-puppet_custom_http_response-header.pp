# puppet adavance task
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
-> package{'nginx':
  ensure => present,
}
-> file_line {'header':
  path => 'etc/nginx/conf/nginx.conf',
  match => 'http {',	
  line => "http {
     	add_header X-Served_By "${hostname}";",
}
-> exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}