def amount_input():
    comment_text = """Įrašykite pajamas arba išlaidas (su '-' ženklu)
    (tusčia eilutė, pradės įrašinėti sumą į failą): """
    user_text = input(comment_text)
    amount_to_save = []
    while user_text != "":
        try:
            user_text = float(user_text)
        except ValueError as e:
            raise e
        amount_to_save.append(user_text)
        user_text = input(comment_text)
    return amount_to_save