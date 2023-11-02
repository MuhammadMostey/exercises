
# fillZeros function is works as the function zfill(x) on string types

# param string is the number you want to  fill the didgits with 0 and the length is the number width like 4  means 4 digit numbers
def fillZeros(string, length):
    if(len(string) == length ):
        return string
    else:
        missing = length - len(string)
        new = ('0' * missing  )
        return new+string 
         
        

x = '999'

ab = fillZeros(x, 4)
print(ab)