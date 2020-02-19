# Programming Assignment 3
# Ricky Long


#1. Greet the customer
#2. Ask how many tickets they want to purchase
#3. Display the order information
#4. Ask customer if they want to change their order
#5. If not, display receipt with information, subtotal, tax, subtotal
#6. If changes are requested, restart the ordering process from the beginning
#7. Display a farewell message

#----------------------------------------------------------------------------------------------
#Welcome banner and intro options
border = '=-'*30
welcome_text = 'Welcome! Please complete your ticket order below!'
center = '{:^'+str(len(border))+'}'
print(border)
print(center.format(welcome_text))
print(border +'\n')
print('='*19,' THEME PARK OPTIONS ','='*19,'\n')
#----------------------------------------------------------------------------------------------
#Theme park selection menu
print('{0:>15}{1:^10}{2:<10}'.format('+','-'*30,'+'))
print('{0:>15}{1:^30}{2:<15}'.format('|','THEME PARK','|'))
print('{0:>15}{1:<0}{2:<17}{3:<18}'.format('+','---+','-'*26,'+'))
print('{0:>15}{1:>2}{2:>2}{3:^26}{4:<15}'.format('|','1','|','UNIVERSAL STUDIOS','|'))
print('{0:>15}{1:<0}{2:<17}{3:<18}'.format('+','---+','-'*26,'+'))
print('{0:>15}{1:>2}{2:>2}{3:^26}{4:<15}'.format('|','2','|','MAGIC KINGDOM','|'))
print('{0:>15}{1:<0}{2:<17}{3:<18}'.format('+','---+','-'*26,'+'))
print('{0:>15}{1:>2}{2:>2}{3:^26}{4:<15}'.format('|','3','|','EPCOT','|'))
print('{0:>15}{1:<0}{2:<17}{3:<18}'.format('+','---+','-'*26,'+'))
#----------------------------------------------------------------------------------------------
#Real world prices from these three places
us_price = 114.99
mk_price = 123.99
ep_price = 132.99

#Discount and cost variables
child_discount = .05
multi_day = .07
park = 0

#----------------------------------------------------------------------------------------------
#Prompt for park choice by user which associates their choice with park price variable.
selection = ''

while True:
    n = int(input('\nChoose a theme park (1-3): '))
    if n == 1:
        park = us_price
        selection = 'UNIVERSAL STUDIOS'
        break
    if n == 2:
        park = mk_price
        selection = 'MAGIC KINGDOM'
        break
    if n == 3:
        park = ep_price
        selection = 'EPCOT'
        break
    else:
        continue

one_day_child = park - (child_discount * park)
two_day_child = (park * 2) - ((child_discount + multi_day) * (park * 2))
three_day_child = (park * 3) - ((child_discount + multi_day) * (park * 3))
two_day_adult = (park * 2) - ((multi_day * 2)* park)
three_day_adult = (park * 3) - ((multi_day * 3)* park)
child_rate = park * child_discount
#----------------------------------------------------------------------------------------------
#formatting for larger table
print('='*19,' TICKET OPTIONS ','='*19,'\n')
print('{0:>5}{1:^10}{2:<8}'.format('+','-'*46,'+'))
print('{0:>5}{1:^46}{2:<8}'.format('|',selection,'|'))
print('{0:>5}{1:<0}{2:<}{3:<}{4:<}{5:<}'.format('+','-----+','-'*19,'+','-'*20,'+'))
print('{0:>5}{1:>4}{2:>2}{3:>16}{4:>4}{5:>16}{6:>5}'.format('|','DAY','|','ADULT TICKET','|','CHILD TICKET','|'))
print('{0:>5}{1:<0}{2:<}{3:<}{4:<}{5:<}'.format('+','-----+','-'*19,'+','-'*20,'+'))
print('{0:>5}{1:>4}{2:>2}{3:>16}{4:>4}{5:>16}{6:>5}'.format('|','1','|',float(round(park,2)),'|',float(round(one_day_child,2)),'|'))
print('{0:>5}{1:<0}{2:<}{3:<}{4:<}{5:<}'.format('+','-----+','-'*19,'+','-'*20,'+'))
print('{0:>5}{1:>4}{2:>2}{3:>16}{4:>4}{5:>16}{6:>5}'.format('|','2','|',float(round(two_day_adult,2)),'|',float(round(two_day_child,2)),'|'))
print('{0:>5}{1:<0}{2:<}{3:<}{4:<}{5:<}'.format('+','-----+','-'*19,'+','-'*20,'+'))
print('{0:>5}{1:>4}{2:>2}{3:>16}{4:>4}{5:>16}{6:>5}'.format('|','3','|',float(round(three_day_adult,2)),'|',float(round(three_day_child,2)),'|'))
print('{0:>5}{1:<0}{2:<}{3:<}{4:<}{5:<}'.format('+','-----+','-'*19,'+','-'*20,'+'))
print('\n')  
#----------------------------------------------------------------------------------------------
#Tallying subtotals and number of tickets per/type
print('='*19,' TICKET AMOUNTS ','='*19,'\n')
adult = (input('Number of Adult Tickets: '))
child = (input('Number of Child Tickets: '))
print('\n')
adult_ticket = 0
kid_ticket = 0
if adult == '1':
    adult_ticket = park
elif adult == '2':
    adult_ticket = ((park *2)/2)
elif adult == '3':
    adult_ticket = ((park * 3)/3)

if child == '1':
        kid_ticket = (park - (child_discount * park))
elif child == '2':
        kid_ticket = (park * 2)/2 - (child_discount * park) 
elif child == '3':
        kid_ticket = (park * 3)/3 - (child_discount * park) 
adult = int(adult)
child = int(child)
#----------------------------------------------------------------------------------------------

print('='*20,' REVIEW ORDER ','='*20,'\n')
print('{0:>15}{1:^10}{2:<10}'.format('+','-'*30,'+'))
print('{0:>15}{1:^30}{2:<15}'.format('|',selection,'|'))
print('{0:>15}{1:^10}{2:<10}'.format('+','-'*30,'+'))
print('{0:>15}{1:>3}{2:>13}{3:>2}{4:>8}{5:>2}'.format('|', 'Adults',adult,'x',round(adult_ticket,2),'|'))
print('{0:>15}{1:>3}{2:>11}{3:>2}{4:>8}{5:>2}'.format('|', 'Children',child,'x',round(kid_ticket,2),'|'))
print('{0:>15}{1:^10}{2:<10}'.format('+','-'*30,'+'))
print('\n')
#----------------------------------------------------------------------------------------------
subtotal = (child * kid_ticket) + (adult * adult_ticket)
tax = subtotal * .11
total = subtotal + tax



print('='*21,' CHECK OUT ','='*21,'\n')
print('=-'*15)
print('{0:^30}'.format('Ticket Order'))
print('=-'*15)
print('{0:^30}'.format(selection))
print('\n')
print('{0:<10}{1:^10}{2:^3}{3:<3}'.format('Adults',adult,'x',round(adult_ticket,2)))
print('\n')
print('{0:<10}{1:^10}{2:^3}{3:<3}'.format('Children',child,'x',round(kid_ticket,2)))
print('\n')
print('-'*30)
print('{0:<8}{1:>20}'.format('Subtotal:',round(subtotal,2)))
print('{0:<8}{1:>21}'.format('Tax:',round(tax,2)))
print('{0:<8}{1:>21}'.format('Total:',round(total,2)))
print('=-'*15)


goodbye_text = 'Thank You! Please Come Again'

print(border)
print(center.format(goodbye_text))
print(border +'\n')