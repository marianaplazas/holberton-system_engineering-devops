# debugging
exec { '/etc/default/nginx':
  command => '/bin/sed -i "s/15/15000/g" /etc/default/nginx &&
  /etc/init.d/nginx restart',
}