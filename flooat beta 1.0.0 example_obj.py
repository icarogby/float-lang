class halfAdder():
    # (bit value, stabilized, changed, sensibility list)
    signsDic = {"sum": [False, False, False, ()], "carry": [False, False, False, ()]}

    def stable(self, a, b):     
        while not all([self.signsDic[sign][1] for sign in self.signsDic]): # While not all signs are stabilized
            # Try stabilize the signs
            for sign in self.signsDic:
                if not self.signsDic[sign][1]:
                    if sign == "sum":
                        self.signsDic[sign][0] = a ^ b
                        self.signsDic[sign][1] = True
                        self.signsDic[sign][2] = True

                    elif sign == "carry":
                        self.signsDic[sign][0] = a & b
                        self.signsDic[sign][1] = True
                        self.signsDic[sign][2] = True
                
            # Verify if the sensibility list has chanced values
            for sign in self.signsDic:
                for sensibilitySign in self.signsDic[sign][3]: # For each sensibility sign
                    if self.signsDic[sensibilitySign][2]: # if someone have changed
                        self.signsDic[sign][1] = False # This sign is not stabilized yet
                        break
            
            # Define all sign as not changed
            for sign in self.signsDic:
                self.signsDic[sign][2] = False

        return self.signsDic

class twoBitIncrementor():
    # (bit value, stabilized, changed, sensibility list)
    signsDic = {"sum2": [False, False, False, ["carry1"]], "carry2": [False, False, False, ["carry1"]],"sum1": [False, False, False, ()], "carry1": [False, False, False, ()]}

    def stable(self, a): # A have tow bits
        while not all([self.signsDic[sign][1] for sign in self.signsDic]): # While not all signs are stabilized
            # Try stabilize the signs
            for sign in self.signsDic:
                if not self.signsDic[sign][1]:
                    if sign == "sum1":
                        self.signsDic[sign][0] = a[1] ^ True
                        self.signsDic[sign][1] = True
                        self.signsDic[sign][2] = True

                    if sign == "carry1":
                        self.signsDic[sign][0] = a[1] & True
                        self.signsDic[sign][1] = True
                        self.signsDic[sign][2] = True

                    if sign == "sum2":
                        self.signsDic[sign][0] = a[0] ^ self.signsDic["carry1"][0]
                        self.signsDic[sign][1] = True
                        self.signsDic[sign][2] = True

                    if sign == "carry2":
                        self.signsDic[sign][0] = a[0] & self.signsDic["carry1"][0]
                        self.signsDic[sign][1] = True
                        self.signsDic[sign][2] = True
                
            # Verify if the sensibility list has chanced values
            for sign in self.signsDic:
                for sensibilitySign in self.signsDic[sign][3]: # For each sensibility sign
                    if self.signsDic[sensibilitySign][2]: # if someone have changed
                        self.signsDic[sign][1] = False # This sign is not stabilized yet
                        break
            
            # Define all sign as not changed
            for sign in self.signsDic:
                self.signsDic[sign][2] = False

        return self.signsDic