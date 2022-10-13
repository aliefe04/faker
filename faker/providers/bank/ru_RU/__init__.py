from typing import Optional

from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``ru_RU`` locale.

    Sources for region codes, currency codes, and bank names:

    - https://ru.wikipedia.org/wiki/Коды_субъектов_Российской_Федерации
    - https://ru.wikipedia.org/wiki/Общероссийский_классификатор_валют
    - http://cbr.ru/credit/coreports/ko17012020.zip
    """

    country_code = "RU"

    region_codes = (
        "01",
        "03",
        "04",
        "05",
        "07",
        "08",
        "10",
        "11",
        "12",
        "14",
        "15",
        "17",
        "18",
        "19",
        "20",
        "22",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "32",
        "33",
        "34",
        "35",
        "36",
        "37",
        "38",
        "40",
        "41",
        "42",
        "44",
        "45",
        "46",
        "47",
        "49",
        "50",
        "52",
        "53",
        "54",
        "56",
        "57",
        "58",
        "60",
        "61",
        "63",
        "64",
        "65",
        "66",
        "67",
        "68",
        "69",
        "70",
        "71",
        "73",
        "75",
        "76",
        "77",
        "78",
        "79",
        "80",
        "81",
        "82",
        "83",
        "84",
        "85",
        "86",
        "87",
        "88",
        "89",
        "90",
        "91",
        "92",
        "93",
        "94",
        "95",
        "96",
        "97",
        "98",
        "99",
    )

    department_code_formats = (
        "0#",
        "1#",
        "2#",
        "3#",
        "4#",
        "5#",
        "6#",
        "7#",
        "8#",
        "9#",
    )

    credit_organization_code_formats = (
        "05#",
        "06#",
        "07#",
        "08#",
        "09#",
        "1##",
        "2##",
        "3##",
        "4##",
        "5##",
        "6##",
        "7##",
        "8##",
        "9##",
    )

    checking_account_codes = (
        [str(i) for i in range(102, 110)]
        + ["203", "204"]
        + [str(i) for i in range(301, 330)]
        + [str(i) for i in range(401, 409)]
        + [str(i) for i in range(411, 426)]
        + ["430"]
        + [str(i) for i in range(501, 527)]
    )

    organization_codes = (
        "01",
        "02",
        "03",
        "04",
    )

    currency_codes = (
        "008",
        "012",
        "032",
        "036",
        "044",
        "048",
        "050",
        "051",
        "052",
        "060",
        "064",
        "068",
        "072",
        "084",
        "090",
        "096",
        "104",
        "108",
        "116",
        "124",
        "132",
        "136",
        "144",
        "152",
        "156",
        "170",
        "174",
        "188",
        "191",
        "192",
        "203",
        "208",
        "214",
        "222",
        "230",
        "232",
        "238",
        "242",
        "262",
        "270",
        "292",
        "320",
        "324",
        "328",
        "332",
        "340",
        "344",
        "348",
        "352",
        "356",
        "360",
        "364",
        "368",
        "376",
        "388",
        "392",
        "398",
        "400",
        "404",
        "408",
        "410",
        "414",
        "417",
        "418",
        "422",
        "426",
        "430",
        "434",
        "440",
        "446",
        "454",
        "458",
        "462",
        "478",
        "480",
        "484",
        "496",
        "498",
        "504",
        "512",
        "516",
        "524",
        "532",
        "533",
        "548",
        "554",
        "558",
        "566",
        "578",
        "586",
        "590",
        "598",
        "600",
        "604",
        "608",
        "634",
        "643",
        "646",
        "654",
        "678",
        "682",
        "690",
        "694",
        "702",
        "704",
        "706",
        "710",
        "728",
        "748",
        "752",
        "756",
        "760",
        "764",
        "776",
        "780",
        "784",
        "788",
        "800",
        "807",
        "810",
        "818",
        "826",
        "834",
        "840",
        "858",
        "860",
        "882",
        "886",
        "894",
        "901",
        "931",
        "932",
        "933",
        "934",
        "936",
        "937",
        "938",
        "940",
        "941",
        "943",
        "944",
        "946",
        "947",
        "948",
        "949",
        "950",
        "951",
        "952",
        "953",
        "959",
        "960",
        "961",
        "962",
        "963",
        "964",
        "968",
        "969",
        "970",
        "971",
        "972",
        "973",
        "975",
        "976",
        "977",
        "978",
        "980",
        "981",
        "985",
        "986",
        "997",
        "998",
        "999",
    )

    banks = (
        "Абсолют Банк",
        "Авангард",
        "Аверс",
        "Автоградбанк",
        "Автокредитбанк",
        "Автоторгбанк",
        "Агора",
        "Агропромкредит",
        "Агророс",
        "Азиатско-Тихоокеанский Банк",
        "Азия-Инвест Банк",
        "Айсибиси Банк",
        "АК Барс",
        "Акибанк",
        "Акрополь",
        "Актив Банк",
        "Акцепт",
        "Александровский",
        "Алеф-Банк",
        "Алмазэргиэнбанк",
        "Алтайкапиталбанк",
        "Алтынбанк",
        "Альба Альянс",
        "Альтернатива",
        "Альфа-Банк",
        "Америкэн Экспресс Банк",
        "Апабанк",
        "Аресбанк",
        "Арзамас",
        "Байкалинвестбанк",
        "Байкалкредобанк",
        "Балаково-Банк",
        "Балтинвестбанк",
        'Банк "Санкт-Петербург"',
        'Банк "СКС"',
        "Банк 131",
        "Банк Берейт",
        "Банк Дом.рф",
        "Банк Жилищного Финансирования",
        "Банк Зенит",
        "Банк Зенит Сочи",
        "Банк Интеза",
        "Банк Казани",
        "Банк Корпоративного Финансирования",
        "Банк Кредит Свисс (Москва)",
        "Банк Оранжевый",
        "Банк Оренбург",
        "Банк ПСА Финанс Рус",
        "Банк Раунд",
        "Банк Реалист",
        "Банк РМП",
        "Банк РСИ",
        "Банк СГБ",
        "Банк Стандарт-Кредит",
        "Банк Финам",
        "Банк ЧБРР",
        "ББР Банк",
        "Белгородсоцбанк",
        "Бест Эффортс Банк",
        "Бизнес-Сервис-Траст",
        "БКС Банк",
        "БМ-Банк",
        "БМВ Банк",
        "БНП Париба Банк",
        "Братский АНКБ",
        "Быстробанк",
        "Бэнк Оф Чайна",
        "Вакобанк",
        "Великие Луки Банк",
        "Венец",
        "Веста",
        "Викинг",
        "Витабанк",
        "Вкабанк",
        "Владбизнесбанк",
        "Внешфинбанк",
        "Возрождение",
        "Вологжанин",
        "Восточный",
        "ВРБ",
        "Всероссийский Банк Развития Регионов",
        "ВТБ",
        "Вуз-Банк",
        "Вятич",
        "Газнефтьбанк",
        "Газпромбанк",
        "Газтрансбанк",
        "Газэнергобанк",
        "Гарант-Инвест",
        "Генбанк",
        "Геобанк",
        "Гефест",
        "Глобус",
        "Голдман Сакс Банк",
        "Горбанк",
        "Гута-Банк",
        "Далена",
        "Дальневосточный Банк",
        "Денизбанк Москва",
        "Держава",
        "Дж.П. Морган Банк Интернешнл",
        "Джей Энд Ти Банк",
        "Дойче Банк",
        "Долинск",
        "Дом-Банк",
        "Донкомбанк",
        "Дон-Тексбанк",
        "Дружба",
        "ЕАТП Банк",
        "Евразийский Банк",
        "Евроазиатский Инвестиционный Банк",
        "Евроальянс",
        "Еврофинанс Моснарбанк",
        "Екатеринбург",
        "Енисейский Объединенный Банк",
        "Ермак",
        "Живаго Банк",
        "Запсибкомбанк",
        "Заречье",
        "Заубер Банк",
        "Земельный",
        "Земский Банк",
        "Зираат Банк (Москва)",
        "Ижкомбанк",
        "ИК Банк",
        "Икано Банк",
        "Инбанк",
        "Инвестторгбанк",
        "Инг Банк (Евразия)",
        "Интерпрогрессбанк",
        "Интерпромбанк",
        "ИРС",
        "ИС Банк",
        "ИТ Банк",
        "Итуруп",
        "Ишбанк",
        "Йошкар-Ола",
        "Калуга",
        "Камский Коммерческий Банк",
        "Капитал",
        "Кетовский Коммерческий Банк",
        "Киви Банк",
        "Классик Эконом Банк",
        "Кольцо Урала",
        "Коммерцбанк (Евразия)",
        "Коммерческий Индо Банк",
        "Консервативный Коммерческий Банк",
        "Континенталь",
        "Космос",
        "Костромаселькомбанк",
        "Кошелев-Банк",
        "Креди Агриколь Киб",
        "Кредит Европа Банк",
        "Кредит Урал Банк",
        "Кремлевский",
        "Крокус-Банк",
        "Крона-Банк",
        "Кросна-Банк",
        "КС Банк",
        "Кубань Кредит",
        "Кубаньторгбанк",
        "Кузбассхимбанк",
        "Кузнецкбизнесбанк",
        "Кузнецкий",
        "Кузнецкий Мост",
        "Курган",
        "Курскпромбанк",
        "Кэб Эйчэнби Банк",
        "Ланта-Банк",
        "Левобережный",
        "Локо-Банк",
        "Майкопбанк",
        "Майский",
        "Максима",
        "МБА-Москва",
        "МВС Банк",
        "Мегаполис",
        "Международный Финансовый Клуб",
        "Мерседес-Бенц Банк Рус",
        "Металлинвестбанк",
        "Металлург",
        "Меткомбанк",
        "Мидзухо Банк (Москва)",
        "Мир Бизнес Банк",
        "МКБ",
        "Модульбанк",
        "Морган Стэнли Банк",
        "Морской Банк",
        "Москва-Сити",
        "Московский Индустриальный Банк",
        "Московский Коммерческий Банк",
        "Московский Кредитный Банк",
        "Московский Нефтехимический Банк",
        "Московский Областной Банк",
        "Московское Ипотечное Агентство",
        "Москоммерцбанк",
        "МС Банк Рус",
        "МСКБ",
        "МСП Банк",
        "МТИ Банк",
        "МТС-Банк",
        "Муниципальный Камчатпрофитбанк",
        "Нальчик",
        "Народный Банк",
        "Народный Банк Тувы",
        "Народный Доверительный Банк",
        "Натиксис Банк",
        "Национальный Банк Сбережений",
        "Национальный Инвестиционно-Промышленный",
        "Национальный Резервный Банк",
        "Национальный Стандарт",
        "НБД-Банк",
        "Невастройинвест",
        "Нейва",
        "Нефтепромбанк",
        "НИБ",
        "Нижневолжский Коммерческий Банк",
        "Нико-Банк",
        "НК Банк",
        "Новикомбанк",
        "Новобанк",
        "Новокиб",
        "Новый Век",
        "Новый Московский Банк",
        "Нокссбанк",
        "Ноосфера",
        "Норвик Банк",
        "Нордеа Банк",
        "НС Банк",
        "НФК",
        "Объединенный Банк Республики",
        "Объединенный Капитал",
        "Онего",
        "Оней Банк",
        "Орбанк",
        "Оргбанк",
        "ОТП Банк",
        "Первоуральскбанк",
        "Первый Дортрансбанк",
        "Первый Инвестиционный Банк",
        "Первый Клиентский Банк",
        "Пересвет",
        "Пермь",
        "Петербургский Социальный Ком. Банк",
        "Платина",
        "Плюс Банк",
        "Пойдём!",
        "Почта Банк",
        "Почтобанк",
        "Приморский Территориальный",
        "Приморье",
        "Примсоцбанк",
        "Приобье",
        "Прио-Внешторгбанк",
        "Прокоммерцбанк",
        "Проминвестбанк",
        "Промсвязьбанк",
        "Промсельхозбанк",
        "Промтрансбанк",
        "Профессионал Банк",
        "Профессиональный Инвестиционный Банк",
        "Прохладный",
        "Развитие-Столица",
        "Райффайзенбанк",
        "РБА",
        "Ренессанс Кредит",
        "Рента-Банк",
        "Ресо Кредит",
        "Республиканский Кредитный Альянс",
        "Ресурс-Траст",
        "РН Банк",
        "Росбанк",
        "Росбизнесбанк",
        "Росгосстрах Банк",
        "Росдорбанк",
        "Роскосмосбанк",
        "Россельхозбанк",
        "Российская Финансовая Корпорация",
        "Российский Национальный Коммерческий Банк",
        "Россита-Банк",
        "Россия",
        "Ростфинанс",
        "Росэксимбанк",
        "Роял Кредит Банк",
        "Руна-Банк",
        "Руснарбанк",
        "Русский Банк Сбережений",
        "Русский Региональный Банк",
        "Русский Стандарт",
        "Русфинанс Банк",
        "Русьуниверсалбанк",
        "РФИ Банк",
        "Саммит Банк",
        "Санкт-Петербургский Банк Инвестиций",
        "Саратов",
        "Саровбизнесбанк",
        "Сбербанк России",
        "Связь-Банк",
        "СДМ-Банк",
        "Севастопольский Морской Банк",
        "Северный Морской Путь",
        "Северный Народный Банк",
        "Северстройбанк",
        "Севзапинвестпромбанк",
        "Сельмашбанк",
        "Сервис Резерв",
        "Сетелем Банк",
        "СИАБ",
        "Сибсоцбанк",
        "Синко-Банк",
        "Система",
        "Сити Инвест Банк",
        "Ситибанк",
        "СКБ-Банк",
        "Славия",
        "Славянбанк",
        "Славянский Кредит",
        "Снежинский",
        "Собинбанк",
        "Совкомбанк",
        "Современные Стандарты Бизнеса",
        "Соколовский",
        "Солид Банк",
        "Солидарность",
        "Социум-Банк",
        "Союз",
        "Спецстройбанк",
        "Спиритбанк",
        "Спутник",
        "Ставропольпромстройбанк",
        "Столичный Кредит",
        "Стройлесбанк",
        "Сумитомо Мицуи Рус Банк",
        "Сургутнефтегазбанк",
        "СЭБ Банк",
        "Таврический Банк",
        "Таганрогбанк",
        "Тайдон",
        "Тамбовкредитпромбанк",
        "Татсоцбанк",
        "Тексбанк",
        "Тендер-Банк",
        "Тимер Банк",
        "Тинькофф Банк",
        "Тойота Банк",
        "Тольяттихимбанк",
        "Томскпромстройбанк",
        "Торжок",
        "Транскапиталбанк",
        "Трансстройбанк",
        "Траст",
        "Тэмбр-Банк",
        "Углеметбанк",
        "Унифондбанк",
        "Уралпромбанк",
        "Уралсиб",
        "Уралфинанс",
        "Уральский Банк Реконструкции и Развития",
        "Уральский Финансовый Дом",
        "УРИ Банк",
        "Финанс Бизнес Банк",
        "Финсервис",
        "ФК Открытие",
        "Фольксваген Банк Рус",
        "Фора-Банк",
        "Форбанк",
        "Форштадт",
        "Фридом Финанс",
        "Хакасский Муниципальный Банк",
        "Химик",
        "ХКФ Банк",
        "Хлынов",
        "Центрально-Азиатский",
        "Центр-Инвест",
        "Центрокредит",
        "ЦМРБанк",
        "Чайна Констракшн Банк",
        "Чайнасельхозбанк",
        "Челиндбанк",
        "Челябинвестбанк",
        "Эйч-Эс-Би-Си Банк (РР)",
        "Эко-Инвест",
        "Экономбанк",
        "Экси-Банк",
        "Экспобанк",
        "Экспресс-Волга",
        "Элита",
        "Эм-Ю-Эф-Джи Банк (Евразия)",
        "Энергобанк",
        "Энергомашбанк",
        "Энерготрансбанк",
        "Эс-Би-Ай Банк",
        "Ю Би Эс Банк",
        "Юг-Инвестбанк",
        "ЮМК Банк",
        "Юникредит Банк",
        "Юнистрим",
        "Яринтербанк",
    )

    def bic(self) -> str:
        """Generate a bank identification code (BIC).

        BIC is a bank identification code that is used in Russia.
        See https://ru.wikipedia.org/wiki/Банковский_идентификационный_код.
        """
        region: str = self.random_element(self.region_codes)
        department_code: str = self.numerify(self.random_element(self.department_code_formats))
        credit_organization_code: str = self.numerify(self.random_element(self.credit_organization_code_formats))
        return f"04{region}{department_code}{credit_organization_code}"

    def correspondent_account(self) -> str:
        """Generate a correspondent account number.

        Correspondent account is established to handle various financial
        operations between financial institutions.
        See https://ru.wikipedia.org/wiki/Корреспондентский_счёт.
        """
        credit_organization_code = self.numerify(self.random_element(self.credit_organization_code_formats))
        return "301" + self.numerify("#" * 14) + credit_organization_code

    def checking_account(self) -> str:
        """Generate a checking account number.

        Checking account is used in banks to handle financial operations of
        clients.
        See https://ru.wikipedia.org/wiki/Расчётный_счёт.
        """
        account: str = self.random_element(self.checking_account_codes)
        organization: str = self.random_element(self.organization_codes)
        currency: str = self.random_element(self.currency_codes)
        return account + organization + currency + self.numerify("#" * 12)

    def bank(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        """Generate a bank name."""
        return self.random_element(self.banks, min_length, max_length)
