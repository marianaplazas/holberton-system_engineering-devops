# puppet adavance task
exec { 'apt_update':
  command  => 'sudo apt-get update',
  provider => shell,
}
-> package{'nginx':
  ensure => present,
}
-> file_line {'heades':
  path   => '/etc/nginx/sites-available/default',
  line   => "http {
  	 add_header X-Served-By ${hostname};",
  match  => 'http {',
}
-> exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}