def calc():
    basic = 'one' \
            'two' \
            'three' \
            'four' \
            'five' \
            'six' \
            'seven' \
            'eight' \
            'nine'
    addit = 'ten' \
            'eleven' \
            'twelve' \
            'thirteen' \
            'fourteen' \
            'fifteen' \
            'sixteen' \
            'seventeen' \
            'eighteen' \
            'nineteen'
    secon = 'twenty' \
            'thirty' \
            'forty' \
            'fifty' \
            'sixty' \
            'seventy' \
            'eighty' \
            'ninety'

    result = len(basic)
    result += len(addit)
    result += len(secon)*10 + len(basic)*8
    result += len(basic)*100 +len('hundred')*9*100+ len('and')*9*99 + result*9
    result += len('onethousand')
    
    return result

print(calc())
