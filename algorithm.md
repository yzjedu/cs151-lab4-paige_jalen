# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. ask user what package they have
2. convert the variable package to lowercase 
2. while package does not equal 'green', 'blue', or 'purple':
   1. output "that is not a valid package, must choose between green blue or purple"
   2. ask user what package they have
3. set variable for monthly cost and additional GB 
4. ask how much data they use
5. ask how many months
6. if package is green:
   1. set monthly cost to 49.99
   2. set data provided to 2
   3. set additional data cost to 15
   4. ask user if they have a coupon 
   5. convert coupon to lowercase
7. if package is blue:
   1. set monthly cost to 70
   2. set data provided to 4
   3. set additional data cost to 10 
   4. coupon = 'no'
8. if package purple:
   1. set monthly cost to 99.95
   2. set data provided to 0
   3. set additional data cost to 0
   4. coupon = 'no'
9. additional data is (data used - data provided)
10. equation for bill is (monthly cost + additional data * additional data cost) * how many months
11. if they have a coupon:
      1. if bill >= 75:
         1. subtract 20 from the bill
11. round bill to the nearest hundredth decimal place
12. output bill  