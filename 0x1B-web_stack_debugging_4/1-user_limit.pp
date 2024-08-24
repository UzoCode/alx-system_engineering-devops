# Increase hard file limit for holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton hard nofile/s/[0-9]\+/65536/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
}

# Increase soft file limit for holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft nofile/s/[0-9]\+/65536/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
}
