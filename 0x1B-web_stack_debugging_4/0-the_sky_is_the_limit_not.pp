#fix limit
exec { 'Fix limit on nginx':
  command => 'sed -ri "s/(ULIMIT=\"-n) [0-9]+/\1 10000/" /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'restart server':
  onlyif  => 'test -e /etc/default/nginx',
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
