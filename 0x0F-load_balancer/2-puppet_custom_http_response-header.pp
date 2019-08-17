#puppet advance
exec { 'update':
command => 'usr/bin/apt-get update'
}

-> package{'nginx':
  ensure => present,
}
-> file_line {'line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  	 add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

-> exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}