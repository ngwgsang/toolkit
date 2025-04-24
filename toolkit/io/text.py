import re

def clean_text(text):
    return re.sub(r"\s+", " ", text.strip())

def split_sentences(text):
    return re.split(r"(?<=[.!?]) +", text)

def is_ascii(text):
    return all(ord(c) < 128 for c in text)

def remove_chars(
    text, 
    blacklist=None, 
    whitelist=(
        "aăâbcdđeêghiklmnoôơpqrstuưvxy"
        "AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY"
        "áàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệ"
        "íìỉĩịóòỏõọốồổỗộớờởỡợúùủũụ"
        "ứừửữựýỳỷỹỵÁÀẢÃẠẮẰẲẴẶẤẦẨẪẬ"
        "ÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌỐỒỔỖỘ"
        "ỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ"
        "0123456789 "
    )):
    if whitelist is not None:
        return ''.join(char for char in text if char in whitelist)
    elif blacklist is not None:
        return ''.join(char for char in text if char not in blacklist)
    else:
        return text

def remove_sw(text, sw):
    words = text.split()
    filtered = [word for word in words if word.lower() not in sw]
    return ' '.join(filtered)