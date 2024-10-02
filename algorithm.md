# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. ask user what package they have
2. covert the variable package to lowercase 
2. set variable for monthly cost and additional GB 
3. ask how much data they use
4. ask how many months
4. while package does not equal 'green', 'blue', and 'purple'
   5. output 'that is not a valid package, must choose between green blue and purple'
4. if package is green
   5. set monthly cost to 49.99
   6. data provided is 2GB
   7. set additional GB to 15
   7. ask user if they have a coupon 
   8. if they have a coupon
11. if package is blue
    12. set monthly cost to 70
    13. data provided is 4GB
    14. set additional GB to 10 
14. if package purple
    15. set monthly cost to 99.95
    16. data provided is unlimited
17. equation for bill is (monthly cost + (data used - data provided) * additional GB) * how many months
18. round bill to the nearest hundredth decimal place
19. if they have a coupon
    20. if bill >= 75
        21. subtract 20 from bill
22. output bill