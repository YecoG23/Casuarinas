# from .common import *

# try:
# 	from .common import *
# except:
# 	pass

from .common import *

env_name = os.getenv('ENV_NAME', 'local')

if env_name == 'production':
    from .production import *
else:
    from .local import *