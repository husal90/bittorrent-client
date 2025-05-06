def bdecode(data):
    def decode_item(index):
        if data[index] == ord('i'):
            index += 1
            end = data.index(b'e', index)
            number = int(data[index:end])
            return number, end + 1
        elif data[index] == ord('l'):
            index += 1
            lst = []
            while data[index] != ord('e'):
                item, index = decode_item(index)
                lst.append(item)
            return lst, index + 1
        elif data[index] == ord('d'):
            index += 1
            dct = {}
            while data[index] != ord('e'):
                key, index = decode_item(index)
                val, index = decode_item(index)
                dct[key] = val
            return dct, index + 1
        elif data[index] in b'0123456789':
            colon = data.index(b':', index)
            length = int(data[index:colon])
            start = colon + 1
            end = start + length
            return data[start:end], end
        else:
            raise ValueError("Invalid bencode data")

    result, _ = decode_item(0)
    return result

def bencode(value):
    if isinstance(value, int):
        return b'i' + str(value).encode() + b'e'
    elif isinstance(value, bytes):
        return str(len(value)).encode() + b':' + value
    elif isinstance(value, str):
        return bencode(value.encode())
    elif isinstance(value, list):
        return b'l' + b''.join([bencode(i) for i in value]) + b'e'
    elif isinstance(value, dict):
        items = sorted(value.items())
        return b'd' + b''.join([bencode(k) + bencode(v) for k, v in items]) + b'e'
    else:
        raise TypeError("Unsupported type")