import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time took by {func.__name__}: {((time.time() - start) * 1000000):.4f} ms")
        return result
    return wrapper

@time_it
def print_rangoli(size):
    alpha_str = "abcdefghijklmnopqrstuvwxyz"
    result = ''
    repr_str = alpha_str[:size][::-1]
    width = size*2 - 2

    # for i in range(1,len(repr_str)+1):
    #     pattern = ''
    #     pattern += '-'.join(repr_str[:i])
    #     result+= f"{'-'*width}{pattern+pattern[::-1][1:]}{'-'*width}\n"
    #     width -= 2

    i = 1
    while i < (len(repr_str)+1):
        pattern = ''
        pattern = '-'.join(repr_str[:i])
        result+= f"{'-'*width}{pattern+pattern[::-1][1:]}{'-'*width}\n"
        width -= 2
        i +=1

    j = i - 2
    width += 4
    while j > 0:
        pattern = ''
        pattern += '-'.join(repr_str[:j])
        result+= f"{'-'*width}{pattern+pattern[::-1][1:]}{'-'*width}\n"
        width += 2
        j-=1

    print(result)
    # return result


@time_it
def rangoli(size):
    # List of lowercase English letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # List to store the lines of the rangoli
    lines = []
    
    # Constructing each line
    for i in range(size):
        # Part of the pattern up to the center (excluding the middle character)
        pattern = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        
        # Calculate the width to pad with dashes
        width = 4 * size - 3  # Total width for each line

        lines.append(pattern.center(width, '-'))
    
    # Combine all lines to form the final output with a new line in between
    return '\n'.join(lines[::-1] + lines[1:])




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    print(rangoli(n))