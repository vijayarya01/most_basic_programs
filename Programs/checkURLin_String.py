import  re # regular expression
str = " I am a blogger and check my website https://www.readblog.com/"

#urlregex.com > to capture the regular expression

url = re.findall('http[s]?://(?:[a-zA-Z])|[0-9]|[$~@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])+' ,str)

print(url) # this will give you url from the string str