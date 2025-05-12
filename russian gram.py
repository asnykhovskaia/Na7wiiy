import random
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

nouns = {
    "страна": ['balad'],
    "город": ['madīnat'],
    "дом": ['bayt'],
    "улица": ['šāriʿ'],
    "школа": ['madrasat'],
    "университет": ['ǧāmiʿat'],
    "мама": ['bayt'],
    "папа": ['šāriʿ'],
    "Миша": ['madrasat'],
    "Филипп": ['ǧāmiʿat']
}
verbs = {
    "убить": ['balad'],
    "забыть": ['madīnat'],
    "простить": ['bayt'],
    "понять": ['šāriʿ'],
    "подумать": ['madrasat'],
    "повеситься": ['ǧāmiʿat']
}
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

noun_nom_syr = random.choice(list(nouns.items()))[0]
noun_nom_number_choice = random.choice(['sing', 'plur', 'plur'])
noun_nom = morph.parse(noun_nom_syr)[0].inflect({noun_nom_number_choice}).word
dual_nom_yes = ""
if noun_nom_number_choice == 'plur':
    dual_nom_choice = random.choice([1, 2])
    if dual_nom_choice == 1:
        dual_nom_yes = "(дв.)"
dual_nom = f" {dual_nom_yes}" if dual_nom_yes else ""

noun_acc_syr = random.choice(list(nouns.items()))[0]
noun_acc_number_choice = random.choice(['sing', 'plur', 'plur'])
noun_acc = morph.parse(noun_acc_syr)[0].inflect({'accs', noun_acc_number_choice}).word
dual_acc_yes = ""
if noun_acc_number_choice == 'plur':
    dual_acc_choice = random.choice([1, 2])
    if dual_acc_choice == 1:
        dual_acc_yes = "(дв.)"
dual_acc = f" {dual_acc_yes}" if dual_acc_yes else ""

noun_gen_syr = random.choice(list(nouns.items()))[0]
noun_gen_number_choice = random.choice(['sing', 'plur', 'plur'])
noun_gen = morph.parse(noun_gen_syr)[0].inflect({'gent', noun_gen_number_choice}).word
dual_gen_yes = ""
if noun_gen_number_choice == 'plur':
    dual_gen_choice = random.choice([1, 2])
    if dual_gen_choice == 1:
        dual_gen_yes = "(дв.)"
dual_gen = f" {dual_gen_yes}" if dual_gen_yes else ""

