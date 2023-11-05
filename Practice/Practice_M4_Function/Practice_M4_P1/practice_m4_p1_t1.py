def display_text():
    text = ('Don'"'"'t let the noise of others'"'"' opinions\ndrown out your own inner voice''"''.')
    author = 'Steve Jobs'
    lenght_author = len(text)
    aligned_author = author.rjust(int(lenght_author/2)+5, ' ')
    print(text)
    print(aligned_author)
 
display_text()