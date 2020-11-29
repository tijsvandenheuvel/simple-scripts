import os

counter=0
quotes="'''"
nl="\n"
n="\\"
itself ='''
import os
with open(f'replica{counter}.py', 'w') as f:
    f.write(f'counter={counter+1}'+nl)
    f.write('quotes="'+quotes+'"'+nl)
    f.write(f'nl="{n}'+'n"'+nl)
    f.write('n="'+n+n+'"'+nl)
    f.write("itself ="+quotes+itself+quotes)
    f.write(itself)
if counter !=10: os.system(f"python3 replica{counter}.py")
    '''
with open(f'replica{counter}.py', 'w') as f:
    f.write(f'counter={counter+1}'+nl)
    f.write('quotes="'+quotes+'"'+nl)
    f.write(f'nl="{n}'+'n"'+nl)
    f.write('n="'+n+n+'"'+nl)
    f.write("itself ="+quotes+itself+quotes)
    f.write(itself)
if counter !=10: os.system(f"python3 replica{counter}.py")