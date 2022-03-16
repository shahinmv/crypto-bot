def start_bot(input_texts):
    user_message = str(input_texts).lower()
    if input_texts in ('necesen', 'necesen?', 'netersen', 'netersen?', 'veziyyet?', 'veziyyet'):
        return("Shukur salamatciliq")
    elif input_texts in ('aye', 'AYE'):
        return("Jizn voram!")
    else:
        return("Basha dushmedim qaqa")