# Install version of flask (2.1.0)
#!/usr/bin/pup
package {['python', 'flask', 'werzeug']:
  ensure   => '3.8.10', '2.1.0', '2.1.1',
  provider => 'pip3'
}
