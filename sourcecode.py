class library:
    def __init__(self,l1,l2,booklist,index):
        line1 = l1.split()
        self.index = index
        self.totalBook = int(line1[0])
        self.signup_process_time = int(line1[1])
        self.can_scan_number = int(line1[2])
        
        
        line2 = l2.split()
        self.list_of_books = []
        for book in line2:
            self.list_of_books.append(booklist[int(book)])
        
    def get_available_book_number(self):    
    
        number = 0

        for i in self.list_of_books:
            if i.scanned:
                continue
            number += 1

        return number
    
    def toplam_kitap_puan(self):

        score = 0

        for i in lib.list_of_books:
            if i.scanned:
                continue

            score += i.score

        return score

    def ortalama_puan(self):
        

        return self.toplam_kitap_puan()  /  self.get_available_book_number()

    def howmany_books_can_be_scanned(self,days):
        kalan_gun = days - self.signup_process_time
        okunabilecek_kitap_sayisi = kalan_gun * self.can_scan_number    # kaç tane kitap okuyabileceği
        musait_kitap_sayisi = self.get_available_book_number()
        
        skor_index_tuple = []
            
        for i in self.list_of_books:
            if i.scanned:
                continue

            skor_index_tuple.append( (i.score,i.id )  )
            i.scanned = True

        skor_index_tuple.sort(reverse=True)

        
        if okunabilecek_kitap_sayisi < musait_kitap_sayisi:

            
            return skor_index_tuple[:okunabilecek_kitap_sayisi]
        
        
        else:
            
            return skor_index_tuple[:musait_kitap_sayisi]
        
            

class book:
    def __init__(self,book_id,score):
        self.id = int(book_id)
        self.score = int(score)
        self.scanned = False
        
    def set_scanned(self):
        self.scanned = True
        
        
def kadir_score_lib(lib):
    
    return (lib.toplam_kitap_puan())  /   ( lib.signup_process_time + (lib.get_available_book_number() / lib.can_scan_number))


def output(lib):
    
    ##ilk line
    
    with open("c_incunabula_output.txt",mode = "a+") as f:
        score_index_tuple = lib.howmany_books_can_be_scanned(days)
        number_of_books_to_be_scanned = len(score_index_tuple)
        
        f.write(str(lib.index) + " " + str(number_of_books_to_be_scanned) + "\n" )
        
        for (score,index) in score_index_tuple[:-1]:
            
            f.write(str(index) + " ")
            
        (score,index) = score_index_tuple[-1]
        
        f.write(str(index) + "\n")




days = 0
with open("c_incunabula.txt", mode = "r") as f:
    list_libs = []
    list_books = []
    
    (totalbooks, totallibraries, days) = f.readline()[:-1].split()
    days = int(days)
    totallibraries = int(totallibraries)
    totalbooks = int(totalbooks)
    
    
    book_scores = f.readline()[:-1].split()
    for i in range(totalbooks):
        list_books.append( book(i, int(book_scores[i])) )
        
    for e,i in enumerate(range(totallibraries)):
        lib_line1 = f.readline()[:-1]
        lib_line2 = f.readline()[:-1]
        
        list_libs.append(  ( library(lib_line1,lib_line2,list_books,e) ,  e   )   )
    
sayi = 0
while True:

    
    if days <= 0:
        break
    if list_libs == []:
        break
    
    
    list_scores = []

    for (lib,e) in list_libs:
        list_scores.append((kadir_score_lib(lib)  ,  e )   )

    list_scores.sort(reverse=True)
    
    
    for (score,index) in list_scores:
        libreelindex = 0
        
        for (lib,e) in list_libs:
            if e == index:
                libreelindex = e
                optimal_lib = lib
                break
                

        if optimal_lib.signup_process_time > days:
            list_libs.remove((optimal_lib,libreelindex))
            continue
        else:
            output(optimal_lib)
            days -= optimal_lib.signup_process_time
            
            
            
            
            list_libs.remove((optimal_lib,libreelindex))
            
            sayi += 1
                
            break
            
    
    
    
with open("c_incunabula_last_output.txt", mode = "a+") as f:
    
    f.write(str(sayi) + "\n")
    with open("c_incunabula_output.txt", mode = "r") as f2:
        
        f.write(f2.read())
    
    
    

    
