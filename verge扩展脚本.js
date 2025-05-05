const rules = [
  //自定义直连
  'DOMAIN-SUFFIX,jx.cn,DIRECT',
  'DOMAIN-SUFFIX,waadri.top,DIRECT',
  'DOMAIN-SUFFIX,linux.do,DIRECT',
  //steam下载直连
  'DOMAIN,steamcdn-a.akamaihd.net,DIRECT',
  'DOMAIN-SUFFIX,steamserver.net,DIRECT',
  //其他分流
  'GEOSITE,telegram,Telegram',
  'GEOIP,telegram,Telegram,no-resolve',
  'DOMAIN-SUFFIX,nexus-cdn.com,HongKong',
  'GEOSITE,github,HongKong',
  'GEOSITE,rockstar,HongKong',
  //基础
  'GEOSITE,gfw,节点选择',
  'GEOIP,CN,DIRECT',
  'MATCH,节点选择',
];

function main(config, profileName) {
  console.log(profileName)
  config['rules'] = rules;
  config['proxy-groups'] = [
    {
      'name': '节点选择',
      'type': 'select',
      'include-all-proxies': true,
      'icon': 'https://www.clashverge.dev/assets/icons/adjust.svg',
      proxies: ['DIRECT', 'HongKong'],
    },
    {
      'name': 'Telegram',
      'type': 'select',
      'include-all-proxies': true,
      'filter': "(?i)singapore|sg",
      'icon': 'https://www.clashverge.dev/assets/icons/telegram.svg',
    },
    {
      'name': 'HongKong',
      'type': 'url-test',
      'url': 'https://www.gstatic.com/generate_204',
      'interval': 300,
      'tolerance': 50,
      'include-all-proxies': true,
      'filter': "(?i)港|hk|hongkong|hong kong",
      'icon': 'https://fastly.jsdelivr.net/gh/clash-verge-rev/clash-verge-rev.github.io@main/docs/assets/icons/flags/hk.svg',
    },
  ];
  return config;
}
