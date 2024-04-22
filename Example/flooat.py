class Signal:
    def __init__(self, value: bool, sensibilityList: list[str] = []) -> None:
        self.value = value
        self.stabilized = False
        self.changed = False
        self.sensibilityList = sensibilityList

    def __repr__(self) -> str:
        return f"Signal({self.value}, {self.stabilized}, {self.changed}, {self.sensibilityList})"

    def getValue(self):
        return self.value
    
    def setValue(self, value: bool):
        self.value = value

    def isStabilized(self):
        return self.stabilized
    
    def setStabilized(self, value):
        self.stabilized = value

    def isChanged(self):
        return self.changed
    
    def setChanged(self, value):
        self.changed = value

    def getSensibilityList(self):
        return self.sensibilityList
    