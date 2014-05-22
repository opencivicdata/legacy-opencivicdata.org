import os
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgis://opencivicdata:test@10.42.2.101/opencivicdata')
