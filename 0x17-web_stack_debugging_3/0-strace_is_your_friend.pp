#Fix wordpress
exec { 'fix_wordpress':
  command => "sed -ie 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}
