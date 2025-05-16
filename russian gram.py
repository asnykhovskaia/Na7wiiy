import random
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

nouns = {
    "страна": ['balad', 'bilād'],
    "город": ['madīnat', 'mudun'],
    "дом": ['bayt', 'buyūt'],
    "улица": ['šāriʿ', 'šawāriʿu'],
    "школа": ['madrasat', 'madārisu'],
    "университет": ['ǧāmiʿat', 1],
    "книга": ['kitāb', 'kutub'],
    "ручка": ['qalam', 'ʾaqlām'],
    "стол": ['maktab', 'makātibu'],
    "стул": ['kursīy', 'karāsīyu'],
    "комната": ['ġurfat', 1],
    "дверь": ['bāb', 'ʾabwāb'],
    "окно": ['nāfiḏat', 1],
    "час": ['sāʿat', 1],
    "день": ['yawm', 'ʾayyām'],
    "ночь": ['layl', 0],
    "неделя": ['ʾusbūʿ', 'ʾasābīʿ'],
    "месяц": ['šahr', 'ʾašhur'],
    "год": ['sanat', 'sanawāt'],
    "имя": ['ʾism', 'ʾasmāʾ'],
    "утро": ['ṣabāḥ', 0],
    "адрес": ['ʿunwān', 'ʿanāwīn'],
    "номер": ['raqm', 'ʾarqām'],
    "письмо": ['risālat', 'rasāʾilu'],
    "язык": ['luġat', 1],
    "работа": ['ʿamal', 'ʾaʿmāl'],
    "друг": ['ṣadīq', 'ʾaṣdiqāʾu'],
    "семья": ['ʾāʿilat', 1],
    "отец": ['ʾab', 'ʾābāʾ'],
    "мать": ['ʾumm', 'ʾummāhāt'],
    "брат": ['ʾaḫ', 'ʾiḫwān'],
    "сестра": ['ʾuḫt', 'ʾaḫawāt'],
    "муж": ['zawǧ', 'ʾazwāǧ'],
    "жена": ['zawǧat', 1],
    "ребенок": ['ṭifl', 'ʾaṭfāl'],
    "человек": ['ʾinsān', 'nās'],
    "мир": ['salām', 0],
    "вопрос": ['suʾāl', 'ʾasʾilat'],
    "ответ": ['ǧawāb', 'ʾaǧwibat'],
    "словарь": ['qāmūs', 'qawāmisu'],
    "предложение": ['ǧumlat', 1],
    "класс": ['ṣaff', 'ʾaṣuff'],
    "доска": ['sabūrat', 1],
    "карта": ['ḫarīṭat', 1],
    "фотография": ['ṣūrat', 'ṣuwar'],
    "новость": ['ḫabar', 'ʾaḫbār'],
    "история": ['qiṣṣat', 1],
    "религия": ['dīn', 'ʾadyān'],
    "план": ['ḫiṭṭat', 1],
    "спорт": ['riyāḍat', 1],
    "искусство": ['fann', 'funūn'],
    "культура": ['ṯaqāfat', 1],
    "еда": ['ṭaʿām', 0],
    "вода": ['māʾ', 0],
    "рынок": ['sūq', 'ʾaswāq'],
    "деньги": ['māl', 0],
    "банк": ['bank', 'bunūk'],
    "почта": ['barīd', 0],
    "аэропорт": ['maṭār', 1],
    "автобус": ['ḥāfilat', 1],
    "машина": ['sayyārat', 1],
    "поезд": ['qiṭār', 'qiṭārāt'],
    "самолет": ['ṭāʾirat', 1],
    "корабль": ['safīnat', 'sufun'],
    "путешествие": ['safar', 0],
    "время": ['waqt', 'ʾawqāt'],
    "место": ['makān', 'ʾamākinu'],
    "цвет": ['lawn', 'ʾalwān'],
    "размер": ['ḥaǧm', 'ʾaḥǧām'],
    "форма": ['šakl', 'ʾaškal'],
    "материал": ['māddat', 1],
    "жара": ['ḥarr', 0],
    "погода": ['ǧaww', 0],
    "ветер": ['rīḥ', 'riyāḥ'],
    "дождь": ['maṭar', 'ʾamṭār'],
    "снег": ['ṯalǧ', 0],
    "гора": ['ǧabal', 'ǧibāl'],
    "река": ['nahr', 'ʾanhār'],
    "море": ['baḥr', 'biḥār'],
    "лес": ['ġābat', 1],
    "животное": ['ḥaywān', 'ḥaywānāt'],
    "птица": ['ṭāʾir', 'ṭuyūr'],
    "растение": ['nabāt', 'nabāt'],
    "цветок": ['zahrat', 1],
    "солнце": ['šams', 0],
    "луна": ['qamar',  0],
    "звезда": ['naǧm', 'nuǧūm'],
    "небо": ['samāʾ', 0],
    "земля": ['ʾarḍ', 0],
    "воздух": ['hawāʾ',  0],
    "мир": ['salām',  0],
    "свобода": ['ḥurriyyat', 1],
    "право": ['ḥaqq', 'ḥuqūq'],
    "дело": ['ʾamr', 'ʾumūr'],
    "надежда": ['ʾamal',  0],
    "страх": ['ḫawf',  0],
    "гнев": ['ġaḍab',  0],
    "радость": ['faraḥ', 0],
    "ум": ['ʿaql',  0],
    "сердце": ['qalb', 'qulūb'],
    "душа": ['nafs', 'ʾanfus'],
    "тело": ['ǧism', 'ʾaǧsām'],
    "голова": ['raʾs', 'ruʾūs'],
    "лицо": ['waǧh', 'wuǧūh'],
    "глаз": ['ʿayn', 'ʾaʿyun'],
    "ухо": ['ʾuḏun', 'ʾāḏān'],
    "нос": ['ʾanf', 'ʾunūf'],
    "рука": ['yad', 0],
    "нога": ['riǧl', 'ʾarǧul'],
    "доктор": ['ṭabīb', 'ʾaṭibbāʾu'],
    "инженер": ['muhandisu', 1],
    "учитель": ['mudarrisu', 1],
    "студент": ['ṭālib', 'ṭullāb'],
    "полицейский": ['šurṭīy', 1],
    "солдат": ['ǧundīy', 1]
}

