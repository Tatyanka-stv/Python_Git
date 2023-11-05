def display_text():
    text = 'Don'"'"'t compare yourself with anyone in this world...\nif you do so, you are insulting yourself.'
    author = 'Bill Gates'
    parts = []
    parts = text.split('...')
    for part in parts:
        lenght_of_part = len(part)
        break
    aligned_author = author.rjust(lenght_of_part+3, ' ')
    print(text)
    print(aligned_author)
 
display_text()