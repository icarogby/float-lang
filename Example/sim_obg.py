from halfAdder_obj import halfAdder

ha = halfAdder()

for i in ha.stabilize(False, False):
    print(i, ha.signalDict[i])

