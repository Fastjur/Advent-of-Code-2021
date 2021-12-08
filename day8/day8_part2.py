from pprint import pprint


def get_digit_value(segment_mapping, digit: [str]) -> int:
    return list(filter(lambda x: segment_mapping[x] == digit, segment_mapping))[0]


if __name__ == "__main__":
    f = open("input.txt", "r")
    count = 0
    lines = f.readlines()

    total_sum = 0
    for line in lines:
        [signals, digits] = line.strip().split(" | ")
        signals = [list(c) for c in signals.split(" ")]
        digits = [list(c) for c in digits.split(" ")]

        for signal in signals:
            signal.sort()

        for digit in digits:
            digit.sort()

        digit_segments = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
        }
        segment_counts = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
        }
        segments = {
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None,
        }


        def get_segments(from_list: [str]) -> [str]:
            return [segments[s] for s in segments if s in from_list]


        for signal in signals:
            for segment in signal:
                segment_counts[segment] = segment_counts[segment] + 1
            if len(signal) == 2:
                digit_segments[1] = signal
                digit_segments[1].sort()
            if len(signal) == 4:
                digit_segments[4] = signal
                digit_segments[4].sort()
            if len(signal) == 3:
                digit_segments[7] = signal
                digit_segments[7].sort()
            if len(signal) == 7:
                digit_segments[8] = signal
                digit_segments[8].sort()

        segments['b'] = list(segment_counts.keys())[list(segment_counts.values()).index(6)]
        segments['e'] = list(segment_counts.keys())[list(segment_counts.values()).index(4)]
        segments['f'] = list(segment_counts.keys())[list(segment_counts.values()).index(9)]
        segments['c'] = list(filter(lambda s: s != segments['f'], digit_segments[1]))[0]
        segments['d'] = \
            list(filter(lambda s: s in digit_segments[4], filter(lambda s: segment_counts[s] == 7, segment_counts)))[0]
        segments['a'] = list(filter(lambda s: segment_counts[s] == 8 and s not in digit_segments[4], segment_counts))[0]
        segments['g'] = list(filter(lambda s: s not in segments.values(), segments))[0]

        digit_segments[0] = get_segments(['a', 'b', 'c', 'e', 'f', 'g'])
        digit_segments[0].sort()
        digit_segments[2] = get_segments(['a', 'c', 'd', 'e', 'g'])
        digit_segments[2].sort()
        digit_segments[3] = get_segments(['a', 'c', 'd', 'f', 'g'])
        digit_segments[3].sort()
        digit_segments[5] = get_segments(['a', 'b', 'd', 'f', 'g'])
        digit_segments[5].sort()
        digit_segments[6] = get_segments(['a', 'b', 'd', 'e', 'f', 'g'])
        digit_segments[6].sort()
        digit_segments[9] = get_segments(['a', 'b', 'c', 'd', 'f', 'g'])
        digit_segments[9].sort()

        line_sum = sum(get_digit_value(digit_segments, digits[i]) * 10 ** (3 - i) for i in range(4))
        print(line.strip(), line_sum)
        total_sum = total_sum + line_sum

    print(total_sum)