noun_loc_syr = random.choice(list(nouns.items()))[0]
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

            used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
            if used_adj_modified_1 is not None:
                used_adj[0] = used_adj_modified_1.word
            else:
                used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect({adj_NP1_gender_check, 'accs'})
                if used_adj_modified_1 is not None:
                    used_adj[0] = used_adj_modified_1.word
            if amount_adj > 1:
                used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                    {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                if used_adj_modified_2 is not None:
                    used_adj[1] = used_adj_modified_2.word
                else:
                    used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect({adj_NP1_gender_check, 'accs'})
                    if used_adj_modified_2 is not None:
                        used_adj[1] = used_adj_modified_2.word
            if amount_adj > 2:
                used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                    {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                if used_adj_modified_3 is not None:
                    used_adj[2] = used_adj_modified_3.word
                else:
                    used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect({adj_NP1_gender_check, 'accs'})
                    if used_adj_modified_3 is not None:
                        used_adj[2] = used_adj_modified_3.word
            NP = f"{' '.join(used_adj)} {noun_acc}{dual_acc}"
        elif structure_NP_podtype == 2:
            adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
            adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
            if adjective_NP2 != False:
                adjective_NP2 = morph.parse(adjective_NP2)[0].inflect({adj_NP2_gender_check, 'loct'}).word

            adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

            NP = f"{noun_acc}{dual_acc} {preposition} {noun_loc}{dual_loc}{adjective_NP2_return}"

        return f"{verb} {NP}"

    elif structure_VP_podtype == 2:
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
            used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
            if used_adj_modified_1 is not None:
                used_adj[0] = used_adj_modified_1.word
            else:
                used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect({adj_NP1_gender_check, 'accs'})
                if used_adj_modified_1 is not None:
                    used_adj[0] = used_adj_modified_1.word
            if amount_adj > 1:
                used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                    {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                if used_adj_modified_2 is not None:
                    used_adj[1] = used_adj_modified_2.word
                else:
                    used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect({adj_NP1_gender_check, 'accs'})
                    if used_adj_modified_2 is not None:
                        used_adj[1] = used_adj_modified_2.word
            if amount_adj > 2:
                used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                    {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                if used_adj_modified_3 is not None:
                    used_adj[2] = used_adj_modified_3.word
                else:
                    used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect({adj_NP1_gender_check, 'accs'})
                    if used_adj_modified_3 is not None:
                        used_adj[2] = used_adj_modified_3.word

            NP = f"{' '.join(used_adj)} {noun_acc}{dual_acc}"

        elif structure_NP_podtype == 2:
            adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
            adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
            if adjective_NP2 != False:
                adjective_NP2 = morph.parse(adjective_NP2)[0].inflect({adj_NP2_gender_check, 'loct'}).word

            adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

            NP = f"{noun_acc}{dual_acc} {preposition} {noun_loc}{dual_loc}{adjective_NP2_return}"

        return f"{verb_personal} {NP}"


def structure_V():
    structure_V_podtype = random.choice([1, 2])

    if structure_V_podtype == 1:
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
            used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect(
                {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
            if used_adj_modified_1 is not None:
                used_adj[0] = used_adj_modified_1.word
            else:
                used_adj_modified_1 = morph.parse(used_adj[0])[0].inflect({adj_NP1_gender_check, 'accs'})
                if used_adj_modified_1 is not None:
                    used_adj[0] = used_adj_modified_1.word
            if amount_adj > 1:
                used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect(
                    {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                if used_adj_modified_2 is not None:
                    used_adj[1] = used_adj_modified_2.word
                else:
                    used_adj_modified_2 = morph.parse(used_adj[1])[0].inflect({adj_NP1_gender_check, 'accs'})
                    if used_adj_modified_2 is not None:
                        used_adj[1] = used_adj_modified_2.word
            if amount_adj > 2:
                used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect(
                    {adj_NP1_gender_check, adj_NP1_animacy_check, 'accs'})
                if used_adj_modified_3 is not None:
                    used_adj[2] = used_adj_modified_3.word
                else:
                    used_adj_modified_3 = morph.parse(used_adj[2])[0].inflect({adj_NP1_gender_check, 'accs'})
                    if used_adj_modified_3 is not None:
                        used_adj[2] = used_adj_modified_3.word

            NP = f"{' '.join(used_adj)} {noun_nom}{dual_nom}"

        elif structure_NP_podtype == 2:
            adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
            adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
            if adjective_NP2 != False:
                adjective_NP2 = morph.parse(adjective_NP2)[0].inflect({adj_NP2_gender_check, 'loct'}).word

            adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

            NP = f"{noun_acc}{dual_acc} {preposition} {noun_loc}{dual_loc}{adjective_NP2_return}"

        noun_gender_check = morph.parse(noun_nom)[0].tag.gender
        noun_number_check = morph.parse(noun_nom)[0].tag.number
        verb_person_check = morph.parse(verb_personal)[0].tag.person
        verb_tense_check = morph.parse(verb_personal)[0].tag.tense

        grammemes = set()
        if verb_person_check != '3per' and verb_tense_check != 'past':
            grammemes = {'3per'}
        if noun_number_check:
            grammemes.add(noun_number_check)
        else:
            grammemes.add('sing')
        if noun_number_check == 'sing' and verb_tense_check == 'past' and noun_gender_check:
            grammemes.add(noun_gender_check)
        inflected_verb = morph.parse(verb_personal)[0].inflect(grammemes).word
        return f"{inflected_verb} {noun_nom}{dual_nom}"
    elif structure_V_podtype == 2:
        return verb_personal


def structure_NP():
    structure_NP_podtype = random.choice([1, 2, 3, 4, 5])
    if structure_NP_podtype == 1:
        amount_adj = random.choice([1, 2, 3])
        used_adj = random.sample(sorted(adjs.keys()), amount_adj)
        if amount_adj == 3:
            used_adj[0] = determiner
        adj_NP1_gender_check = morph.parse(noun_nom)[0].tag.gender
        used_adj[0] = morph.parse(used_adj[0])[0].inflect({adj_NP1_gender_check}).word

        if amount_adj > 1:
            used_adj[1] = morph.parse(used_adj[1])[0].inflect({adj_NP1_gender_check}).word

        if amount_adj > 2:
            used_adj[2] = morph.parse(used_adj[2])[0].inflect({adj_NP1_gender_check}).word

        return f"{' '.join(used_adj)} {noun_nom}{dual_nom}"

    elif structure_NP_podtype == 2:
        adjective_NP2 = random.choice([False, random.choice(list(adjs.keys()))])
        adj_NP2_gender_check = morph.parse(noun_loc)[0].tag.gender
        if adjective_NP2 != False:
            adjective_NP2 = morph.parse(adjective_NP2)[0].inflect({adj_NP2_gender_check, 'loct'}).word

        adjective_NP2_return = f" {adjective_NP2}" if adjective_NP2 else ""

        return f"{noun_nom}{dual_nom} {preposition} {adjective_NP2_return} {noun_loc}{dual_loc}"

    elif structure_NP_podtype == 3:
        adjective_NP3_1 = random.choice([False, random.choice(list(adjs.keys()))])

        adj_NP3_1_gender_check = morph.parse(noun_nom)[0].tag.gender

        if adjective_NP3_1 != False:
            adjective_NP3_1 = morph.parse(adjective_NP3_1)[0].inflect({adj_NP3_1_gender_check}).word
        adjective_NP3_1_return = f" {adjective_NP3_1}" if adjective_NP3_1 else ""

        adjective_NP3_2 = random.choice([False, random.choice(list(adjs.keys()))])
        adj_NP3_2_gender_check = morph.parse(noun_gen)[0].tag.gender
        adj_NP3_2_animacy_check = morph.parse(noun_gen)[0].tag.animacy
        if adj_NP3_2_animacy_check == None:
            adj_NP3_2_animacy_check = 'inan'
        adjective_NP3_2_modified = None
        adjective_NP3_2_return = ""

        if adjective_NP3_2:
            adjective_NP3_2_modified = morph.parse(adjective_NP3_2)[0].inflect(
                {adj_NP3_2_gender_check, adj_NP3_2_animacy_check, 'gent'})

            if adjective_NP3_2_modified is None:
                adjective_NP3_2_modified = morph.parse(adjective_NP3_2)[0].inflect(
                    {adj_NP3_2_gender_check, 'gent'})

            if adjective_NP3_2_modified:
                adjective_NP3_2_return = f" {adjective_NP3_2_modified.word}"

        return f"{adjective_NP3_1_return} {noun_nom}{dual_nom} {adjective_NP3_2_return} {noun_gen}{dual_gen}"

    elif structure_NP_podtype == 4:
        VP_NP4_num = random.choice([1, 2])
        that_NP4 = 'который'
        if VP_NP4_num == 1:
            VP_NP4 = f"{verb} {noun_acc}{dual_acc}"
        elif VP_NP4_num == 2:
            VP_NP4 = verb

            that_NP4_number_check = morph.parse(noun_nom)[0].tag.number
            if that_NP4_number_check == 'plur':
                that_NP4 = 'которые'
            else:
                that_NP4_gender_check = morph.parse(noun_nom)[0].tag.gender
                if that_NP4_gender_check == 'masc':
                    that_NP4 = 'который'
                elif that_NP4_gender_check == 'femn':
                    that_NP4 = 'которая'
                elif that_NP4_gender_check == 'neut':
                    that_NP4 = 'которое'
        return f"{noun_nom}{dual_nom}, {that_NP4} {VP_NP4}"

    elif structure_NP_podtype == 5:
        VP_NP5_num = random.choice([1, 2, 3])
        that_NP5 = 'который'
        if VP_NP5_num == 1:
            VP_NP5 = f"{verb} {noun_nom}{dual_nom}"
        elif VP_NP5_num == 2:
            VP_NP5 = verb_personal
        elif VP_NP5_num == 3:
            VP_NP5 = f"{verb_personal} {noun_acc}{dual_acc}"

            that_NP5_number_check = morph.parse(noun_nom)[0].tag.number
            if that_NP5_number_check == 'plur':
                if morph.parse(noun_nom)[0].tag.animacy == None:
                    that_NP5 = 'которые'
                else:
                    that_NP5 = 'которых'
            else:
                that_NP5_gender_check = morph.parse(noun_nom)[0].tag.gender
                if that_NP5_gender_check == 'masc':
                    if morph.parse(noun_nom)[0].tag.animacy == None:
                        that_NP5 = 'который'
                    else:
                        that_NP5 = 'которого'
                elif that_NP5_gender_check == 'femn':
                    that_NP5 = 'которую'
                elif that_NP5_gender_check == 'neut':
                    that_NP5 = 'которое'
        return f"{noun_nom}{dual_nom}, {that_NP5} {VP_NP5}"


structure_choice = random.choice([1, 2, 3])

if structure_choice == 1:
    print(structure_VP())
elif structure_choice == 2:
    print(structure_NP())
else:
    print(structure_V())
