from libs.analysis import *
from libs.verbs import *
from libs.language import *
from libs.kw import *

for i in language["pronouns"].keys():
    print(conjugate(i, Word("use")))