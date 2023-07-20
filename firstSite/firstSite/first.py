from django.shortcuts import render
from django.http import HttpResponse

# Rendering the home page
def index(request):
    return render(request, 'index.html')

# Function to add an operation to the purpose list
def purpose_setter(purpose, oper):
    if purpose == []:
        purpose.append(oper)
    else:
        purpose.append(f', {oper}')

# Function to analyze text
def analyse(request):
    # Getting the text and the operations that the user may want to perform
    user_txt = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcapitalise = request.POST.get('fullcaps', 'off')
    titlecase = request.POST.get('titlecase', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')

    # Setting up the variables
    analyzed_txt = ""
    purpose = []

    # Checking if the remove punctuation operation is requested
    if removepunc == "on":
        purpose_setter(purpose, 'Remove Punctuation')
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # Removing punctuation characters from the user's text
        for char in user_txt:
            if char not in punctuations:
                analyzed_txt = analyzed_txt + char
        user_txt = analyzed_txt

    # Checking if the title case operation is requested
    if titlecase == "on":
        purpose_setter(purpose, 'Title-Case')
        if analyzed_txt != "":
            # Converting the analyzed text to title case
            analyzed_txt = analyzed_txt.title()
        else:
            # Converting the user's text to title case
            analyzed_txt = user_txt.title()
        user_txt = analyzed_txt

    # Checking if the full capitalization operation is requested
    if fullcapitalise == "on":
        purpose_setter(purpose, 'Upper-Case')
        if analyzed_txt != "":
            # Converting the analyzed text to uppercase
            analyzed_txt = analyzed_txt.upper()
        else:
            # Converting each character in the user's text to uppercase
            for char in user_txt:
                analyzed_txt += char.upper()
        user_txt = analyzed_txt

    # Checking if the new line remover operation is requested
    if new_line_remover == "on":
        purpose_setter(purpose, 'New-Line-Remover')
        # Removing new line characters from the user's text
        for char in user_txt:
            if char != '\n':
                analyzed_txt += char
        user_txt = analyzed_txt


    main_purpose = ""
    params = {
        'purpose': main_purpose.join(purpose),  # Joining the purpose list into a string
        'analyzed_text': analyzed_txt
    }
    return render(request, 'analyse.html', params)
