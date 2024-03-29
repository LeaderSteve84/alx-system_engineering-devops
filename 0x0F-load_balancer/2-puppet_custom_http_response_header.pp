# install nginx in New Ubuntu server
# add a custom HTTP header

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
        ensure  => 'installed',
        require => Exec['update system']
}

file {'/var/www/html/index.html':
        content => 'Hello World!'
}

exec {'redirect_me':
        command  => 'sed -i "24i\         rewrite ^ https://th3-grOOt.tk/ permanent;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

exec {'HTTP header':
        command  => 'sed -i "25i\          add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

service {'nginx':
        ensure  => running,
        require => Package['nginx']
}
