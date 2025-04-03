def solution(wallpaper):
    answer = []
    lux = 99;
    luy = 99;
    rdx = 0;
    rdy = 0;
    for line_idx in range(len(wallpaper)):
        line_arr = list(wallpaper[line_idx]);
        for paper_idx in range(len(line_arr)):
            if (line_arr[paper_idx] == "#" and lux == 99):
                lux = line_idx;
            if (line_arr[paper_idx] == "#" and luy > paper_idx):
                luy = paper_idx;
            if (line_arr[paper_idx] == "#"):
                rdx = line_idx + 1;
            if (line_arr[paper_idx] == "#" and rdy < paper_idx):
                rdy = paper_idx;
    answer = [lux, luy, rdx, rdy+1]
    return answer

solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]);
