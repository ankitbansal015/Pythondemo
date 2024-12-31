class dad:
    basketball=2

class son(dad):
    dance=1
    def isdance(self):
        return f"yes i dance {self.dance}no of times"

class grandson(son):

    dance=5
    def isdance(self):
        return f"jakson yeah!!" \
            f"yes i dance very owsm {self.dance}no of times"

darry=dad()
larrry=son()
hary=grandson()

print(hary.isdance())
print(hary.basketball)

