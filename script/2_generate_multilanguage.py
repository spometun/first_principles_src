from libs.utils import *
from libs.pipeline_classes import *
from libs.generate_language import *

root = "../.."

recreate_dir(root + "/www");
os.mkdir(root + "/www/studies")

generate_language(root, "ru")