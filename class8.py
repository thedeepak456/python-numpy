# So, Today we talk about the if elif and else conditions in python.

# python is a indentation friendly language.

productname1 = 'veg biryani'
productname2 = 'chole bhature'
productname3 = 'chole kulche'
productname4 = 'rajma chawal'
productname5 = 'naan'
on = True
off = False
total = 500
rate = 50

if productname1 == 'veg biryani' and rate == 50 and on == False:
    print( "ye lo sir aapki biryani")
    total -= rate
    print( total)

elif productname2 == 'chole bhature' and rate == 50 and on == False:
    print( "ye lo sir aapki chole bhature")
    total -= rate
    print( total)

else:
    print("sir aapka khana nhi mila aur ye rahe aapke paise", total)