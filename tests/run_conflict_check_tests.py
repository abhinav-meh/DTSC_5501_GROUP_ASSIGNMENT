# Array Tests
# Known Data Set
testKnownDataArray(10)

# Small Random Data Set (10)
testRandomDataArray(10,1)

# Medium Random Data Set (500)
testRandomDataArray(500,1)

# Random Data Set for 50,500,1000,5000,10000,25000,50000
test_inc = (50,500,1000,5000,10000,25000,50000)

test_mult_cases_array(test_inc)


# Linked List Tests
# Known Data Set
testKnownDataLinked(10)

# Small Random Data Set (10)
testRandomDataLinked(10)

# Medium Random Data Set (500)
testRandomDataLinked(500)

# Random Data Set for 50,500,1000,5000,10000,25000,50000
test_inc = (50,500,1000,5000,10000,25000,50000)

test_mult_cases_linked(test_inc)
