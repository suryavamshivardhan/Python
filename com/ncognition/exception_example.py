def exception_example():
    while True:
        try:
            x = int(input("Enter integer value ..."))
            #remove the below line if you want to see else block getting executed
            break
        except Exception as exc:
            print("There is an exception : {0}".format(exc))
        else:
            print("Else block exceuted if there is no exception ..")
        finally:
            print("finally block executed in all the scenarios ..")
exception_example()


