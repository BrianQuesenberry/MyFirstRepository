#Basic login structure with data logging
#Use account.loginmain() to call from start

current_user = []
#Stores the current user's info in an array for easy access

logcount = open('D:\\LoginCount.txt', 'r')
#LoginCount keeps track of total number of users
t_users = logcount.readline()



class account() :
    

  def loginmain() :
  
    if (input('\nDo you already have an account: ').lower() == 'no') :
    
      account.newacc()
    
    else :
    
      account.login()


  def newacc() :
      
    global t_users
   
    firstname = (input('\n\nEnter your first name: ').lower())
    while (firstname.isalpha() == False) :
      
      print('\nName must only contain letters')
      firstname = input('\nEnter your first name: ')
      
    lastname = (input('Enter your last name: ').lower())
    while (lastname.isalpha() == False) :
      
      print('\nName must only contain letters')
      lastname = input('\nEnter your last name: ')
      #Prevents first or last name from containing non letter characters 
    
    fullname = (firstname + ' ' + lastname)
    
    first_initial = (firstname[:1].upper())
    last_initial = (lastname[:1].upper())
    rest_of_firstname = firstname[1:]
    
    t_users = (int(t_users)) + 1
    t_users = str(t_users)
    
    username = ''.join(t_users + first_initial + rest_of_firstname + last_initial)
    #Creates a different individual username for users
    
    log = open('D:\\PythonLoginData.txt', 'a')
    log.write(t_users + ':' + username + ':' + fullname + ':')
    #writes user data to file
    
    password = input('\nEnter a password: ')
    while (len(password) <= 5) :
      
      print('Password must be more than 6 characters. Try again')
      password = input('\nEnter a password: ')
      #Prevents users from using passwords shorter than 6 characters
      
    log.write(password + ':\n')
    log.close()
    #Writes password to user data. Then creates new line; ready for next new user
    
    logcount = open('D:\\LoginCount.txt', 'w')
    logcount.write(t_users)
    logcount.close()
    #Overwrites previous user total with new total users
    
    print('\nYour username is ' + username + '\nDont forget your username!')
    print('\n~~~~~~~~~~~~~~~~~~~~~ Account Created ~~~~~~~~~~~~~~~~~~~~~')
    
    account.login()
    #user signs in to check it's working
    

  def login() :

    global currentuser
    signin = 'false'
    log = open('D:\\PythonLoginData.txt', 'r')
    
    print('\nPlease log in')
    
    check_username = input('\nUsername: ')
    check_password = input('\nPassword: ')
    
    for line in log :
      
      user_array = line.split(':', 4)
      db_username = user_array[1]
      #Goes through every line in file and checks if usernames match
      
      if (check_username == db_username) :
        
        db_password = user_array[3]
        #After usernames match, checks if passwords match
        
        if (check_password == db_password) :
          
          print('\n\nThank you for logging in')
          currentuser = user_array
          signin = 'true'
          #User is signed in and their data is saved locally under currentuser
  
    if (signin != 'true') :
      
      print('\nIncorrect username or password')
      account.askacc()
      #If username or password doesn't match. Also error checks for loop errors.
    
  def askacc() :

    newacc = input('\nWould you like to make a new account: ')
    
    if (newacc.lower() == 'yes') :
      
      account.newacc()
      
    else :
      
      account.login()

