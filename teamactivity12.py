largest_chapter = 0
largest_BOM_chapter = 0
largest_user_chapter = 0
largest_user_book = 0
user_volume = input('Which volume would you like to learn about? ')
with open ("books_and_chapters.txt") as file:
    for line in file:
        line_list = line.strip().split(':')
        book = line_list[0]
        chapter = int(line_list[1])
        volume = line_list[2]

        #find largest book
        if chapter > largest_chapter:
            largest_chapter = chapter
            largest_book = book

        #find BOM info
        if volume == 'Book of Mormon':
            print(book)
            if chapter > largest_BOM_chapter:
                largest_BOM_chapter = chapter

        #user requested info
        if volume == user_volume:
            if chapter > largest_user_chapter:
                largest_user_chapter = chapter
                largest_user_book = book


    print(f'The largest number of chapters is {largest_chapter} \n\
The largest book is {largest_book}')
    print(f'The largest Book of Mormon chapter is {largest_BOM_chapter}')
    print(f'The largest book in the user\'s requested volume is {largest_user_book}')

        
