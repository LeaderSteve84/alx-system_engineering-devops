# to increases the amount of traffic which nginx can handle

exec { 'file--for-nginx':
  command => "/bin/sed -i 's/15/4094/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
