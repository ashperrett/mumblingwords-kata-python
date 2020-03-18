class MumblingWords():

    def mumble_letters(self,inputStr):

        formattedOutput = ""
        separator = ""

        for i in range( len(inputStr) ):
            repeat = inputStr[i].lower() * i
            formattedOutput += separator + inputStr[i].capitalize() + repeat
            separator = "-"
        return formattedOutput