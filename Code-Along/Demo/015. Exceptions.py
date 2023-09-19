def input_int():
    while True:
        try:
            return int(input("Enter integer: "))
        except ValueError:
            print("my_int is not an integer")
        except NameError:
            print("x is not defined")
        except: # Avoid this, as you cannot abort using Ctrl+C for instance.
            print("Some other kind of error")


x = input_int()
# It's possible to create a cell for debugging inside VS Code by writing #%% at the beginning of a line
#%%
print(f"x = {x}")