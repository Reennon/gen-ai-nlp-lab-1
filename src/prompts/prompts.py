from langchain.prompts import PromptTemplate

from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel


class BasePrompt(BaseModel):
    template: str = """"""
    input_variables: list[str] = []

    @property
    def prompt_template(self):
        return PromptTemplate(
            template=self.template,
            input_variables=self.input_variables
        )

class NERPrompt1(BasePrompt):
    template: str = """Твоє завдання – виділити всі сутності у наданому тексті за наведеними категоріями та вивести їх у форматі JSON-списку:

Категорії сутностей:
- ART: артефакт (створений людиною предмет)
- DATE: дата (календарна дата, рік)
- DOC: документ (назви документів)
- JOB: посада (професійний титул, робоча позиція)
- LOG: місце (географічні об’єкти, назви країн, міст, річок тощо)
- MISC: різне (інші сутності, не підпадають під інші категорії)
- MON: гроші (сума, валюта)
- ORG: організація (установи, компанії, заклади)
- PCT: відсоток (число у відсотках)
- PERIOD: період (тривалість часу)
- PERS: особа (людські імена, прізвища)
- QUANT: кількість (числові значення)
- TIME: час (конкретний момент доби)

Формат відповіді: список об’єктів у JSON, кожен об’єкт має поля:
"label" – категорія сутності
"text" – фрагмент тексту сутності з оригінального тексту без змін

Не виводь дублікати знайдених сутностей.

Нижче наведено приклади формату та стилю розпізнавання сутностей:
{examples}

Вхідний текст:
{text}

Спочатку ознайомся з прикладами, потім визнач усі сутності у наведеному тексті.
"""
    input_variables: list[str] = ["text", "examples"]


class NERPrompt2(BasePrompt):
    template: str = """Проаналізуй наведений нижче текст і визнач усі сутності за даними категоріями:

Категорії сутностей:
- ART: артефакт
- DATE: дата
- DOC: документ
- JOB: посада
- LOG: місце
- MISC: різне
- MON: гроші
- ORG: організація
- PCT: відсоток
- PERIOD: період
- PERS: особа
- QUANT: кількість
- TIME: час

Всі сутності виведи у JSON-списку, де кожен елемент має формат:
{"label": "КАТЕГОРІЯ", "text": "ВИХІДНИЙ ТЕКСТ СУТНОСТІ"}

Ось приклади правильної роботи (взято із змінної examples):
{examples}

Текст для аналізу:
{text}

Прошу виділити всі сутності згідно з указаними категоріями.
"""
    input_variables: list[str] = ["text", "examples"]

class NERPrompt3(BasePrompt):
    template: str = """Твоє завдання – виділити іменовані сутності з наведеного тексту відповідно до таких категорій:

Категорії сутностей:
- ART: артефакт
- DATE: дата
- DOC: документ
- JOB: посада
- LOG: місце
- MISC: різне
- MON: гроші
- ORG: організація
- PCT: відсоток
- PERIOD: період
- PERS: особа
- QUANT: кількість
- TIME: час

Відповідь надай у форматі JSON-списку об’єктів з полями "label" та "text".

Приклади (змінна examples):
{examples}

Текст для аналізу:
{text}

Використай наведені приклади як орієнтир.
"""
    input_variables: list[str] = ["text", "examples"]


class NERPrompt4(BasePrompt):
    template: str = """Прочитай цей текст та знайди у ньому всі іменовані сутності. Класифікуй їх за такими категоріями:

Категорії сутностей:
- ART: артефакт
- DATE: дата
- DOC: документ
- JOB: посада
- LOG: місце
- MISC: різне
- MON: гроші
- ORG: організація
- PCT: відсоток
- PERIOD: період
- PERS: особа
- QUANT: кількість
- TIME: час

Результат оформи як JSON-список, де кожен об’єкт містить:
"label" – категорія сутності
"text" – оригінальний текст сутності

Ознайомся з прикладами, які надано у змінній examples:
{examples}

Тепер застосуй цей підхід до наведеного тексту:
{text}
"""
    input_variables: list[str] = ["text", "examples"]
