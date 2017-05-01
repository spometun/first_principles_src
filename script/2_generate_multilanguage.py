from context import *
from libs.utils import *
from libs.pipeline_classes import *
from libs.generate_language import *


recreate_dir(ROOT + WWW);
os.mkdir(ROOT + WWW + STUDIES)

generate_language("ru")