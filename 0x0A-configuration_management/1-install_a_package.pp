#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package { 'python3-pip':
  ensure => installed,
}

package { 'python3-setuptools':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show flask',
  require => [
    Package['python3-pip'],
    Package['python3-setuptools'],
  ],
}
