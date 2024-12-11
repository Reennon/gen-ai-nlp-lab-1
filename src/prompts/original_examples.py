# MISC, ORG, PERS
EXAMPLE1: dict[str, str] = {
    "text": "український бізнес почав використовувати КСВ як інструмент формування репутації... наприклад, проект « Життєлюб » Гаріка Корогодського.",
    "labels": [
        {"label": "MISC", "text": "КСВ"},
        {"label": "ORG", "text": "Життєлюб"},
        {"label": "PERS", "text": "Гаріка Корогодського"}
    ]
}

# ORG, LOG, DATE, MON
EXAMPLE2: dict[str, str] = {
    "text": "Збройні Сили України напередодні анексії Криму та втручання у Донбасі перебували в стані недофінансування ... чи буде коли-небудь зроблена оцінка пожертв громадян у 2014 р., але йдеться про сотні мільйонів доларів.",
    "labels": [
        {"label": "ORG", "text": "Збройні Сили України"},
        {"label": "LOG", "text": "Криму"},
        {"label": "LOG", "text": "Донбасі"},
        {"label": "DATE", "text": "2014 р."},
        {"label": "MON", "text": "сотні мільйонів доларів"}
    ]
}

# ORG, LOG, DATE, QUANT, MON
EXAMPLE3: dict[str, str] = {
    "text": "Корпорація Roshen ... відновити протиповітряний « щит » над Києвом 2014 р. та придбала 430 снайперських гвинтівок, витративши 700-800 млн грн.",
    "labels": [
        {"label": "ORG", "text": "Roshen"},
        {"label": "LOG", "text": "Києвом"},
        {"label": "DATE", "text": "2014 р."},
        {"label": "QUANT", "text": "430"},
        {"label": "MON", "text": "700-800 млн грн"}
    ]
}

# ORG, MISC, LOG, DATE
EXAMPLE4: dict[str, str] = {
    "text": "Фармацевтична компанія « Фармак » впроваджує великі проекти в сфері КСВ, експортує продукцію у понад 20 країн світу, в тому числі до Німеччини, Австралії, Швеції, США. У березні 2018 р. « Фармак » розпочав пілотний проект « Екошкола ».",
    "labels": [
        {"label": "ORG", "text": "Фармак"},
        {"label": "MISC", "text": "КСВ"},
        {"label": "LOG", "text": "Німеччини"},
        {"label": "LOG", "text": "Австралії"},
        {"label": "LOG", "text": "Швеції"},
        {"label": "LOG", "text": "США"},
        {"label": "DATE", "text": "березні 2018 р."},
        {"label": "ORG", "text": "Екошкола"}
    ]
}

# JOB, PERS, ORG, DATE, LOG, PCT
EXAMPLE5: dict[str, str] = {
    "text": "Долучилися заступник голови райдержадміністрації Сергій Білецький ... у 2018 році школи Бориспільського району ... близько 30 % учнів потребують кваліфікованої логопедичної допомоги.",
    "labels": [
        {"label": "JOB", "text": "заступник голови райдержадміністрації"},
        {"label": "PERS", "text": "Сергій Білецький"},
        {"label": "ORG", "text": "райдержадміністрації"},
        {"label": "DATE", "text": "2018 році"},
        {"label": "LOG", "text": "Бориспільського району"},
        {"label": "PCT", "text": "30 %"}
    ]
}

# ORG, JOB, LOG, PERS
EXAMPLE6: dict[str, str] = {
    "text": "Міжнародний благодійний фонд « Покуття », фундатором якого є народний депутат України Андрій Іванчук, підтримує спортивні школи у Коломиї.",
    "labels": [
        {"label": "ORG", "text": "Міжнародний благодійний фонд « Покуття »"},
        {"label": "JOB", "text": "народний депутат"},
        {"label": "LOG", "text": "України"},
        {"label": "PERS", "text": "Андрій Іванчук"},
        {"label": "LOG", "text": "Коломиї"}
    ]
}

# JOB, PERS, ART
EXAMPLE7: dict[str, str] = {
    "text": "Краєзнавець і тележурналіст Василь Нагірний випустив двомовну книжечку « А . Kubler . Світло і тіні маестро ».",
    "labels": [
        {"label": "JOB", "text": "Краєзнавець"},
        {"label": "JOB", "text": "тележурналіст"},
        {"label": "PERS", "text": "Василь Нагірний"},
        {"label": "ART", "text": "А . Kubler . Світло і тіні маестро"}
    ]
}

# JOB, ORG, PERS, PERIOD
EXAMPLE8: dict[str, str] = {
    "text": "За словами заступника голови РДА Сергій Білецький наголосив ... Термін виконання: один тиждень.",
    "labels": [
        {"label": "JOB", "text": "заступника голови"},
        {"label": "ORG", "text": "РДА"},
        {"label": "PERS", "text": "Сергій Білецький"},
        {"label": "PERIOD", "text": "один тиждень"}
    ]
}

# DOC
EXAMPLE9: dict[str, str] = {
    "text": "Присутні обговорили необхідність привести у відповідність до законодавчих норм Статутів та Положень закладів освіти.",
    "labels": [
        {"label": "DOC", "text": "Статутів"},
        {"label": "DOC", "text": "Положень"}
    ]
}

# DATE, LOG, ORG, QUANT
EXAMPLE10: dict[str, str] = {
    "text": "У неділю, 4 березня, у Чернівцях у ліцеї № 4 відбулися змагання з бойового гопака. Участь взяли 58 учасників.",
    "labels": [
        {"label": "DATE", "text": "4 березня"},
        {"label": "LOG", "text": "Чернівцях"},
        {"label": "ORG", "text": "ліцеї № 4"},
        {"label": "QUANT", "text": "58"}
    ]
}

# No entities
EXAMPLE_NO_ENTITIES: dict[str, str] = {
    "text": "Це абсолютно нормальна практика, коли громади самостійно визначають пріоритети.",
    "labels": []
}

ELEVEN_SHOT_EXAMPLES_DICT: list[dict[str, str]] = [
    EXAMPLE1,
    EXAMPLE2,
    EXAMPLE3,
    EXAMPLE4,
    EXAMPLE5,
    EXAMPLE6,
    EXAMPLE7,
    EXAMPLE8,
    EXAMPLE9,
    EXAMPLE10,
    EXAMPLE_NO_ENTITIES
]
FIVE_SHOT_EXAMPLES_DICT: list[dict[str, str]] = [
    EXAMPLE1,
    EXAMPLE2,
    EXAMPLE3,
    EXAMPLE4,
    EXAMPLE_NO_ENTITIES
]
THREE_SHOT_EXAMPLES_DICT: list[dict[str, str]] = [
    EXAMPLE1,
    EXAMPLE2,
    EXAMPLE_NO_ENTITIES
]
ZERO_SHOT_EXAMPLES_DICT: list[dict[str, str]] = [
]
