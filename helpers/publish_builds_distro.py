from distro import *
from glob import iglob, glob

import casadi
release = casadi.__version__

for i in glob("*.deb"):
  os.remove(i)
  releaseFile(release,i,label="Development version (libraries and headers)")