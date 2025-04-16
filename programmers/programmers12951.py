def solution(s):
    answer = ''
    word_list = s.split(" ");
    for word in(word_list):
        first = word[0:1];
        last =  word[1:].lower();
        if(first.isdigit()):
            answer = answer + first + last;
        if(first.isalpha()):
            answer = answer + first.upper() + last;
        if(first == " "):
            answer = answer + " "
        answer = answer + " "
    answer = answer[0:-1]
    return answer

solution("3people unFollowed me");