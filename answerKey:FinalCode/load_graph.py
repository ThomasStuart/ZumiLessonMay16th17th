from IPython.display import Image
G = Graph()

def load_graph( num ):
    global G 
    
    while num < 1 or num > 5: 
        num = input("Invalid Graph number, please enter a new one:  ")
        num = int(num)

    fileName = ""
    
    if num == 1:
        #set the file name 
        fileName = "simpleG.jpg"
        G.create_simple()
    elif num == 2:
        #set the file name 
        fileName = "simp_diff_len.jpg"
        G.create_simple_different_road_lengths()  
    elif num ==3:
        #set the file name 
        fileName = "simp_diff_ang.jpg"
        G.create_simple_different_angles()      
    elif num == 4:
        #set the file name 
        fileName = "mystery.jpg"
        G.mystery_graph()  
    elif num == 5:
        #set the file name 
        fileName = "complex.jpg"
        G.create_complex() 
        
    #display the image here 
    display( Image(filename=('/home/pi/Dashboard/user/Thomas/MyImages/'+fileName), width=300, height=200) )

load_graph(2)
