# Install version of flask (2.1.0)
#!/usr/bin/pup
package {'flask':
  ensure   => '3.0.0',
  provider => 'pip3'
}
