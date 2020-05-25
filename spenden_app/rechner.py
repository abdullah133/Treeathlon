def berechnung_co2_ausfuehren(request,form):
    print('Juhuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
    frage = form.cleaned_data.get('frage')
    frage_2 = form.cleaned_data.get('frage_2')
    frage_3 = form.cleaned_data.get('frage_3')
    frage_4 = form.cleaned_data.get('frage_4')
    frage_5 = form.cleaned_data.get('frage_5')
    frage_6 = form.cleaned_data.get('frage_6')
    frage_7 = form.cleaned_data.get('frage_7')
    frage_8 = form.cleaned_data.get('frage_8')
    frage_9 = form.cleaned_data.get('frage_9')
    frage_10 = form.cleaned_data.get('frage_10')
    frage_11 = form.cleaned_data.get('frage_11')
    frage_12 = form.cleaned_data.get('frage_12')
    frage_13 = form.cleaned_data.get('frage_13')
    frage_14 = form.cleaned_data.get('frage_14')
    frage_15 = form.cleaned_data.get('frage_15')
    print('frage:'+str(frage))
    print('frage_3:'+str(frage_3))
    if frage_3 =='OPTION_1':
        print('ich habe 1 gewählt')
        heizwert = 1.2
    elif frage_3 =='OPTION_2':
        heizwert = 0.9
    elif frage_3 =='OPTION_3':
        heizwert = 0.75
    elif frage_3 =='OPTION_4':
        heizwert = 0.4
    elif frage_3 =='OPTION_5':
        heizwert = 0.3
    else:
        heizwert = 1.75


    if frage_4 =='OPTION_1':
        stromart = 1.5
    elif frage_4 =='OPTION_2':
        stromart = 0.95
    elif frage_4 =='OPTION_3':
        stromart = 0.65
    else:
        stromart = 0.09


    if frage_12 =='OPTION_1':
        milchkonsum = 197
    elif frage_12 =='OPTION_2':
        milchkonsum = 427
    elif frage_12 =='OPTION_3':
        milchkonsum = 855
    elif frage_12 =='OPTION_4':
        milchkonsum = 1282
    elif frage_12 =='OPTION_5':
        milchkonsum = 1710
    elif frage_12 =='OPTION_6':
        milchkonsum = 2137
    elif frage_12 =='OPTION_7':
        milchkonsum = 2564
    else:
        milchkonsum = 3000


    if frage_13=='OPTION_1':
        fleischkonsum = 522
    elif frage_13 =='OPTION_2':
        fleischkonsum = 1132
    elif frage_13 =='OPTION_3':
        fleischkonsum = 2264
    elif frage_13 =='OPTION_4':
        fleischkonsum = 3396
    elif frage_13 =='OPTION_5':
        fleischkonsum = 5660
    elif frage_13 =='OPTION_6':
        fleischkonsum = 6792
    elif frage_13 =='OPTION_7':
        fleischkonsum = 7945
    else:
        fleischkonsum = 10884


    if frage_14=='OPTION_1':
        regional_kaufen = 1.08
    elif frage_14 =='OPTION_2':
        regional_kaufen = 1
    else:
        regional_kaufen = 0.95

    if frage_11=='OPTION_1':
        bio_kaufen = 1.1
    elif frage_11 =='OPTION_2':
        bio_kaufen = 1.0
    else:
        bio_kaufen = 0.8


    if frage_15=='OPTION_1':
        verschwenden = 1.08
    elif frage_15 =='OPTION_2':
        verschwenden = 1
    else:
        verschwenden = 0.95

    mein_ergebnis_1 = ((float(frage) * heizwert *180000) + (2000000 * stromart)) / (frage_2*0.7) + (frage_5*2000000)
    mein_ergebnis_2 = (milchkonsum + fleischkonsum) * regional_kaufen * bio_kaufen * verschwenden * 1000
    mein_ergebnis_3 = (frage_6 * frage_8 *60) + (1156 * frage_9 * 900) + (2002 * frage_10 * 1000) -500
    mein_end_ergebnis = mein_ergebnis_1 + mein_ergebnis_2 + float(mein_ergebnis_3)

    footprint = round((mein_end_ergebnis / 10000000) + 2.5, 2)
    spende = round(max(footprint *2, 10),2)
    dict = {'footprint':footprint,
            'spende':spende,
            }
    return dict
