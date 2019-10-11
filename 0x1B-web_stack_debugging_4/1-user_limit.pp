# User limit
exec { 'replace_hard':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 10048/g' \
/etc/security/limits.conf",
  path    => ['usr/bin', 'usr/sbin', '/bin'],
}
exec {'replace_soft':
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 30048/g' \
/etc/security/limits.conf",
  path    => ['usr/bin', 'usr/sbin', '/bin']
}
exec { 'restart-op':
  command => 'sysctl -p',
  path    => ['/sbin']
}