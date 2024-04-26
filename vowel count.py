def vowel_count(str):
    count=0
    vowel=set("aeiou")
    
    for alphabet in str:
        if alphabet in vowel:
            count=count+1
    print("no.of vowels:",count)

str="anitha"
vowel_count(str)