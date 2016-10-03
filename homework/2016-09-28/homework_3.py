# 3. 단어 횟수 카운트
color_list = ['red', 'green', 'blue', 'blue', 'green', 'black', 'black', 'lime']
colors = ','.join(color_list)

print('color list: {}'.format(colors))
selected_color = input("input color: ")

count = 0
for color in color_list:
    if color == selected_color:
        count += 1

print('color count: {}'.format(count))