nouns_anim_m= [
    "друг",
    "отец",
    "брат",
    "муж",
    "человек",
    "доктор",
    "инженер",
    "учитель",
    "студент",
    "полицейский",
    "солдат"
]

nouns_anim_f = [
    "мать",
    "сестра",
    "жена"
]

nouns_unanim_m = [
    "город",
    "дом",
    "университет",
    "книга",
    "ручка",
    "стол",
    "стул",
    "час",
    "день",
    "номер",
    "язык",
    "мир",
    "вопрос",
    "словарь",
    "класс",
    "план",
    "спорт",
    "искусство",
    "рынок",
    "банк",
    "аэропорт",
    "автобус",
    "поезд",
    "самолет",
    "корабль",
    "ветер",
    "дождь",
    "снег",
    "гора",
    "река",
    "море",
    "лес",
    "гнев",
    "ум",
    "нос",
    "самолет"
]

nouns_unanim_f = [
    "страна",
    "школа",
    "комната",
    "дверь",
    "окно",
    "ночь",
    "неделя",
    "месяц",
    "год",
    "имя",
    "утро",
    "адрес",
    "письмо",
    "работа",
    "семья",
    "религия",
    "доска",
    "карта",
    "фотография",
    "новость",
    "история",
    "культура",
    "еда",
    "почта",
    "машина",
    "путешествие",
    "время",
    "место",
    "форма",
    "вода",
    "жара",
    "погода",
    "земля",
    "война",
    "свобода",
    "право",
    "дело",
    "надежда",
    "страх",
    "радость",
    "душа",
    "голова",
    "рука",
    "нога",
    "луна",
    "звезда",
    "небо",
    "улица"
]

