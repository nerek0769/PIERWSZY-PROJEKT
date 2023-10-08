meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL" : "odpowiedź na żart",
            "SHEESH" : "lekka dezaprobata",
            "CREEPY" : "straszny, złowieszczy",
            "rel" : "oznacza to prawde ",
            "AGGRO" : "stać się agresywnym/zły",
            
}            
            
word=input("wpisz słowo którego nie rozumiesz(pamiętaj aby urzywać durzych liter!): ")           
if word in meme_dict.keys():
    print(meme_dict[word])
    # Co powinniśmy zrobić, jeśli słowo zostało znalezione?
else:
    print("nie ma jeszcze takiego słowa")
    # Co powinniśmy zrobić, jeśli słowo nie zostało znalezione?
