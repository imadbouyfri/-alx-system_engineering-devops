#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
exec { 'install_flask_2.1.0':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin'],
}

