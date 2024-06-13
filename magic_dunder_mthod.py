class Magic:
    name="magic"
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
            return i    

M=Magic()
print(M.name)
print(len(M))