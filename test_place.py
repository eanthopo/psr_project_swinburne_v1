import pandas as pd

df = pd.read_csv('tst.csv',  header=None, sep='~', engine='python')

assoc_col = 47
assoc_list = df.iloc[:,assoc_col]




for i in range(len(assoc_list)):
    assoc_dict = {"EXGAL": "is an extragalactic pulsar", 
                  "SMC": " located in the Small Magellanic Cloud.", 
                  "XRS": "an x-ray source",
                  "GRS": "with a gamma-ray source",
                  "SNR": "a supernova remnant",
                  "GC": "located in the globular cluster",
                  "PWN": " located in the pulsar wind nebula",
                  "LMC": " located in the Large Magellanic Cloud.",
                  "OPT": "the optical counterpart"
                 }
    assoc = str(assoc_list[i]).strip()
    assoc_str_final = ''
    assoc_str = ''
    assoc_str_temp = ''
    assoc_str_temp2 = ''
    assoc_str2 = ''
    count = 0
    count2 = 0
    exgal_flag = False
    if '*' not in assoc:
        if ',' in assoc:
            assoc_split = assoc.split(',')
            for comma_split in assoc_split:
                count += 1
                if ':' in comma_split:
                    colon_split = comma_split.split(':')
                    for item in colon_split:
                        item = str(item).strip()
                        if item in assoc_dict and exgal_flag == True:
                            assoc_str_temp += assoc_dict[item]
                        elif item in assoc_dict and 'EXGAL' == item:
                            assoc_str_temp = assoc_dict[item]
                            exgal_flag = True
                        elif item in assoc_dict:
                            if count == 2:
                                assoc_str_temp += ' with '
                            elif count < len(assoc_split) and count != 1:
                                assoc_str_temp += ' and '
                            if 'with' in assoc_str_temp or 'and' in assoc_str_temp:
                                assoc_str_temp += assoc_dict[item]
                            else:
                                assoc_str_temp = assoc_dict[item]
                        elif item not in assoc_dict and '[' in item and len(item) > 9:
                            bracket = item.index('[')
                            new_item = item[:bracket]
                            assoc_str_temp += ' ' + '(' + str(new_item) + ')'
                            if count < len(assoc_split)-1:
                                assoc_str_temp += ', '
                            elif count < len(assoc_split):
                                assoc_str_temp += ' and '
                            else:
                                assoc_str_temp += '.'
                        elif item not in assoc_dict and '[' in item:
                            if count < len(assoc_split)-1:
                                assoc_str_temp += ', '
                            elif count < len(assoc_split):
                                assoc_str_temp += ' and '
                            assoc_str_temp = assoc_str_temp.replace('the', 'an')
                            if count < len(assoc_split)-1:
                                assoc_str_temp += ', '
                            elif count < len(assoc_split):
                                assoc_str_temp += ' and '
                            else:
                                assoc_str_temp += '.'
                        elif item not in assoc_dict:
                            assoc_str_temp += ' ' + str(item)
                        assoc_str = assoc_str_temp
                    assoc_str_final += assoc_str
        elif ':' in assoc:
            colon_split2 = assoc.split(':')
            for item in colon_split2:
                count2 += 1
                item = str(item).strip()
                if item in assoc_dict and exgal_flag == True:
                    assoc_str_temp2 += assoc_dict[item]
                elif item in assoc_dict and 'EXGAL' == item:
                    # assoc_str_temp2 += ' and has '
                    assoc_str_temp2 = assoc_dict[item]
                    exgal_flag = True
                elif item in assoc_dict:
                    assoc_str_temp2 = ' and has ' + assoc_dict[item]
                elif item not in assoc_dict and '[' in item and len(item) > 9:
                    bracket = item.index('[')
                    new_item = item[:bracket]
                    assoc_str_temp2 += ' ' + '(' + str(new_item) + ')'
                    if count2 < len(colon_split2):
                        assoc_str_temp2 += ' and has '
                    else:
                        assoc_str_temp2 += '. '
                elif item not in assoc_dict and '[' in item:
                    assoc_str_temp2 += ' with '
                    assoc_str_temp2 = assoc_str_temp2.replace('the', 'an')
                elif item not in assoc_dict:
                    assoc_str_temp2 += ' ' + str(item)
                    if count2 < len(colon_split2):
                        assoc_str_temp2 += ' and has '
                    else:
                        assoc_str_temp2 += '. '
            assoc_str2 = assoc_str_temp2
            assoc_str_final += assoc_str2
    print(assoc_str_final)