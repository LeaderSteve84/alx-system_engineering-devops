#!/usr/bin/env bash
# using puppet for SSH client configuration

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
          HOST *
          IdentityFile ~/.ssh/school
          PasswordAuthentication no
          ",
}
