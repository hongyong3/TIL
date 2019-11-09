def solution(k, room_number):
    for i in range(1, len(room_number)):
        if room_number[i] not in room_number[: i]:
            continue
        while i < len(room_number):
            room_number[i] += 1
            if room_number[i] not in room_number[: i]:
                break
    return room_number

k = 10
room_number = [1, 3, 4, 1, 3, 1]
print(solution(k, room_number))