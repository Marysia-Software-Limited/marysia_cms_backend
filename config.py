from beret_utils import get_config, EnvValue, join_path_value, format_string
from beret_utils import PathData

base_dir = PathData.main()

DEFAULT_CONFIG = (
    ('POSTGRES_ENGINE', 'django.db.backends.postgresql'),
    ('POSTGRES_NAME', 'postgres'),
    ('POSTGRES_USER', 'postgres'),
    ('POSTGRES_PASSWORD', 'postgres'),
    ('POSTGRES_HOST', 'db'),
    ('POSTGRES_PORT', ''),
    ('PROJECT_APP', base_dir.name),
    ('SECRET_KEY', "django-insecure-aj#exo2bw$h%ps^hr4o+ch)e_u2ao1j19rd6z0q)l1o#e!9rn5"),
)

ENV_FILES = (
    '.env',
    '.local.env',
)

Config = get_config(DEFAULT_CONFIG, ENV_FILES)
config = Config()

print(config)
