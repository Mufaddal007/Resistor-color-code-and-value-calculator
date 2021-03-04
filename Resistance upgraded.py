color_codes=['Black', 'Brown', 'Red', 'Orange', 'Yellow','Green', 'Blue', 'Purple', 'Gray', 'White']
multiplier={'E':1,'k':pow(10,3),'M':pow(10,6),'G':pow(10,9)}
m1=['ohm','k-ohm','M-ohm','G-ohm']

def get_figure(resistance, bands):
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
    if bands=='4':
        f2=10*first_digit+second_digit
        third_digit=str(int(f1/f2)).count('0')
        get_color(first_digit,second_digit, third_digit)
    elif bands=='5':
        third_digit=int(f1/pow(10,len(str(f1))-3)%10)
        f2=100*first_digit+10*second_digit+third_digit
        fourth_digit=str(int(f1/f2)).count('0')
        get_color(first_digit, second_digit, third_digit, fourth_digit)
    
def get_color(a,b,c,d=None):
    first_band=second_band=third_band=fourth_band=fifth_band=''
    first_band=color_codes[a]
    second_band=color_codes[b]
    if d==None:
        third_band=color_codes[c]
        fourth_band='Golden'
        print(first_band,second_band,third_band,fourth_band)
    else:
        third_band=color_codes[c]
        fourth_band=color_codes[d]
        fifth_band='Golden'
        print(first_band,second_band,third_band,fourth_band,fifth_band)
while 1:
    resistance, bands=input("Enter the resistance and number of bands(4/5) for color code: \n").split()
    get_figure(resistance, bands)
            
        
        

        
        
