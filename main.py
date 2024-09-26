
def sort_on(dict):
    return dict["count"]

def main():
    """Reads the contents of the "frankenstein.txt" and prints it all to the console"""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        lowered_string = file_contents.lower()
        character_count = {}
        dict_list = []

        for s in lowered_string:
            if s in character_count:
                character_count[s] += 1
            else:
                character_count[s] = 1

        print(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        
        for c in character_count:
            d = {}
            d["char"]=c[0]
            d["count"]=character_count[c]
            if d["char"].isalpha():
                dict_list.append(d)

        dict_list.sort(reverse=True, key=sort_on)
        for d in dict_list:
            char = d["char"]
            num = d["count"]
            if char.isalpha():
                print(f"The {char} character was found {num} times")
                
        print("--- End report ---")
main()
