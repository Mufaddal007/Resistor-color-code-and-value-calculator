color_codes=['Black', 'Brown', 'Red', 'Orange', 'Yellow','Green', 'Blue', 'Purple', 'Gray', 'White']
multiplier={'E':1,'k':pow(10,3),'M':pow(10,6),'G':pow(10,9)}
m1=['ohm','k-ohm','M-ohm','G-ohm']
while 1:
    
    print("What do you want to perform? ")
    c=input("Press 'C'  to get 'color code' or \nPress 'R' to get 'resistor value'.\n").lower()
    if c=='c':
        b=int(input("Number of bands? (4 or 5)\n"))
             # for 4 band value to color
        if b==4:
            resistance=input("Enter the resistance you want color code for: ")
            figure=''
            unit='E'
            for x in resistance:
                if x.isdigit() or x=='.':
                    figure+=x
                elif x.isalpha():
                    unit=x
            f1=int(float(figure)*multiplier[unit])
            
            first_digit=int(f1/pow(10,len(str(f1))-1)%10)
            second_digit=int(f1/pow(10,len(str(f1))-2)%10)
            
            f2=10*first_digit+second_digit

            third_digit=str(int(f1/f2)).count('0')
            first_band=color_codes[first_digit]
            second_band=color_codes[second_digit]
            third_band=color_codes[third_digit]
            fourth_band='Golden'
            print("Color code for {} resistance  is ======>{} {} {} {}".format(resistance, first_band, second_band, third_band, fourth_band))

            #for 5 band value to color
        elif b==5:
            resistance=input("Enter the resistance you want color code for: ")
            figure=''
            unit='E'
            for x in resistance:
                if x.isdigit() or x=='.':
                    figure+=x
                elif x.isalpha():
                    unit=x
            f1=int(float(figure)*multiplier[unit])
                                
            first_digit=int(f1/pow(10,len(str(f1))-1)%10)
            second_digit=int(f1/pow(10,len(str(f1))-2)%10)
            third_digit=int(f1/pow(10,len(str(f1))-3)%10)
            f2=100*first_digit+10*second_digit+third_digit

                                
            fourth_digit=str(int(f1/f2)).count('0')
                                
            first_band=color_codes[first_digit]
            second_band=color_codes[second_digit]
            third_band=color_codes[third_digit]
            fourth_band=color_codes[fourth_digit]
            fifth_band='Golden'
            print("Color code for {} resistance  is ======>{} {} {} {} {}".format(resistance, first_band, second_band, third_band, fourth_band, fifth_band))



    elif c=='r':
        b=int(input("Number of bands?(4 or 5)\n"))
        if b==4:
        #for 4 band color to value 
            colorarr=input("Enter color code to get value of resistance: ").split()
            first=color_codes.index(colorarr[0].title().strip())
            second=color_codes.index(colorarr[1].title().strip())
            third=color_codes.index(colorarr[2].title().strip())
                        
            t2=third-(third%3)
            suf=m1[int(t2/3)]
            resnet=(10*first+second)*pow(10, third%3 )
            if (third+1)%3==0:
                resnet/=pow(10, third+1)
                suf=m1[int(t2/3)+1]
            print("Resistance Value =======>{}{}".format(resnet, suf))
        elif b==5:
        #for 5 band color to value
            colorarr=input("Enter color code to get value of resistance: ").split()
            first=color_codes.index(colorarr[0].title().strip())
            second=color_codes.index(colorarr[1].title().strip())
            third=color_codes.index(colorarr[2].title().strip())
            fourth=color_codes.index(colorarr[3].title().strip())
                            
            t2=fourth-(fourth%3)
            suf=m1[int(t2/3)]
            resnet=(100*first+10*second+third)*pow(10, fourth%3)
            if (fourth+1)%3==0:
                resnet/=pow(10, fourth+1)
                suf=m1[int(t2/3)+1]
            print("Resistance Value =======>{}{}".format(resnet, suf))


    else :
        print("Invalid input")

    print("\n")

    
        

