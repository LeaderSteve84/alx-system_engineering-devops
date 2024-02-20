# to increases the amount of traffic which nginx can handle

exec { 'file-for-nginx':
  command => "/bin/sed -i 's/15/4094/' /etc/default/nginx && sudo service nginx restart",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/usr/games:/usr/local/games',
}