nouns_locativable = [
    "страна",
    "город",
    "дом",
    "улица",
    "школа",
    "университет",
    "комната",
    "класс",
    "рынок",
    "банк",
    "почта",
    "аэропорт",
    "автобус",
    "машина",
    "поезд",
    "самолет",
    "корабль",
    "гора",
    "река",
    "море",
    "лес",
    "луна",
    "небо",
    "земля",
    "воздух"
]
verbs = {
    "убить": ['balad'],
    "забыть": ['madīnat'],
    "простить": ['bayt'],
    "понять": ['šāriʿ'],
    "подумать": ['madrasat'],
    "повеситься": ['ǧāmiʿat']
}

verbs_trans = [
    "убить",
    "забыть"
]
adjs = {
    "белый": ['balad'],
    "зелёный": ['madīnat'],
    "красный": ['bayt'],
    "весёлый": ['šāriʿ'],
    "арабский": ['madrasat'],
    "красивый": ['ǧāmiʿat']
}
determiners = {
    "этот": ['balad'],
    "тот": ['madīnat'],
}
prepositions = {
    "в": ['balad'],
    "на": ['madīnat'],
}

while True:
    noun_nom_syr = random.choice(list(nouns.items()))[0]
    if noun_nom_syr in nouns_anim_f or noun_nom_syr in nouns_anim_m:
        break
noun_nom_number_choice = random.choice(['sing', 'plur', 'plur'])
noun_nom = morph.parse(noun_nom_syr)[0].inflect({noun_nom_number_choice}).word
dual_nom_yes = ""
if noun_nom_number_choice == 'plur':
    dual_nom_choice = random.choice([1, 2])
    if dual_nom_choice == 1:
        dual_nom_yes = "(дв.)"
dual_nom = f" {dual_nom_yes}" if dual_nom_yes else ""

while True:
    noun_acc_syr = random.choice(list(nouns.items()))[0]
    if noun_acc_syr in nouns_unanim_m or noun_acc_syr in nouns_unanim_f:
        break

noun_acc_number_choice = random.choice(['sing', 'plur', 'plur'])
noun_acc = morph.parse(noun_acc_syr)[0].inflect({'accs', noun_acc_number_choice}).word
dual_acc_yes = ""
if noun_acc_number_choice == 'plur':
    dual_acc_choice = random.choice([1, 2])
    if dual_acc_choice == 1:
        dual_acc_yes = "(дв.)"
dual_acc = f" {dual_acc_yes}" if dual_acc_yes else ""

while True:
    noun_gen_syr = random.choice(list(nouns.items()))[0]
    if noun_gen_syr in nouns_anim_f or noun_gen_syr in nouns_anim_m:
        break
noun_gen_number_choice = random.choice(['sing', 'plur', 'plur'])
noun_gen = morph.parse(noun_gen_syr)[0].inflect({'gent', noun_gen_number_choice}).word
dual_gen_yes = ""
if noun_gen_number_choice == 'plur':
    dual_gen_choice = random.choice([1, 2])
    if dual_gen_choice == 1:
        dual_gen_yes = "(дв.)"
dual_gen = f" {dual_gen_yes}" if dual_gen_yes else ""

while True:
    noun_loc_syr = random.choice(list(nouns.items()))[0]
    if noun_loc_syr in nouns_locativable:
        break
noun_loc_number_choice = random.choice(['sing', 'plur', 'plur'])
noun_loc = morph.parse(noun_loc_syr)[0].inflect({'loct', noun_loc_number_choice}).word
dual_loc_yes = ""
if noun_loc_number_choice == 'plur':
    dual_loc_choice = random.choice([1, 2])
    if dual_loc_choice == 1:
        dual_loc_yes = "(дв.)"
dual_loc = f" {dual_loc_yes}" if dual_loc_yes else ""

verb = random.choice(list(verbs.items()))[0]
verb_forms = [
    form.word for form in morph.parse(verb)[0].lexeme
    if 'VERB' in form.tag and 'impr' not in form.tag
]
verb_personal = random.choice(verb_forms)

determiner = random.choice(list(determiners.keys()))
preposition = random.choice(list(prepositions.keys()))


