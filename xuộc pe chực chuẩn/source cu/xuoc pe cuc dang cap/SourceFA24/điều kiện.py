#1 No case sensitive (không phân biệt in hoa hay in thường)
    if name[-1].lower() == 'z': #Tên kết thúc bằng chữ z không phân biệt in hoa hay in thường
            return
#2 is a fibonacci number
    def is_fibonacci_number(self,num):
            if num < 0:
                return False
            a, b = 0, 1
            while b < num:
                a, b = b, a + b
            return b == num        
            pass
#3 is a perfect number (số hoàn hảo)
    def isPerfectNumber(self,num):
        if num <= 0:
            return False
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        
        return divisors_sum == num
        pass
#4 is a prime number (số nguyên tố)
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
#5 is a composite number (số hợp ngược lại số nguyen tố)
    def is_composite(self, number):
        if number < 4:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return True
        return False
#6 is a perfect square number(số chính phương)
    def is_square(self, number):
        if number < 0:
            return False
        sqrt = int(number ** 0.5)
        return sqrt * sqrt == number
#7 is a Armstrong number
    def is_armstrong(self, number):
        # Chuyển số thành chuỗi để tính độ dài
        num_str = str(number)
        # Tính tổng lũy thừa các chữ số
        power_sum = sum([int(digit) ** len(num_str) for digit in num_str])
        # Kiểm tra xem số có bằng tổng lũy thừa các chữ số hay không
        return number == power_sum
#8 is a permutation number (số hoán vị)
    def is_permutation_number(self, number):
        num_str = str(number)
        digits = set(num_str)  # Unique digits in the number
        return len(digits) == len(num_str)
#9 is Harshad number
    def is_harshad_number(self, number):
        sum_digits = sum(int(digit) for digit in str(number))
        return number % sum_digits == 0
#10 is triangle number(số tam giác)
    def is_triangle_number(number):
        if number < 0:
            return False
        i = 1
        while number > 0:
            number -= i
            i += 1
        return number == 0
#11 is Catalan number 
    def is_catalan_number(number):
        if number < 0:
            return False
        catalan = 1
        for i in range(1, number+1):
            catalan = catalan * (4*i - 2) // (i + 1)
            if catalan == number:
                return True
            elif catalan > number:
                return False
        return False
#12 is a Kaprekar number
    def is_kaprekar_number(number):
        square = str(number ** 2)
        num_length = len(str(number))
        
        for i in range(1, num_length):
            left_part = int(square[:i])
            right_part = int(square[i:])
            
            if left_part + right_part == number and right_part != 0:
                return True
        
        return False
#13 is a Mersenne number
    def is_mersenne_number(number):
        exponent = 1
        while 2**exponent - 1 <= number:
            if 2**exponent - 1 == number:
                return True
            exponent += 1
        return False
