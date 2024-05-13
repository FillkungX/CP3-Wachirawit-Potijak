usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "wachi" and passwordInput == "1234" :
    print("""---------WELLCOME TO WACHII COFFE!!---------
          Product List:
          [1] Coffe          20THB
          [2] Amasang Coffe  50THB
          [3] StarBook Coffe 100THB""")
    user_select = int(input())
    if user_select == 1:
        quantity = int(input("How Much Do You Want? : "))
        total = quantity * 20
        print(f"""
              --------------------------------------------------------
              Coffe          20THB x {quantity}  = {total}THB 
              --------------------------------------------------------""")
    elif user_select == 2:
        quantity = int(input("How Much Do You Want? : "))
        total = quantity * 50
        print(f"""
              -------------------------------------------------------
              Amasang Coffe          50THB x {quantity}  = {total}THB 
              -------------------------------------------------------""")
    elif user_select == 3:
        quantity = int(input("How Much Do You Want? : "))
        total = quantity * 100
        print(f"""
              ---------------------------------------------------------
              StarBook Coffe          100THB x {quantity}  = {total}THB 
              ---------------------------------------------------------""")
else:
    print("Error: Username or Password incorrect")

print("""Thank you!!
      You visit My site at
     wachicoffe.netlify.app""")
