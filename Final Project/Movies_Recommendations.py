###  CMPT 120 Final Project


'''
# input:  TEXT FILE "IN_genres.txt"

example first three genres:

action
comedy
drama
... 
'''

'''
# input:  TEXT FILE "IN_all_data.txt"
movie name      type, genres (4 genres), rating, origin
Harry_Potter      1    2345                 0   1       
The_Matrix        1    034X                 4   1
Black_mirror      0    45XX                 3   1


Numbers represent:
type: 0 - 'TV series', 1- 'movie'
genres are coded with numbers 0,1,2 … based on  the  IN-genres.txt file data.
An X represents an unknown genre. A movie will have at least 1 genre (not X)
genres not necessarily are in order within one movie
rating: 0- 'G' , 1- 'PG', 2- 'PG 13', 3- 'NC17', 4- 'R'
origin: 0- 'Canadian', 1- 'Foreign'


Assumption: data is all correct
There are no repeated movies

'''
'''

OUTPUT File - "OUT_recommended.csv"

one line per movie

Harry_Potter      
Black_mirror
'''


#########
#   MAIN GLOBAL VARIABLES AND STRUCTURES
#


#  MAIN TOP LEVEL VARIABLES AND STRUCTURES

#Lists with avaliable values for each feature

ltype = ["tv series","movies"]
lgenre = [] # will be populated with genres from file
lrating = ['G','PG','PG13','NC17','R']
lorigin = ['Canadian','foreign']



# all data
# are  inititalized here in empty just for documentation purposes,
# but are initialized below with the data from the files
# global lists
ld_mov = []
ld_type = []
ld_genres = []
ld_rating = [] 
ld_origin = [] 

lrecommend = [] # will be appended all recommended movies to output later as
                # output file

################# FUNCTIONS DEFINITIONS

def welcome():
    title = "WELCOME to the CMPT 120 Movies recommendation system!"
    print ("\n",title,"\n","="*len(title), "\n")
    return


def choice_file_names():
    file_name_all_data = "IN_all_data.txt"
    file_name_genres = "IN_genres.txt"
    file_name_out = "OUT_recommended.csv"
    print("The files that will be used by default (and need to be in this folder!) are:")
    print("\t IN all data:",file_name_all_data)
    print("\t IN genres:",file_name_genres)
    return file_name_all_data,file_name_genres,file_name_out

def inform_features():
    print("\nFeatures\n")
    print("TYPE: 0-tv series","1-movies")
    print("RATING: 0-G", "1-PG", "2-PG13", "3-NC17","4-R")
    print("ORIGIN: 0-Canadian","1-foreign")
    print("GENRES: from file")
    return


def read_string_list_from_file(the_file):

    
    fileRef = open(the_file,"r")      # opening file to be read
    localList_ofstrings=[]            # new list being constructed 
    
    for line in fileRef:
        string = line[0:len(line)-1]  # -1 to eliminate trailing '\n'
                                      # of each line 
                                    
        localList_ofstrings.append(string)      # adds string (line) to list
        
    fileRef.close()                  
    return localList_ofstrings


def convert_lstrings_to_lists(lstrings):

    
    ld_mov = []
    ld_type = []
    ld_rating = [] 
    ld_origin = []
    ld_genres = []
    
    nmovs = 0 
    for s_oneMov in lstrings:
        nmovs += 1
        l_oneMov = s_oneMov.split()

        ld_mov.append( l_oneMov[0] )  # alpha
        
        ld_type.append( int(l_oneMov[1]) )  # ints
        ld_rating.append( int(l_oneMov[3]) )
        ld_origin.append( int(l_oneMov[4]) )
        
        # 34XX  --> [3,4]
        four_genres = l_oneMov[2]
        list_genres_int = []
        
        for gen in four_genres:
            if (gen !="X"):
                    list_genres_int.append(int(gen))
                
        ld_genres.append( list_genres_int )
        
    #........
    print ("\n JUST TO TRACE, the lists with data are:\n")
    
    print("\n number of movies available:",nmovs,"\n")
    
    print ("movie \t\t type \t genres \t rating \t origin")
    for i in range(nmovs):
        print (ld_mov[i], "\t", ld_type[i], "\t", ld_genres[i],\
               "\t", ld_rating[i], "\t\t", ld_origin[i])
    
    #........
        
    return nmovs,ld_mov,ld_type,ld_genres,ld_rating,ld_origin

        
        
