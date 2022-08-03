import random
import sys
import time
def nulis(teks):
    for i in teks:
        sys.stdout.write(i)
        sys.stdout.flush()
    #kecepatan mengetik
        time.sleep(random.random()*0.20)
nulis('njajal sek ae')