EC2STACK_BIND_ADDRESS = '0.0.0.0'
EC2STACK_PORT = '5000'
CLOUDSTACK_HOST = 'api.exoscale.ch'
CLOUDSTACK_PORT = '443'
CLOUDSTACK_PROTOCOL = 'https'
CLOUDSTACK_PATH = '/compute'
CLOUDSTACK_CUSTOM_DISK_OFFERING = 'Custom'
CLOUDSTACK_DEFAULT_ZONE = 'CH-GV2'

INSTANCE_TYPE_MAP = {'m1.small': 'micro'}

DEBUG = False
TESTING = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