def show_one_movie(i):
    print("\n We recommend...")
    print ("movie \t\t type \t genres \t rating \t origin")
    print (ld_mov[i], "\t", ld_type[i], "\t", ld_genres[i],\
               "\t", ld_rating[i], "\t\t", ld_origin[i])
    return
    

def inputNumValidate(message):
    value = input(message)
    while not(value.isdigit()):
        print (" What you provided is not an integer  number, please re-type")
        value = input(message)
    ret = int(value)
    return ret


def ask_features():
    print("\n\n Please provide the features for your movie (type the number code):")

    print("\nType")
    for i in range(len(ltype)):
        print(i,"-", ltype[i])
    t = inputNumValidate("\nThe type? --> ")
                                                       
        
    print("\nRating")
    for i in range(len(lrating)):
        print(i,"-", lrating[i])
    r = inputNumValidate("\nThe rating? --> ")

    print("\nOrigin")
    for i in range(len(lorigin)):
        print(i,"-", lorigin[i])
    o = inputNumValidate("\nThe origin? --> ")

    
    print("\nGenres")
    for i in range(len(lgenres)):
        print(i,"-", lgenres[i])
    g = inputNumValidate("\nOne genre that you prefer? --> ")

    return [t,r,o,g]

def find_next_features_movie(list_features, start_from):

    [t,r,o,g] = list_features
    
    sel_idx = -1
    found = False
    
    i = start_from
    
    while not found and i< nmovs :
        
        if ld_type[i] == t  and ld_rating[i] == r  and \
           ld_origin[i] == o  and   (g in ld_genres[i]):

            sel_idx = i
            found = True

        i = i+1
        
    return sel_idx   
        

def format_to_list_of_str(lout):

    lstr = []
    for name in lout:
        elemFormatted = name + "\n"
        lstr.append(elemFormatted)

    ##.......
    print("\nTRACE list of strings ready to save to output file, one per line\n")
    for el in lstr:
        print(el)
    ##.......

    return lstr

def write_recommend_list_to_file(lout,the_file):

    lout_Strings = format_to_list_of_str(lout)
    
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lout_Strings:
        fileRef.write(line)
                                    
    fileRef.close()
    return
        
    
############################ TOP LEVEL

welcome()


file_name_all_data,file_name_genres,file_name_out = choice_file_names()

# loading input data in internal lists 



print ("\n\nInitial processing ...\n")

lgenres = read_string_list_from_file(file_name_genres)

lstrings_all = read_string_list_from_file(file_name_all_data)
            # reading from text file to a list of strings
          
nmovs,ld_mov,ld_type,ld_genres,ld_rating,ld_origin = \
                        convert_lstrings_to_lists(lstrings_all)
            # converting from list of strings to several lists
            
inform_features()

# to write the output file a list of lists will be gradually created
# and is started as an empty list
lrecommend = []


another_request= input("\n\n ** Would you like to make a request? (y/n) --> ").lower()
nreqs = 0

while another_request == "y":
    
    nreqs += 1
          
    requested_features = ask_features()

    more_recom = "y"
    start_from = 0
        
    while more_recom == "y":
            
        selected_idx = find_next_features_movie(requested_features, start_from)

        if selected_idx == -1:
            more_recom = "n"
            print("Sorry we do not have more movies with those features!!")
              
        else:
            show_one_movie(selected_idx)
            name_recom = ld_mov[selected_idx]
            lrecommend.append(name_recom) 
            start_from = selected_idx +1

            moreRecMssg = "\nMore recommendations, same features? (y/n) --> "

            more_recom = input(moreRecMssg).lower()      
              

    another_request= input("\n\n ** Would you like another request? (y/n) --> ").lower()


### BONUS: Inform similarities between two movies
### NOT IMPLEMENTED IN STAGE 2.5

## WRITE OUTPUT FILE (REQUIRED BUT USER IS PROMPTED
## Trace printing in functions
x = input("\nAre you ready to save your recommended movies? (y/n) --> ").lower()
if (x == "y"):
    if len(lrecommend) == 0:
        print("\nWe did not recommend you any movie, so, no file will be saved")
    else:
        write_recommend_list_to_file(lrecommend,file_name_out)


print("\nAll done! Bye!\n")

# END OF PROGRAM

    
    
    
    
 


