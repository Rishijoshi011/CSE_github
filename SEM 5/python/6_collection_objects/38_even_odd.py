class EvenOdd:
    even_numbers = []
    odd_numbers = []
    
    @classmethod
    def get_num(cls):
        print("Enter -1 to stop: \n")

        numbers = []
        while True:
            x = int(input("Enter num: "))
            if x <= -1:
                break
            else:
                numbers.append(x)
            
        return numbers    
        
    @classmethod
    def classify_numbers(cls, numbers):
        for i in numbers:
            if i == 0:
                return ""
            elif i % 2 == 0:
                cls.even_numbers.append(i)
            else:
                cls.odd_numbers.append(i)
                
    @classmethod
    def show_numbers(cls, Type = 0):
        if Type == 0:
            cls.even_numbers.sort()
            return cls.even_numbers
        elif Type == 1:
            cls.odd_numbers.sort()
            return cls.odd_numbers
        else:
            print("Enter 0 for Even list and 1 for Odd List")


num = EvenOdd()  # * creating an object

numbers = num.get_num() 
print(numbers)        # * getting a list

num.classify_numbers(numbers)

print(f"Even numbers: {num.show_numbers(0)}")
print(f"Odd numbers: {num.show_numbers(1)}")