def structure_VP():
    structure_VP_podtype = random.choice([1, 2, 3])

    if structure_VP_podtype == 1:
        structure_NP_podtype = random.choice([1, 2])
        if structure_NP_podtype == 1:
            amount_adj = random.choice([1, 2, 3])
            used_adj = random.sample(sorted(adjs.keys()), amount_adj)
            if amount_adj == 3:
                used_adj[0] = determiner
            adj_NP1_gender_check = morph.parse(noun_acc)[0].tag.gender
            adj_NP1_animacy_check = morph.parse(noun_acc)[0].tag.animacy
            if adj_NP1_animacy_check == None:
                adj_NP1_animacy_check = 'inan'

            if noun_acc_number_choice == 'sing':
                used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                    {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
            else:
                used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                    {noun_acc_number_choice, adj_NP1_animacy_check, 'accs'})
            if used_adj_modified_1 is not None:
                used_adj[0] = used_adj_modified_1.word
            else:
                if noun_acc_number_choice == 'sing':
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect({adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                else:
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect({noun_acc_number_choice, 'accs'})
                if used_adj_modified_1 is not None:
                    used_adj[0] = used_adj_modified_1.word
            if amount_adj > 1:
                if noun_acc_number_choice == 'sing':
                    used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                        {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                else:
                    used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                        {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                if used_adj_modified_2 is not None:
                    used_adj[1] = used_adj_modified_2.word
                else:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect({adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                            {noun_acc_number_choice, 'accs'})
                    if used_adj_modified_2 is not None:
                        used_adj[1] = used_adj_modified_2.word
            if amount_adj > 2:
                if noun_acc_number_choice == 'sing':
                    used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                        {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                else:
                    used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                        {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                if used_adj_modified_3 is not None:
                    used_adj[2] = used_adj_modified_3.word
                else:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect({adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                            {noun_acc_number_choice, 'accs'})
                    if used_adj_modified_3 is not None:
                        used_adj[2] = used_adj_modified_3.word
            NP = f"{' '.join(used_adj)} {noun_acc}{dual_acc}"
        elif structure_NP_podtype == 2:
          adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
          adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
          if adjective_NP2 != False:
            if noun_loc_number_choice == 'sing':
                adjective_NP2 = morph.parse(adjective_NP2)[0].inflect({adj_NP2_gender_check, noun_loc_number_choice, 'loct'}).word
            else:
                adjective_NP2 = morph.parse(adjective_NP2)[0].inflect(
                    {noun_loc_number_choice, 'loct'}).word

          adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

          NP = f"{noun_acc}{dual_acc} {preposition} {adjective_NP2_return} {noun_loc}{dual_loc}"

        while True:
            verb = random.choice(list(verbs.keys()))
            if verb in verbs_trans:
                break

        return f"{verb} {NP}"

    elif structure_VP_podtype == 2:
        verb = random.choice(list(verbs.items()))[0]
        verb_forms = [
            form.word for form in morph.parse(verb)[0].lexeme
            if 'VERB' in form.tag and 'impr' not in form.tag and 'past' not in form.tag
        ]
        verb_personal = random.choice(verb_forms)
        return verb_personal

    elif structure_VP_podtype == 3:
            structure_NP_podtype = random.choice([1, 2])
            if structure_NP_podtype == 1:
                amount_adj = random.choice([1, 2, 3])
                used_adj = random.sample(sorted(adjs.keys()), amount_adj)
                if amount_adj == 3:
                    used_adj[0] = determiner
                adj_NP1_gender_check = morph.parse(noun_acc)[0].tag.gender
                adj_NP1_animacy_check = morph.parse(noun_acc)[0].tag.animacy
                if adj_NP1_animacy_check == None:
                    adj_NP1_animacy_check = 'inan'
                if noun_acc_number_choice == 'sing':
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                        {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                else:
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                        {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                if used_adj_modified_1 is not None:
                    used_adj[0] = used_adj_modified_1.word
                else:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect({adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                            {noun_acc_number_choice, 'accs'})
                    if used_adj_modified_1 is not None:
                        used_adj[0] = used_adj_modified_1.word
                if amount_adj > 1:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                            {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                    else:
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                            {noun_acc_number_choice, adj_NP1_animacy_check, 'accs'})
                    if used_adj_modified_2 is not None:
                        used_adj[1] = used_adj_modified_2.word
                    else:
                        if noun_acc_number_choice == 'sing':
                            used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect({adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                        else:
                            used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                                {noun_acc_number_choice, 'accs'})
                        if used_adj_modified_2 is not None:
                            used_adj[1] = used_adj_modified_2.word
                if amount_adj > 2:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                            {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                            {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    if used_adj_modified_3 is not None:
                        used_adj[2] = used_adj_modified_3.word
                    else:
                        if noun_acc_number_choice == 'sing':
                            used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                                {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                        else:
                            used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                                {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})

                        if used_adj_modified_3 is not None:
                            used_adj[2] = used_adj_modified_3.word

                NP = f"{' '.join(used_adj)} {noun_acc}{dual_acc}"

            elif structure_NP_podtype == 2:
              adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
              adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
              if adjective_NP2 != False:
                if noun_loc_number_choice == 'sing':
                    adjective_NP2 = morph.parse(adjective_NP2)[0].inflect({adj_NP2_gender_check, noun_loc_number_choice, 'loct'}).word
                else:
                    adjective_NP2 = morph.parse(adjective_NP2)[0].inflect(
                        {noun_loc_number_choice, 'loct'}).word

              adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

              NP = f"{noun_acc}{dual_acc} {preposition} {adjective_NP2_return} {noun_loc}{dual_loc}"

            while True:
                verb = random.choice(list(verbs.keys()))
                if verb in verbs_trans:
                    break
            verb_forms = [
                form.word for form in morph.parse(verb)[0].lexeme
                if 'VERB' in form.tag and 'impr' not in form.tag and 'past' not in form.tag
            ]
            verb_personal = random.choice(verb_forms)

            return f"{verb_personal} {NP}"



def structure_NP():
    structure_NP_podtype = random.choice([1, 2, 3, 4, 5])
    if structure_NP_podtype == 1:
        amount_adj = random.choice([1, 2, 3])
        used_adj = random.sample(sorted(adjs.keys()), amount_adj)
        if amount_adj == 3:
            used_adj[0] = determiner
        adj_NP1_gender_check = morph.parse(noun_nom)[0].tag.gender
        if noun_nom_number_choice == 'sing':
            used_adj[0] = morph.parse(used_adj[0])[0].inflect({adj_NP1_gender_check, 'nomn'}).word
        else:
            used_adj[0] = morph.parse(used_adj[0])[0].inflect({noun_nom_number_choice, 'nomn'}).word

        if amount_adj > 1:
            if noun_nom_number_choice == 'sing':
                used_adj[1] = morph.parse(used_adj[1])[0].inflect({adj_NP1_gender_check, 'nomn'}).word
            else:
                used_adj[1] = morph.parse(used_adj[1])[0].inflect({noun_nom_number_choice, 'nomn'}).word

        if amount_adj > 2:
            if noun_nom_number_choice == 'sing':
                used_adj[2] = morph.parse(used_adj[2])[0].inflect({adj_NP1_gender_check, 'nomn'}).word
            else:
                used_adj[2] = morph.parse(used_adj[2])[0].inflect({noun_nom_number_choice, 'nomn'}).word

        return f"{' '.join(used_adj)} {noun_nom}{dual_nom}"

    elif structure_NP_podtype == 2:
      adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
      adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
      if adjective_NP2 != False:
        if noun_loc_number_choice == 'sing':
            adjective_NP2 = morph.parse(adjective_NP2)[0].inflect({adj_NP2_gender_check, noun_loc_number_choice, 'loct'}).word
        else:
            adjective_NP2 = morph.parse(adjective_NP2)[0].inflect(
                {noun_loc_number_choice, 'loct'}).word

      adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

      return f"{noun_nom}{dual_nom} {preposition} {adjective_NP2_return} {noun_loc}{dual_loc}"

    elif structure_NP_podtype == 3:
        adjective_NP3_1 = random.choice([False, random.choice(list(adjs.keys()))])

        adj_NP3_1_gender_check = morph.parse(noun_nom)[0].tag.gender

        if adjective_NP3_1 != False:
            if noun_nom_number_choice == 'sing':
                adjective_NP3_1 = morph.parse(adjective_NP3_1)[0].inflect({adj_NP3_1_gender_check}).word
            else:
                adjective_NP3_1 = morph.parse(adjective_NP3_1)[0].inflect({noun_nom_number_choice}).word
        adjective_NP3_1_return = f" {adjective_NP3_1}" if adjective_NP3_1 else ""

        adjective_NP3_2 = random.choice([False, random.choice(list(adjs.keys()))])
        adj_NP3_2_gender_check = morph.parse(noun_gen)[0].tag.gender
        adj_NP3_2_animacy_check = morph.parse(noun_gen)[0].tag.animacy
        if adj_NP3_2_animacy_check == None:
            adj_NP3_2_animacy_check = 'inan'
        adjective_NP3_2_modified = None
        adjective_NP3_2_return = ""

        if adjective_NP3_2:
            if noun_gen_number_choice == 'sing':
                adjective_NP3_2_modified = morph.parse(adjective_NP3_2)[0].inflect(
                    {adj_NP3_2_gender_check, adj_NP3_2_animacy_check, noun_gen_number_choice, 'gent'})
            else:
                adjective_NP3_2_modified = morph.parse(adjective_NP3_2)[0].inflect(
                    {adj_NP3_2_animacy_check, noun_gen_number_choice, 'gent'})

            if adjective_NP3_2_modified is None:
                if noun_gen_number_choice == 'sing':
                    adjective_NP3_2_modified = morph.parse(adjective_NP3_2)[0].inflect(
                        {adj_NP3_2_gender_check, noun_gen_number_choice, 'gent'})
                else:
                    adjective_NP3_2_modified = morph.parse(adjective_NP3_2)[0].inflect(
                        {noun_gen_number_choice, 'gent'})

            if adjective_NP3_2_modified:
              adjective_NP3_2_return = f" {adjective_NP3_2_modified.word}"

        return f"{adjective_NP3_1_return} {noun_nom}{dual_nom} {adjective_NP3_2_return} {noun_gen}{dual_gen}"

    elif structure_NP_podtype == 4:
        while True:
            verb = random.choice(list(verbs.keys()))
            if verb in verbs_trans:
                break
        verb_forms = [
            form.word for form in morph.parse(verb)[0].lexeme
            if 'VERB' in form.tag and 'impr' not in form.tag
        ]
        verb_personal = random.choice(verb_forms)
        VP_NP4_num = random.choice([1, 2])
        if VP_NP4_num == 1:
            structure_NP_podtype = random.choice([1, 2])
            if structure_NP_podtype == 1:
                amount_adj = random.choice([1, 2, 3])
                used_adj = random.sample(sorted(adjs.keys()), amount_adj)
                if amount_adj == 3:
                    used_adj[0] = determiner
                adj_NP1_gender_check = morph.parse(noun_acc)[0].tag.gender
                adj_NP1_animacy_check = morph.parse(noun_acc)[0].tag.animacy
                if adj_NP1_animacy_check == None:
                    adj_NP1_animacy_check = 'inan'
                if noun_acc_number_choice == 'sing':
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                        {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                else:
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                        {noun_acc_number_choice, adj_NP1_animacy_check, 'accs'})
                if used_adj_modified_1 is not None:
                    used_adj[0] = used_adj_modified_1.word
                else:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                            {adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect({noun_acc_number_choice, 'accs'})
                    if used_adj_modified_1 is not None:
                        used_adj[0] = used_adj_modified_1.word
                if amount_adj > 1:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                            {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                            {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    if used_adj_modified_2 is not None:
                        used_adj[1] = used_adj_modified_2.word
                    else:
                        if noun_acc_number_choice == 'sing':
                            used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                                {adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                        else:
                            used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                                {noun_acc_number_choice, 'accs'})
                        if used_adj_modified_2 is not None:
                            used_adj[1] = used_adj_modified_2.word
                if amount_adj > 2:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                            {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                            {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    if used_adj_modified_3 is not None:
                        used_adj[2] = used_adj_modified_3.word
                    else:
                        if noun_acc_number_choice == 'sing':
                            used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                                {adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                        else:
                            used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                                {noun_acc_number_choice, 'accs'})
                        if used_adj_modified_3 is not None:
                            used_adj[2] = used_adj_modified_3.word
                NP = f"{' '.join(used_adj)} {noun_acc}{dual_acc}"
            elif structure_NP_podtype == 2:
                adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
                adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
                if adjective_NP2 != False:
                    if noun_loc_number_choice == 'sing':
                        adjective_NP2 = morph.parse(adjective_NP2)[0].inflect(
                            {adj_NP2_gender_check, noun_loc_number_choice, 'loct'}).word
                    else:
                        adjective_NP2 = morph.parse(adjective_NP2)[0].inflect(
                            {noun_loc_number_choice, 'loct'}).word

                adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

                NP = f"{noun_acc}{dual_acc} {preposition} {adjective_NP2_return} {noun_loc}{dual_loc}"
            noun_gender_check = morph.parse(noun_nom)[0].tag.gender
            
            verb_person_check = morph.parse(verb_personal)[0].tag.person
            verb_tense_check = morph.parse(verb_personal)[0].tag.tense

            grammemes = set()
            if verb_person_check != '3per' and verb_tense_check != 'past':
                grammemes = {'3per'}
            if noun_nom_number_choice:
                grammemes.add(noun_nom_number_choice)
            else:
                grammemes.add('sing')
            if noun_nom_number_choice == 'sing' and verb_tense_check == 'past' and noun_gender_check:
                grammemes.add(noun_gender_check)
            inflected_verb = morph.parse(verb_personal)[0].inflect(grammemes).word
            VP_NP4 = f"{inflected_verb} {NP}"

        elif VP_NP4_num == 2:
            noun_gender_check = morph.parse(noun_nom)[0].tag.gender
            verb_person_check = morph.parse(verb_personal)[0].tag.person
            verb_tense_check = morph.parse(verb_personal)[0].tag.tense

            grammemes = set()
            if verb_person_check != '3per' and verb_tense_check != 'past':
                grammemes = {'3per'}
            if noun_nom_number_choice:
                grammemes.add(noun_nom_number_choice)
            else:
                grammemes.add('sing')
            if noun_nom_number_choice == 'sing' and verb_tense_check == 'past' and noun_gender_check:
                grammemes.add(noun_gender_check)
            inflected_verb = morph.parse(verb_personal)[0].inflect(grammemes).word
            VP_NP4 = inflected_verb

        if noun_nom_number_choice == 'plur':
            that_NP4 = 'которые'
        else:
            that4_gender_check = morph.parse(noun_nom)[0].tag.gender
            that4_gender_forms = {
                'masc': 'который',
                'femn': 'которая',
                'neut': 'которое'
            }
            that_NP4 = that4_gender_forms.get(that4_gender_check)
        return f"{noun_nom}{dual_nom}, {that_NP4} {VP_NP4}"

    elif structure_NP_podtype == 5:
        while True:
            verb = random.choice(list(verbs.keys()))
            if verb in verbs_trans:
                break
        verb_forms = [
            form.word for form in morph.parse(verb)[0].lexeme
            if 'VERB' in form.tag and 'impr' not in form.tag
        ]
        verb_personal = random.choice(verb_forms)
        VP_NP5_num = random.choice([1, 2])
        if VP_NP5_num == 1:
            structure_NP_podtype = random.choice([1, 2])
            if structure_NP_podtype == 1:
                amount_adj = random.choice([1, 2, 3])
                used_adj = random.sample(sorted(adjs.keys()), amount_adj)
                if amount_adj == 3:
                    used_adj[0] = determiner
                adj_NP1_gender_check = morph.parse(noun_nom)[0].tag.gender
                adj_NP1_animacy_check = morph.parse(noun_nom)[0].tag.animacy
                if adj_NP1_animacy_check == None:
                    adj_NP1_animacy_check = 'inan'
                if noun_acc_number_choice == 'sing':
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                        {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                else:
                    used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                        {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                if used_adj_modified_1 is not None:
                    used_adj[0] = used_adj_modified_1.word
                else:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                            {adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                            {noun_acc_number_choice, 'accs'})
                    if used_adj_modified_1 is not None:
                        used_adj[0] = used_adj_modified_1.word
                if amount_adj > 1:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                            {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                            {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    if used_adj_modified_2 is not None:
                        used_adj[1] = used_adj_modified_2.word
                    else:
                        if noun_acc_number_choice == 'sing':
                            used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                                {adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                        else:
                            used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                                {noun_acc_number_choice, 'accs'})
                        if used_adj_modified_2 is not None:
                            used_adj[1] = used_adj_modified_2.word
                if amount_adj > 2:
                    if noun_acc_number_choice == 'sing':
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                            {adj_NP1_gender_check, adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    else:
                        used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                            {adj_NP1_animacy_check, noun_acc_number_choice, 'accs'})
                    if used_adj_modified_3 is not None:
                        used_adj[2] = used_adj_modified_3.word
                    else:
                        if noun_acc_number_choice == 'sing':
                            used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                                {adj_NP1_gender_check, noun_acc_number_choice, 'accs'})
                        else:
                            used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                                {noun_acc_number_choice, 'accs'})
                        if used_adj_modified_3 is not None:
                            used_adj[2] = used_adj_modified_3.word

                NP = f"{' '.join(used_adj)} {noun_nom}{dual_nom}"

            elif structure_NP_podtype == 2:
                adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
                adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
                if adjective_NP2 != False:
                    if noun_loc_number_choice == 'sing':
                        adjective_NP2 = morph.parse(adjective_NP2)[0].inflect(
                            {adj_NP2_gender_check, noun_loc_number_choice, 'loct'}).word
                    else:
                        adjective_NP2 = morph.parse(adjective_NP2)[0].inflect(
                            {noun_loc_number_choice, 'loct'}).word

                adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

                NP = f"{noun_acc}{dual_acc} {preposition} {adjective_NP2_return} {noun_loc}{dual_loc}"

            noun_gender_check = morph.parse(noun_nom)[0].tag.gender


            verb_person_check = morph.parse(verb_personal)[0].tag.person
            verb_tense_check = morph.parse(verb_personal)[0].tag.tense


            grammemes = set()
            if verb_person_check != '3per' and verb_tense_check != 'past':
                grammemes = {'3per'}
            if noun_nom_number_choice:
                grammemes.add(noun_nom_number_choice)
            else:
                grammemes.add('sing')
            if noun_nom_number_choice == 'sing' and verb_tense_check == 'past' and noun_gender_check:
                grammemes.add(noun_gender_check)
            inflected_verb = morph.parse(verb_personal)[0].inflect(grammemes).word
            VP_NP5 = f"{inflected_verb} {noun_nom}{dual_nom}"

        elif VP_NP5_num == 2:
            verb_forms = [
                form.word for form in morph.parse(verb)[0].lexeme
                if 'VERB' in form.tag and 'impr' not in form.tag and 'past' not in form.tag
            ]
            verb_personal = random.choice(verb_forms)
            VP_NP5 = verb_personal

        that5_gender_check = morph.parse(noun_nom)[0].tag.gender
        that5_animacy_check = morph.parse(noun_nom)[0].tag.animacy

        if noun_nom_number_choice == 'plur':
            that_NP5 = 'которые' if that5_animacy_check is None else 'которых'
        else:
            if that5_gender_check == 'masc':
                that_NP5 = 'который' if that5_animacy_check is None else 'которого'
            elif that5_gender_check == 'femn':
                that_NP5 = 'которую'
            elif that5_gender_check == 'neut':
                that_NP5 = 'которое'

        return f"{noun_nom}{dual_nom}, {that_NP5} {VP_NP5}"


structure_choice = random.choice([1, 2])

if structure_choice == 1:
    res = structure_VP()
elif structure_choice == 2:
    res = structure_NP()

print(' '.join(res.split()))
