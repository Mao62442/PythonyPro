def moduleMethod():
    print("Module Method Called")

print("Module Name:", __name__)

if __name__ == "__main__":
    print("Module is being run directly")
    moduleMethod()
else:
    print("Module is being imported")