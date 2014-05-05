{
   'name': 'Extra reports',
   'version': '0.02',
   'category': 'Reports',
   'description': "OpenERP module that adds reports to existing modules in OpenERP.",
   'author': 'Covetel R.S',
   'website': 'http://www.covetel.com.ve',
   'depends': ['stock', 'procurement', 'board', 'sale'],
   'data': [
       'reports.xml',
   ],
   'init_xml': [],
   'update_xml': [
       'reports.xml',
   ],
   'demo_xml': [],
   'test': [],
   'installable': True,
   'active': False,
}
