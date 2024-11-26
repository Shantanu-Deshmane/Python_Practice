def calculate(a):
    sum1=0
    product=1
    for i in a:
        sum1+=int(i)
        product*=int(i)

    return f"Sum is {sum1} and product is {product}"
    # print("sum of entered number: ", sum1)
    # print("product of entered number: ", product)

# a=input("Enter a number: ")
# calculate(a)