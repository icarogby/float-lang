from flooat import Signal


class halfAdder:
    def __init__(self) -> None:
        self.signalDict: dict[str, Signal] = {'aValue': Signal(False), 'bValue': Signal(False), 'carryOut': Signal(False, ['aValue', 'bValue']), 'result': Signal(False, ['aValue', 'bValue'])}

    def stabilize(self, aValue_value: bool, bValue_value: bool):
        self.signalDict['aValue'].setValue(aValue_value)
        self.signalDict['aValue'].setStabilized(True)

        self.signalDict['bValue'].setValue(bValue_value)
        self.signalDict['bValue'].setStabilized(True)
        
        while not all([self.signalDict[signal].isStabilized() for signal in self.signalDict]): # While not all signs are stabilized
            # Try stabilize the signs
            for signal in self.signalDict:
                if not self.signalDict[signal].isStabilized():
                    if signal == "carryOut":
                        self.signalDict[signal].setValue(self.signalDict['aValue'].getValue() & self.signalDict['bValue'].getValue())
                        
                        self.signalDict[signal].setStabilized(True)
                        self.signalDict[signal].setChanged(True)

                    if signal == "result":
                        self.signalDict[signal].setValue(self.signalDict['aValue'].getValue() ^ self.signalDict['bValue'].getValue())
                        
                        self.signalDict[signal].setStabilized(True)
                        self.signalDict[signal].setChanged(True)
                
            # Verify if the sensibility list has chanced values
            for signal in self.signalDict:
                for sensibilitySignal in self.signalDict[signal].getSensibilityList(): # For each sensibility signal
                    if self.signalDict[sensibilitySignal].isChanged(): # if someone have changed
                        self.signalDict[signal].setStabilized(False) # This sign is not stabilized yet
                        break
            
            # Define all sign as not changed
            for signal in self.signalDict:
                self.signalDict[signal].setChanged(False)

        return self.signalDict
