# Python 2 and 3



import os

here = os.path.abspath(os.path.dirname(__file__))

exec( open(os.path.join( here,'_version.py' )).read() )  # creates local __version__ variable
