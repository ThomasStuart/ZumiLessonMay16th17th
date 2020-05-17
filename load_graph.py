G = Graph()
 
#1  -> G.create_simple()    #showed you guys 
#2  -> G.create_simple_different_road_lengths()  
#3  -> G.create_simple_different_angles()      
#4  -> G.mystery_graph()  
#5  -> G.create_complex()    #showed you guys 
# invalid 
 

def load_graph( num ):
    global G 
    
    while num < 1 and num > 5: 
        num = input("Invalid Graph number, please enter a new one:  ")
        num = int(num)
    
    fileName = ''  # TODO:: add this line 
    
    if num == 1:
        fileName= 'simpleG.jpg'  # TODO:: ADD THIS LINE 
        G.create_simple()
    elif num == 2:
        fileName= 'simp_diff_len.jpg'
        G.create_simple_different_road_lengths()  
    elif num ==3:
        fileName= 'simp_diff_ang.jpg'
        G.create_simple_different_angles()      
    elif num == 4:
        fileName= 'mystery.jpg'
        G.mystery_graph()  
    elif num == 5:
        fileName= 'complex.jpg'
        G.create_complex() 
    else:
        print("Invalid Graph number")
        
    display( Image(filename=('/home/pi/Dashboard/user/Thomas/MyImages/' + fileName), width=300, height=200) )
    
user_input = input("Enter Graph Number:  ")
print("You entered: ", user_input)
user_input = int(user_input)
load_graph(user_input)
